from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.card import Card
from app.models.layout import Layout
import os
from dotenv import load_dotenv
from random import randint
import random

# example_bp = Blueprint('example_bp', __name__)
layout_bp = Blueprint("layout", __name__, url_prefix="/layout")
hello_world_bp = Blueprint("hello_world", __name__)
cards_bp = Blueprint("cards", __name__, url_prefix="/cards")


load_dotenv()


@hello_world_bp.route("/hello-world", methods=["GET"])
def hello_world():
    my_beautiful_response_body = "Hello, World!"
    return my_beautiful_response_body


@layout_bp.route("/paw", methods=["GET"])
def get_paw_layout():
    cards = Card.query.all()
    ranCards= [random.sample(cards, 1) for x in range(3)]
    layout_response = []
    # print(ranCards)
    for element in ranCards:
        for card in element:
            layout_response.append(
                {
                    "card name": card.card_name,
                    "general": card.card_general,})
    
    return jsonify(layout_response)


@cards_bp.route("", methods=["GET", "POST"])
def get_cards():
    if request.method == "GET":
        cards = Card.query.all()
        print(cards)
        cards_response = []
        for card in cards:
            cards_response.append(
                {
                    "card ID": card.card_id,
                    "card_name": card.card_name,
                    "card_general": card.card_general,
                    "card_upright": card.card_upright,
                    "card_reversed": card.card_reversed,
                    # <img src="{{ url_for('static', filename='images/' + card.card_image_location) }}">
                }
            )
        return jsonify(cards_response)

    elif request.method == "POST":
        request_body = request.get_json()
        card_name = request_body.get("card_name")
        card_general = request_body.get("card_general")
        card_upright = request_body.get("card_upright")
        card_reversed = request_body.get("card_reversed")
        card_image_location = request_body.get("card_image_location")
        new_card = Card(
            card_name=request_body["card_name"],
            card_general=request_body["card_general"],
            card_upright=request_body["card_upright"],
            card_reversed=request_body["card_reversed"],
            card_image_location=request_body["card_image_location"],
        )
        db.session.add(new_card)
        db.session.commit()

    return make_response(f"Card {new_card.card_name} successfully created", 201)

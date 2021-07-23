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

# generic route to test it works
@hello_world_bp.route("/hello-world", methods=["GET"])
def hello_world():
    my_beautiful_response_body = "Hello, World!"
    return my_beautiful_response_body

#route to get paw print layout
@layout_bp.route("/paw", methods=["GET"])
def get_paw_layout():
    cards = Card.query.all()
    ranCards = [random.sample(cards, 3)];
    layout_response = []
    # print(ranCards)
    for element in ranCards:
        for card in element:
            layout_response.append(
                {
                    "placement": ranCards.index(element),
                    "id": card.id,
                    "name": card.name,
                    "general": card.general,
                    "upright": card.upright,
                    "reversed": card.reversed,
                    })
    
    return jsonify(layout_response)

#route to get all the cards or post a new one
@cards_bp.route("", methods=["GET", "POST"])
def get_cards():
    if request.method == "GET":
        cards = Card.query.all()
        print(cards)
        cards_response = []
        for card in cards:
            cards_response.append(
                {
                    "id": card.id,
                    "name": card.name,
                    "general": card.general,
                    "upright": card.upright,
                    "reversed": card.reversed,
                }
            )
        return jsonify(cards_response)

    elif request.method == "POST":
        request_body = request.get_json()
        name = request_body.get("name")
        general = request_body.get("general")
        upright = request_body.get("upright")
        reversed = request_body.get("reversed")
        image_location = request_body.get("image_location")
        new_card = Card(
            name=request_body["name"],
            general=request_body["general"],
            upright=request_body["upright"],
            reversed=request_body["reversed"],
            image_location=request_body["image_location"],
        )
        db.session.add(new_card)
        db.session.commit()

    return make_response(f"Card {new_card.name} successfully created", 201)

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
hello_world_bp = Blueprint("", __name__, url_prefix="/")
cards_bp = Blueprint("cards", __name__, url_prefix="/cards")


load_dotenv()

# generic route to test it works
@hello_world_bp.route("", methods=["GET"])
def hello_world():
    my_beautiful_response_body = "Greetings from the Cat Realm"
    return my_beautiful_response_body

#route to get paw print layout
@layout_bp.route("/paw", methods=["GET"])
def get_paw_layout():
    cards = Card.query.all()
    ranCards = [random.sample(cards, 5)];
    layout_response = []
    
    for element in ranCards:
        for card in element:
            cardDir = random.choice([True, False])
            if cardDir == True:
                layout_response.append(
                    {
                        "card_id": card.card_id,
                        "card_name": card.card_name,
                        "card_general": card.card_general,
                        "card_upright": card.card_upright,
                        "card_image": card.card_image_location,
                        "direction": cardDir,
                        })
            elif cardDir == False:
                layout_response.append(
                    {
                        "card_id": card.card_id,
                        "card_name": card.card_name,
                        "card_general": card.card_general,
                        "card_reversed": card.card_reversed,
                        "card_image": card.card_image_location,
                        "direction": cardDir,
                    })  
    return jsonify(layout_response)

#route to get all the cards or post a new one
@cards_bp.route("", methods=["GET", "POST"])
def get_cards():
    if request.method == "GET":
        cards = Card.query.all()
        cards_response = []
        for card in cards:
                cards_response.append(
                    {
                        "card_id": card.card_id,
                        "card_name": card.card_name,
                        "card_general": card.card_general,
                        "card_upright": card.card_upright,
                        "card_reversed": card.card_reversed,
                        "image-location": card.card_image_location,
                    }               
            )
        
        return jsonify(cards_response)

    elif request.method == "POST":
        request_body = request.get_json()
        card_id = request_body.get("card_id"),
        card_name = request_body.get("name")
        card_general = request_body.get("general")
        card_upright = request_body.get("upright")
        card_reversed = request_body.get("card_reversed")
        card_image_location = request_body.get("card_image_location")
        new_card = Card(
            card_id=request_body["card_id"],
            card_name=request_body["card_name"],
            card_general=request_body["card_general"],
            card_upright=request_body["card_upright"],
            card_reversed=request_body["card_reversed"],
            card_image_location=request_body["card_image_location"],
        )
        db.session.add(new_card)
        db.session.commit()

    return make_response(f"Card {new_card.card_name} successfully created", 201)

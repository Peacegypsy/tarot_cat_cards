from flask import Blueprint, request, jsonify, make_response
from app import db
from app.models.card import Card

import os
from dotenv import load_dotenv

# example_bp = Blueprint('example_bp', __name__)
layout_bp = Blueprint("layout", __name__, url_prefix="/layout")
hello_world_bp = Blueprint("hello_world", __name__)

load_dotenv()


@hello_world_bp.route("/hello-world", methods=["GET"])
def hello_world():
    my_beautiful_response_body = "Hello, World!"
    return my_beautiful_response_body

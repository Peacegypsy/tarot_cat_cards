from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from dotenv import load_dotenv
import os
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
load_dotenv()


def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("SQLALCHEMY_DATABASE_URI")

    # Import models here for Alembic setup
    # from app.models.ExampleModel import ExampleModel
    from .routes import hello_world_bp

    app.register_blueprint(hello_world_bp)

    from .routes import cards_bp

    app.register_blueprint(cards_bp)

    from .routes import layout_bp

    app.register_blueprint(layout_bp)

    db.init_app(app)
    migrate.init_app(app, db)

    # Register Blueprints here
    # from .routes import example_bp
    # app.register_blueprint(example_bp)

    CORS(app)
    return app

from app import db


class Card(db.Model):
    card_id = db.Column(db.Integer, primary_key=True)
    card_name = db.Column(db.String(100), nullable=False)
    card_general = db.Column(db.Text, nullable=False)
    card_upright = db.Column(db.Text, nullable=False)
    card_reversed = db.Column(db.Text, nullable=False)
    card_image_location = db.Column(db.String)

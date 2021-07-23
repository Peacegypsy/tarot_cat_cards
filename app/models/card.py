from app import db


class Card(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    general = db.Column(db.Text, nullable=False)
    upright = db.Column(db.Text, nullable=False)
    reversed = db.Column(db.Text, nullable=False)
    image_location = db.Column(db.String)

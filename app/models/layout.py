from app import db

class Layout(db.Model):
    layout_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String, nullable=False)
    #cards = db.relationship('Card', backref='layout', lazy=True)
    
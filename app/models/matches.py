from .db import db, environment, SCHEMA, add_prefix_for_prod

class Match(db.Model):
    __tablename__ = "matches"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    winner_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    losers_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))

    
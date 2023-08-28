from .db import db, environment, SCHEMA, add_prefix_for_prod

class Live_Game(db.Model):
    __tablename__ = "live_games"

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.id")))
    mana = db.Column(db.Integer, nullable=False)
from .db import db, environment, SCHEMA, add_prefix_for_prod

class Character_Move(db.Moel):
    __tablename__ = 'character_moves'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    character_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("characters.id")))
    move_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("moves.id")))
    current_cooldown = db.Column(db.Integer, nullable=False)

    characters = db.relationship("Character", back_populates="moves")

    
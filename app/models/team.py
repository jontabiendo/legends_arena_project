from .db import db, environment, SCHEMA, add_prefix_for_prod

class Team(db.Model, UserMixin):
    __tablename__ = 'teams'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    player_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("users.team_id")))
    character_id = db.Column(db.Integer, db.ForeignKey(add_prefix_for_prod("characters.id")))
    health = db.Column(db.Integer, default=100)
    
    effects = db.relationship("Move", back_populates="affecting")
    character = db.relationship("Character", back_populates="team")

    def to_dict(self):
        return {
            "id": self.id,
            "owner_id": self.owner_id,
            "character": self.character,
            "health": self.health,
            "effects": self.effects
        }
from .db import db, environment, SCHEMA, add_prefix_for_prod

class Character(db.Model):
    __tablename__ = 'characters'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(12), nullable=False)
    title = db.Column(db.String(20), nullable=False)
    region = db.Column(db.String(20), nullable=False)
    about = db.Column(db.String(255), nullable=False)
    classification = db.Column(db.String(20), nullable=False)

    moves = db.relationship("Character_Move", back_populates="character")
    associations = db.relationship("Character", back_populates="associations")
    team = db.relationship("Team", back_populates="character")

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "region": self.region,
            "about": self.about,
            "moves": self.moves,
            "associations": self.associations
        }
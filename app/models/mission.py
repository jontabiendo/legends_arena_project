from .db import db, environment, SCHEMA, add_prefix_for_prod


class User(db.Model):
    __tablename__ = 'missions'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(255))
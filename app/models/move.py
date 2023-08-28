from .db import db, environment, SCHEMA, add_prefix_for_prod

class Move(db.Moel):
    __tablename__ = 'moves'

    if environment == "production":
        __table_args__ = {'schema': SCHEMA}

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(255), nullable=False)
    cooldown = db.Column(db.Integer, nullable=False)
    cost = db.Column(db.Integer, nullable=False)
    damage = db.Column(db.Integer, nullable=False)
    target = db.Column(db.String(10), nullable=False) #ally vs enemy
    num_targets = db.Column(db.Integer, nullable=False)
    damage_over_time = db.Column(db.Integer)
    dot_duration = db.Column(db.Integer)
    shield_amount = db.Column(db.Integer)
    shield_duration = db.Column(db.Integer)
    is_ranged = db.Column(db.Boolean)
    is_hidden = db.Column(db.Boolean)
    stun_duration = db.Column(db.Integer)
    damage_reduction = db.Column(db.Integer)
    dr_duration = db.Column(db.Integer)
    damage_amp = db.Column(db.Integer)
    da_duration = db.Column(db.Integer)
    is_spell = db.Column(db.Boolean)
    is_chain = db.Column(db.Boolean)
    root_duration = db.Column(db.Integer)
    vamp_amount = db.Column(db.Integer)
    vamp_duration = db.Column(db.Integer)
    silence_duration = db.Column(db.Integer)
    heal_amount = db.Column(db.Integer)
    max_health_increase = db.Column(db.Integer)
    taunt_duration = db.Column(db.Integer)
    reveals = db.Column(db.Boolean)
    marks = db.Column(db.Boolean)
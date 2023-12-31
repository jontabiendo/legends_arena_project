"""empty message

Revision ID: 377cd262cc33
Revises: 
Create Date: 2023-08-28 17:48:09.252484

"""
from alembic import op
import sqlalchemy as sa

import os
environment = os.getenv("FLASK_ENV")
SCHEMA = os.environ.get("SCHEMA")

# revision identifiers, used by Alembic.
revision = '377cd262cc33'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('characters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=12), nullable=False),
    sa.Column('title', sa.String(length=20), nullable=False),
    sa.Column('region', sa.String(length=20), nullable=False),
    sa.Column('about', sa.String(length=255), nullable=False),
    sa.Column('classification', sa.String(length=20), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('teams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('health', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.ForeignKeyConstraint(['player_id'], ['users.team_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=40), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('hashed_password', sa.String(length=255), nullable=False),
    sa.Column('rank', sa.String(length=10), nullable=False),
    sa.Column('level', sa.Integer(), nullable=False),
    sa.Column('wins', sa.Integer(), nullable=False),
    sa.Column('losses', sa.Integer(), nullable=False),
    sa.Column('team_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['team_id'], ['teams.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('username')
    )
    op.create_table('live_games',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('player_id', sa.Integer(), nullable=True),
    sa.Column('mana', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['player_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('matches',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('winner_id', sa.Integer(), nullable=True),
    sa.Column('losers_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['losers_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['winner_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('moves',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('character_id', sa.Integer(), nullable=True),
    sa.Column('name', sa.String(length=20), nullable=False),
    sa.Column('description', sa.String(length=255), nullable=False),
    sa.Column('cooldown', sa.Integer(), nullable=False),
    sa.Column('cost', sa.Integer(), nullable=False),
    sa.Column('damage', sa.Integer(), nullable=False),
    sa.Column('target', sa.String(length=10), nullable=False),
    sa.Column('num_targets', sa.Integer(), nullable=False),
    sa.Column('damage_over_time', sa.Integer(), nullable=True),
    sa.Column('dot_duration', sa.Integer(), nullable=True),
    sa.Column('shield_amount', sa.Integer(), nullable=True),
    sa.Column('shield_duration', sa.Integer(), nullable=True),
    sa.Column('is_ranged', sa.Boolean(), nullable=True),
    sa.Column('is_hidden', sa.Boolean(), nullable=True),
    sa.Column('stun_duration', sa.Integer(), nullable=True),
    sa.Column('damage_reduction', sa.Integer(), nullable=True),
    sa.Column('dr_duration', sa.Integer(), nullable=True),
    sa.Column('damage_amp', sa.Integer(), nullable=True),
    sa.Column('da_duration', sa.Integer(), nullable=True),
    sa.Column('is_spell', sa.Boolean(), nullable=True),
    sa.Column('is_chain', sa.Boolean(), nullable=True),
    sa.Column('root_duration', sa.Integer(), nullable=True),
    sa.Column('vamp_amount', sa.Integer(), nullable=True),
    sa.Column('vamp_duration', sa.Integer(), nullable=True),
    sa.Column('silence_duration', sa.Integer(), nullable=True),
    sa.Column('heal_amount', sa.Integer(), nullable=True),
    sa.Column('max_health_increase', sa.Integer(), nullable=True),
    sa.Column('taunt_duration', sa.Integer(), nullable=True),
    sa.Column('reveals', sa.Boolean(), nullable=True),
    sa.Column('marks', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['character_id'], ['characters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###
    if environment == "production":
        op.execute(f"ALTER TABLE users SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE matches SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE live_games SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE moves SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE teams SET SCHEMA {SCHEMA};")
        op.execute(f"ALTER TABLE characters SET SCHEMA {SCHEMA};")


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('moves')
    op.drop_table('matches')
    op.drop_table('live_games')
    op.drop_table('users')
    op.drop_table('teams')
    op.drop_table('characters')
    # ### end Alembic commands ###

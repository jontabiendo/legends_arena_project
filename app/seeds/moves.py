from app.models import db, Move, environment, SCHEMA
from sqlalchemy.sql import text

def seed_moves():
    rangers_focus = Move(
        name = "Ranger's Focus",
        description = "Ashe deals 20 damage the next 2 turns to a single target. If that target uses a movement ability during this time, the cooldown is increased by 1 turn",
        cooldown = 3,
        cost = 1,
        damage = 20,
        num_targets = 1,
        damage_over_time = 1,
        dot_duration = 1
    )
    volley = Move(
        name = "Volley",
        description = "Ashe fires a volley of arrows to all enemies dealing 15 damage to each",
        cooldown = 3,
        cost = 1,
        damage = 15,
        num_targets = 3,
    )
    hawkshot = Move(
        name = "Hawkshot",
        description = "Ashe scouts the enemy team, revealing any hidden effects or abilities the next 2 turns",
        cooldown = 4,
        cost = 1,
        damage = 0,
        num_targets = 3,
        reveals = True
    )
    crystal_arrow = Move(
        name = "Enchanted Crystal Arrow",
        description = "Ashe fires an enchanted crystal arrow at a single target, dealing 45 damage and stunning them for 2 turns",
        cooldown = 6,
        cost = 3,
        damage = 45,
        num_targets = 1,
        stun_duration = 2
    )
    decisive_strike = Move(
        name = "Decisive Strike",
        description = "Garen attacks a single enemy dealing 25 damage to a single target, stunning them for 1 round",
        cooldown = 3,
        cost = 1,
        damage = 25,
        num_targets = 1,
        stun_duration = 1
    )
    courage = Move(
        name = "Courage",
        description = "Garen shields himself, blocking 20 damage. The following 2 turns, garen takes 10% less damage",
        cooldown = 4,
        cost = 1,
        damage = 0,
        num_targets = 1,
        damage_reduction = 0.1,
        dr_duration = 2
    )
    judgement = Move(
        name = "Judgement",
        description = "Garen deals 10 damage to all enemies for 3 turns. During this time, enemies affected by this ability will take 20% more damage from Garen and his allies",
        cooldown = 4,
        cost = 1,
        damage = 10,
        num_targets = 3,
        dmage_amp = 0.2,
        da_duration = 3
    )
    demacian_justice = Move(
        name = "Demacian Justice",
        description = "Garen deals 50 damage to a single target",
        cooldown = 6,
        cost = 3,
        damage = 50,
        num_targets = 1,
    )
    overload = Move(
        name = "Overload",
        description = "Ryze deals 20 damage to a single enemy. If the enemy is marked by 'Spell Flux', it does 10 bonus damage and bounces to all enemies marked by 'Spell Flux', consuming the mark",
        cooldown = 2,
        cost = 1,
        damage = 20,
        num_targets = 1,
        is_chain = True
    )
    rune_prison = Move(
        name = "Rune Prison",
        description = "Ryze deals 20 damage to a single enemy. If the enemy is marked by 'Spell Flux', they take 10 bonus damage and are rooted for 1 turn, consuming the mark.",
        cooldown = 3,
        cost = 1,
        damage = 20,
        num_targets = 1,
    )
    spell_flux = Move(
        name = "Spell Flux",
        description = "Ryze deals 10 damage to a single enemy, marking them with 'Spell Flux'. If the enemy is already marked by 'Spell Flux', it bounces to all enemies, marking them with 'Spell Flux'",
        cooldown = 1,
        cost = 1,
        damage = 10,
        num_targets = 1,
        marks = True
    )
    desperate_power = Move(
        name = "Desperate Power",
        description = "For the next 3 turns, Ryze's abilities deal 50% bonus damage and heal him for 10 health per enemy hit",
        cooldown = 8,
        cost = 3,
        damage = 0,
        num_targets = 1,
        damage_amp = 1.5,
        da_duration = 3,
        vamp = 10
    )
    rupture = Move(
        name = "Rupture",
        description = "Cho'gath deals 20 damage to all enemies",
        cooldown = 3,
        cost = 1,
        damage = 20,
        num_targets = 3,
    ),
    feral_scream = Move(
        name = "Feral Scream",
        description = "Cho'gath deals 10 damage to all enemies, silencing them for 1 turn",
        cooldown = 3,
        cost = 1,
        damage = 10,
        num_targets = 3,
        silence_duration = 1
    )
    vorpal_spikes = Move(
        name = "Vorpal Spikes",
        description = "Cho'gath deals 20 damage to a single enemy for 3 turns. All enemies also take 10% of their current health as damage",
        cooldown = 4,
        cost = 1,
        damage = 20,
        num_targets = 1,
        damage_over_time = 20,
        dot_duration = 2
    )
    feast = Move(
        name = "Feast",
        description = "Cho'gath does 40 damage to a single enemy. If this kills the enemy, Cho'gath heals 20% of his max-health and then gains 20 max-health",
        cooldown = 6,
        cost = 3,
        damage = 40,
        num_targets = 1,
    )

def undo_moves():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.moves RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()
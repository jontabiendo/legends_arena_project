from app.models import db, Move, environment, SCHEMA
from sqlalchemy.sql import text

def seed_moves():
    rangers_focus = Move(
        name = "Ranger's Focus",
        character_id = 1,
        description = "Ashe deals 20 damage the next 2 turns to a single target. If that target uses a movement ability during this time, the cooldown is increased by 1 turn",
        target = "enemy",
        cooldown = 3,
        cost = 1,
        damage = 20,
        num_targets = 1,
        damage_over_time = 1,
        dot_duration = 1
    )
    volley = Move(
        name = "Volley",
        character_id = 1,
        description = "Ashe fires a volley of arrows to all enemies dealing 15 damage to each",
        target = "enemy",
        cooldown = 3,
        cost = 1,
        damage = 15,
        num_targets = 3,
    )
    hawkshot = Move(
        name = "Hawkshot",
        character_id = 1,
        description = "Ashe scouts the enemy team, revealing any hidden effects or abilities the next 2 turns",
        target = "enemy",
        cooldown = 4,
        cost = 1,
        damage = 0,
        num_targets = 3,
        reveals = True
    )
    crystal_arrow = Move(
        name = "Enchanted Crystal Arrow",
        character_id = 1,
        description = "Ashe fires an enchanted crystal arrow at a single target, dealing 45 damage and stunning them for 2 turns",
        target = "enemy",
        cooldown = 6,
        cost = 3,
        damage = 45,
        num_targets = 1,
        stun_duration = 2
    )
    decisive_strike = Move(
        name = "Decisive Strike",
        character_id = 2,
        description = "Garen attacks a single enemy dealing 25 damage to a single target, stunning them for 1 round",
        target = "enemy",
        cooldown = 3,
        cost = 1,
        damage = 25,
        num_targets = 1,
        stun_duration = 1
    )
    courage = Move(
        name = "Courage",
        character_id = 2,
        description = "Garen shields himself, blocking 20 damage. The following 2 turns, garen takes 10% less damage",
        target = "ally",
        cooldown = 4,
        cost = 1,
        damage = 0,
        num_targets = 1,
        damage_reduction = 0.9,
        dr_duration = 2
    )
    judgement = Move(
        name = "Judgement",
        character_id = 2,
        description = "Garen deals 10 damage to all enemies for 3 turns. During this time, enemies affected by this ability will take 20% more damage from Garen and his allies",
        target = "enemy",
        cooldown = 4,
        cost = 1,
        damage = 10,
        num_targets = 3,
        dmage_amp = 1.2,
        da_duration = 3
    )
    demacian_justice = Move(
        name = "Demacian Justice",
        character_id = 2,
        description = "Garen deals 50 damage to a single target",
        target = "enemy",
        cooldown = 6,
        cost = 3,
        damage = 50,
        num_targets = 1,
    )
    overload = Move(
        name = "Overload",
        character_id = 3,
        description = "Ryze deals 20 damage to a single enemy. If the enemy is marked by 'Spell Flux', it does 10 bonus damage and bounces to all enemies marked by 'Spell Flux', consuming the mark",
        target = "enemy",
        cooldown = 2,
        cost = 1,
        damage = 20,
        num_targets = 1,
        is_chain = True
    )
    rune_prison = Move(
        name = "Rune Prison",
        character_id = 3,
        description = "Ryze deals 20 damage to a single enemy. If the enemy is marked by 'Spell Flux', they take 10 bonus damage and are rooted for 1 turn, consuming the mark.",
        cooldown = 3,
        target = "enemy",
        cost = 1,
        damage = 20,
        num_targets = 1,
    )
    spell_flux = Move(
        name = "Spell Flux",
        character_id = 3,
        description = "Ryze deals 10 damage to a single enemy, marking them with 'Spell Flux'. If the enemy is already marked by 'Spell Flux', it bounces to all enemies, marking them with 'Spell Flux'",
        target = "enemy",
        cooldown = 1,
        cost = 1,
        damage = 10,
        num_targets = 1,
        marks = True
    )
    desperate_power = Move(
        name = "Desperate Power",
        character_id = 3,
        description = "For the next 3 turns, Ryze's abilities deal 50% bonus damage and heal him for 10 health per enemy hit",
        cooldown = 8,
        target = "ally",
        cost = 3,
        damage = 0,
        num_targets = 1,
        damage_amp = 1.5,
        da_duration = 3,
        vamp = 10
    )
    rupture = Move(
        name = "Rupture",
        character_id = 4,
        description = "Cho'gath deals 20 damage to all enemies",
        target = "enemy",
        cooldown = 3,
        cost = 1,
        damage = 20,
        num_targets = 3,
    ),
    feral_scream = Move(
        name = "Feral Scream",
        character_id = 4,
        description = "Cho'gath deals 10 damage to all enemies, silencing them for 1 turn",
        target = "enemy",
        cooldown = 3,
        cost = 1,
        damage = 10,
        num_targets = 3,
        silence_duration = 1
    )
    vorpal_spikes = Move(
        name = "Vorpal Spikes",
        character_id = 4,
        description = "Cho'gath deals 20 damage to a single enemy for 3 turns. All enemies also take 10% of their current health as damage",
        target = "enemy",
        cooldown = 4,
        cost = 1,
        damage = 20,
        num_targets = 1,
        damage_over_time = 20,
        dot_duration = 2
    )
    feast = Move(
        name = "Feast",
        character_id = 4,
        description = "Cho'gath does 40 damage to a single enemy. If this kills the enemy, Cho'gath heals 20% of his max-health and then gains 20 max-health",
        target = "enemy",
        cooldown = 6,
        cost = 3,
        damage = 40,
        num_targets = 1,
    )
    winters_bite = Move(
        name = "Winter's Bite",
        character_id = 5,
        description = "Propels freezing ice from his shield dealing 20 damage marking the target for 3 turns. If the target is attacked by one of Braum's allies during this time, they are stunned 1 turn.",
        target = "enemy",
        cooldown = 4,
        cost = 1,
        damage = 20,
        num_targets = 1,
        marks = True
    )
    stand_behind_me = Move(
        name = "Stand Behind Me",
        character_id = 5,
        description = "Braum decreases the amount of damage he and an ally take by 30% for 2 turns",
        cooldown = 4,
        target = "ally",
        cost = 1,
        damage = 0,
        num_targets = 1,
        damage_reduction = 0.7,
        dr_duration = 2
    )
    unbreakable = Move(
        name = "Unbreakable",
        character_id = 5,
        description = "Braum raises his shield, blocking all spells for his allies for 1 turn. He reduces the damage of the first ability by 50% and all other attacks by 20%. Braum can only take damage once from each ability",
        cooldown = 4,
        target = "ally",
        cost = 1,
        damage = 0,
        num_targets = 3,
        damage_reduction = 0.8,
        dr_duration = 2
    )
    glacial_fissure = Move (
        name = "Glacial Fissure",
        character_id = 5,
        description = "Braum smashes the ground dealing 20 damage to all enemies and stunning them for 1 turn",
        cooldown = 4,
        target = "enemy",
        cost = 1,
        damage = 0,
        num_targets = 3,
        stun_duration = 1
    )
    glacial_fissure = Move (
        name = "Glacial Fissure",
        character_id = 5,
        description = "Braum smashes the ground dealing 20 damage to all enemies and stunning them for 1 turn",
        cooldown = 4,
        target = "enemy",
        cost = 1,
        damage = 0,
        num_targets = 3,
        stun_duration = 1
    )
    noxian_diplomacy = Move (
        name = "Noxian Diplomacy",
        character_id = 6,
        description = "Talon stabs the target dealing 30 damage. If the target is marked by 'Rake', the also bleed for 10 additional damage for 2 turns",
        cooldown = 4,
        target = "enemy",
        cost = 1,
        damage = 30,
        num_targets = 1,
        damage_over_time = 10,
        dot_duration = 2
    )
    rake = Move (
        name = "Rake",
        character_id = 6,
        description = "Talon throws out his blades at a target, marking them and dealing 20 damage. The next turn, the blades return dealing an additional 25 damage",
        cooldown = 4,
        target = "enemy",
        cost = 1,
        damage = 20,
        num_targets = 1,
        damage_over_time = 25,
        dot_duration = 1,
        marks = True
    )
    cutthroat = Move (
        name = "Cutthroat",
        character_id = 6,
        description = "Talon slashes the enemy's throat, dealing 15 damage and increasing damage Talon deals by 15% the following 2 turns",
        cooldown = 4,
        target = "enemy",
        cost = 1,
        damage = 15,
        num_targets = 1,
        damage_amp = 1.15,
        da_duration = 2,
        marks = True
    )
    shadow_assault = Move (
        name = "Shadow Assault",
        character_id = 6,
        description = "Talon jumps to a single enemy, dealing 25 damage to them. All other enemies take 15 damage. The following turn, all targets take the damage again",
        cooldown = 4,
        target = "enemy",
        cost = 1,
        damage = 15,
        num_targets = 3,
        damage_amp = 10,
        da_duration = 1,
        damage_over_time = 15,
        dot_duration = 1,
        marks = True
    )

    db.session.add(rangers_focus)
    db.session.add(volley)
    db.session.add(hawkshot)
    db.session.add(crystal_arrow)
    db.session.add(decisive_strike)
    db.session.add(courage)
    db.session.add(judgement)
    db.session.add(demacian_justice)
    db.session.add(overload)
    db.session.add(rune_prison)
    db.session.add(spell_flux)
    db.session.add(desperate_power)
    db.session.add(rupture)
    db.session.add(feral_scream)
    db.session.add(vorpal_spikes)
    db.session.add(feast)
    db.session.add(winters_bite)
    db.session.add(stand_behind_me)
    db.session.add(unbreakable)
    db.session.add(glacial_fissure)
    db.session.add(noxian_diplomacy)
    db.session.add(rake)
    db.session.add(cutthroat)
    db.session.add(shadow_assault)
    db.session.commit()
    

def undo_moves():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.moves RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM moves"))
        
    db.session.commit()
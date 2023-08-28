from app.models import db, Character, environment, SCHEMA
from sqlalchemy.sql import text

def seed_characters():
    ashe = Character(
        name = "Ashe",
        title = "The Frost Archer",
        region = "Freljord",
        about = "Iceborn warmother of the Avarosan tribe, Ashe commands the most populous horde in the north. Stoic, intelligent, and idealistic, yet uncomfortable with her role as leader, she taps into the ancestral magics of her lineage to wield a bow of True Ice. With her people's belief that she is the mythological hero Avarosa reincarnated, Ashe hopes to unify the Freljord once more by retaking their ancient, tribal lands.",
        classification = "marksman"
    )
    garen = Character(
        name = "Garen",
        title = "The Might of Demacia",
        region = "Demacia",
        about = "A proud and noble warrior, Garen fights as one of the Dauntless Vanguard. He is popular among his fellows, and respected well enough by his enemies—not least as a scion of the prestigious Crownguard family, entrusted with defending Demacia and its ideals. Clad in magic-resistant armor and bearing a mighty broadsword, Garen stands ready to confront mages and sorcerers on the field of battle, in a veritable whirlwind of righteous steel.",
        classification = "fighter"
    )
    ryze = Character(
        name = "Ryze",
        title = "The Rune Mage",
        region = "",
        about = "Widely considered one of the most adept sorcerers on Runeterra, Ryze is an ancient, hard-bitten archmage with an impossibly heavy burden to bear. Armed with immense arcane power and a boundless constitution, he tirelessly hunts for World Runes—fragments of the raw magic that once shaped the world from nothingness. He must retrieve these artifacts before they fall into the wrong hands, for Ryze understands the horrors they could unleash on Runeterra.",
        classification = "mage"
    )
    chogath = Character(
        name = "Cho'Gath",
        title = "The Terror of the Void",
        region = "The Void",
        about = "From the moment Cho'Gath first emerged into the harsh light of Runeterra's sun, the beast was driven by the most pure and insatiable hunger. A perfect expression of the Void's desire to consume all life, Cho'Gath's complex biology quickly converts matter into new bodily growth—increasing its muscle mass and density, or hardening its outer carapace like organic diamond. When growing larger does not suit the Void-spawn's needs, it vomits out the excess material as razor-sharp spines, leaving prey skewered and ready to feast upon later.",
        classification = "tank"
    )
    warwick = Character(
        name = "Warwick",
        title = "The Uncagfed Wrath of Zaun",
        region = "Zaun",
        about = "Warwick is a monster who hunts the gray alleys of Zaun. Transformed by agonizing experiments, his body is fused with an intricate system of chambers and pumps, machinery filling his veins with alchemical rage. Bursting out of the shadows, he preys upon those criminals who terrorize the city's depths. Warwick is drawn to blood, and driven mad by its scent. None who spill it can escape him.",
        classification = "fighter"
    )
    braum = Character(
        name = "Braum",
        title = "The Heart of the Freljord",
        region = "Freljord",
        about = "Blessed with massive biceps and an even bigger heart, Braum is a beloved hero of the Freljord. Every mead hall north of Frostheld toasts his legendary strength, said to have felled a forest of oaks in a single night, and punched an entire mountain into rubble. Bearing an enchanted vault door as his shield, Braum roams the frozen north sporting a mustachioed smile as big as his muscles—a true friend to all those in need.",
        classification = "support"
    )
    lux = Character(
        name = "Lux",
        title = "The Lady of Luminosity",
        region = "Demacia",
        about = "Blessed with massive biceps and an even bigger heart, Braum is a beloved hero of the Freljord. Every mead hall north of Frostheld toasts his legendary strength, said to have felled a forest of oaks in a single night, and punched an entire mountain into rubble. Bearing an enchanted vault door as his shield, Braum roams the frozen north sporting a mustachioed smile as big as his muscles—a true friend to all those in need.",
        classification = "mage"
    )
    sivir = Character(
        name = "Sivir",
        title = "The Battle Mistress",
        region = "Shurima",
        about = "Sivir is a renowned fortune hunter and mercenary captain who plies her trade in the deserts of Shurima. Armed with her legendary jeweled crossblade, she has fought and won countless battles for those who can afford her exorbitant price. Known for her fearless resolve and endless ambition, she prides herself on recovering buried treasures from the perilous tombs of Shurima—for a generous bounty. With ancient forces stirring the very bones of Shurima, Sivir finds herself torn between conflicting destinies.",
        classification = "marksman"
    )
    shen = Character(
        name = "Shen",
        title = "The Eye of Twilight",
        region = "Ionia",
        about = "Among the secretive, Ionian warriors known as the Kinkou, Shen serves as their leader, the Eye of Twilight. He longs to remain free from the confusion of emotion, prejudice, and ego, and walks the unseen path of dispassionate judgment between the spirit realm and the physical world. Tasked with enforcing the equilibrium between them, Shen wields blades of steel and arcane energy against any who would threaten it.",
        classification = "tank"
    )
    thresh = Character(
        name = "Thresh",
        title = "The Chain Warden",
        region = "The Shadow Isles",
        about = "Sadistic and cunning, Thresh is an ambitious and restless spirit of the Shadow Isles. Once the custodian of countless arcane secrets, he was undone by a power greater than life or death, and now sustains himself by tormenting and breaking others with slow, excruciating inventiveness. His victims suffer far beyond their brief mortal coil as Thresh wreaks agony upon their souls, imprisoning them in his unholy lantern to torture for all eternity.",
        classification = "support"
    )
    talon = Character(
        name = "Talon",
        title = "The Blade's Shadow",
        region = "Noxus",
        about = "Talon is the knife in the darkness, a merciless killer able to strike without warning and escape before any alarm is raised. He carved out a dangerous reputation on the brutal streets of Noxus, where he was forced to fight, kill, and steal to survive. Adopted by the notorious Du Couteau family, he now plies his deadly trade at the empire's command, assassinating enemy leaders, captains, and heroes… as well as any Noxian foolish enough to earn the scorn of their masters.",
        classification = "assassin"
    )
    qiyana = Character(
        name = "Qiyana",
        title = "Empress of the Elements",
        region = "Ixtal",
        about = "In the jungle city of Ixaocan, Qiyana plots her own ruthless path to the high seat of the Yun Tal. Last in line to succeed her parents, she faces those who stand in her way with brash confidence and unprecedented mastery over elemental magic. With the land itself obeying her every command, Qiyana sees herself as the greatest elementalist in the history of Ixaocan—and by that right, deserving of not only a city, but an empire.",
        classification = "assassin"
    )

    db.session.add(ashe)
    db.session.add(garen)
    db.session.add(ryze)
    db.session.add(chogath)
    db.session.add(lux)
    db.session.add(shen)
    db.session.add(talon)
    db.session.add(qiyana)
    db.session.add(warwick)
    db.session.add(braum)
    db.session.add(thresh)
    db.session.add(sivir)
    db.session.commit()

def undo_characters():
    if environment == "production":
        db.session.execute(f"TRUNCATE table {SCHEMA}.characters RESTART IDENTITY CASCADE;")
    else:
        db.session.execute(text("DELETE FROM users"))
        
    db.session.commit()
# List of spell schools
spell_schools = [
    'Combat', 'Detection', 'Health', 'Illusion', 'Manipulation', 'Drain', 'Enchantment', 'Geomancy'
]

# Dictionary of spell lists
spell_list = {
    'Combat': ['Ball Lightning', 'Clout', 'Flamethrower', 'Ice Spear', 'Lightning Bolt', 'Manaball', 'Manabolt',
               'Powerbolt'],
    'Detection': ['Analyze Device', 'Analyze Truth', 'Assensing', 'Clairaudience', 'Clairvoyance', 'Detect Enemies',
                  'Detect Individual', 'Detect Life'],
    'Health': ['Decrease Attribute', 'Heal', 'Increase Attribute', 'Increase Reflexes', 'Stabilize'],
    'Illusion': ['Chaotic World', 'Control Thoughts', 'Improved Invisibility', 'Mask', 'Physical Mask',
                 'Trid Phantasm'],
    'Manipulation': ['Analyze Device', 'Control Actions', 'Control Thoughts', 'Fling', 'Influence', 'Levitate',
                     'Mob Mind'],
    'Enchantment': ['Armor', 'Bind', 'Elemental Barrier', 'Magic Fingers', 'Trid Phantasm'],
    'Drain': ['Alleviate Addiction', 'Death Touch', 'Mind Probe', 'Psychic Surgery'],
    'Geomancy': ['Elemental Manipulation', 'Plant Control', 'Shape Earth', 'Water Spirit']
}

spells = {
    "Combat Spells": {
        "Direct Combat Spells": {
            "Acid Stream": {
                "Range": "LOS",
                "Type": "Physical",
                "Duration": "Instant",
                "DV": 5,
                "Damage": "Physical, Special"
            },
            "Toxic Wave": {
                "Range": "LOS (A)",
                "Type": "Physical",
                "Duration": "Instant",
                "DV": 6,
                "Damage": "Physical, Special",
                "Sustained Costs": "Magic is wearying and requires concentration, so if you are trying to keep a spell running while doing other things, there will be a price to pay due to the concentration and energy spent maintaining the spell. Whenever a spellcaster is sustaining a spell, they take a –2 dice pool penalty to any action test for each spell they sustain."
            }
        },
        "Indirect Combat Spells": {
            "Clout": {
                "Range": "LOS",
                "Type": "Stun",
                "Duration": "Instant",
                "DV": 3
            },
            "Blast": {
                "Range": "LOS (A)",
                "Type": "Stun",
                "Duration": "Instant",
                "DV": 4
            },
            "Flamestrike": {
                "Range": "LOS",
                "Type": "Physical",
                "Duration": "Instant",
                "DV": 5,
                "Damage": "Physical, Special"
            },
            "Fireball": {
                "Range": "LOS (A)",
                "Type": "Physical",
                "Duration": "Instant",
                "DV": 6,
                "Damage": "Physical, Special"
            },
            "Ice Spear": {
                "Range": "LOS",
                "Type": "Physical",
                "Duration": "Instant",
                "DV": 5,
                "Damage": "Physical, Special"
            },
            "Ice Storm": {
                "Range": "LOS (A)",
                "Type": "Physical",
                "Duration": "Instant",
                "DV": 6,
                "Damage": "Physical, Special"
            },
            "Lightning Bolt": {
                "Range": "LOS",
                "Type": "Physical",
                "Duration": "Instant",
                "DV": 5,
                "Damage": "Physical, Special"
            },
            "Lightning Ball": {
                "Range": "LOS (A)",
                "Type": "Physical",
                "Duration": "Instant",
                "DV": 6,
                "Damage": "Physical, Special"
            },
            "Manabolt": {
                "Range": "LOS",
                "Type": "Physical",
                "Duration": "Instant",
                "DV": 4
            },
            "Manaball": {
                "Range": "LOS (A)",
                "Type": "Physical",
                "Duration": "Instant",
                "DV": 5
            },
            "Powerbolt": {
                "Range": "LOS",
                "Type": "Physical",
                "Duration": "Instant",
                "DV": 4
            },
            "Powerball": {
                "Range": "LOS (A)",
                "Type": "Physical",
                "Duration": "Instant",
                "DV": 5
            },
            "Stunbolt": {
                "Range": "LOS",
                "Type": "Stun",
                "Duration": "Instant",
                "DV": 3
            },
            "Stunball": {
                "Range": "LOS (A)",
                "Type": "Stun",
                "Duration": "Instant",
                "DV": 4
            }
        }
    },
    "Detection Spells": {
        "Analyze Device": {
            "Range": "Touch",
            "Type": "Physical",
            "Duration": "Sustained",
            "DV": 2
        },
        "Analyze Magic": {
            "Range": "Touch",
            "Type": "Physical",
            "Duration": "Sustained",
            "DV": 3
        },
        "Analyze Truth": {
            "Range": "Touch",
            "Type": "Mental",
            "Duration": "Sustained",
            "DV": 3
        },
        "Clairaudience": {
            "Range": "Touch",
            "Type": "Mental",
            "Duration": "Sustained",
            "DV": 3
        },
        "Clairvoyance": {
            "Range": "Touch",
            "Type": "Mana",
            "Duration": "Sustained",
            "DV": 3,
            "Description": "The person on whom this is cast gains the ability to see distant sights. The subject may select and move the spot; the size of the spot is determined by normal area-of-effect rules and can be adjusted with Increase Area and can be moved with Shift Area. The subject can only see visuals in the target area while this spell is in effect (as opposed to sights near them), and any visual augmentations they have do not have any effect."
        },
        "Combat Sense": {
            "Range": "Touch",
            "Type": "Mana",
            "Duration": "Sustained",
            "DV": 3,
            "Description": "The subject gets a heightened awareness of possible dangers and the ability to react to them faster. Net hits on the Spellcasting test are added to the subject’s Defense Rating and dice pool for Surprise tests (see p. 108) as long as the spell is sustained."
        },
        "Detect Enemies": {
            "Range": "Touch",
            "Type": "Mana",
            "Duration": "Sustained",
            "DV": 3,
            "Description": "This spell lets the subject know if anyone within the sense’s range has hostile intentions toward them. It only works on people—not things, and it only detects people who have hostility specifically to the subject, not generalized anger at all metahumanity (if it did, everyone in the barrens would light up). Great for detecting ambushes!"
        },
        "Detect Life": {
            "Range": "Touch",
            "Type": "Mana",
            "Duration": "Sustained",
            "DV": 3,
            "Description": "Are there people hiding in that pile of rubble? Or in the forest? This spell will point them out for you. Despite its broad-sounding name, it does not detect every living thing, but rather focuses on sentient beings."
        },
        "Detect Magic": {
            "Range": "Touch",
            "Type": "Mana",
            "Duration": "Sustained",
            "DV": 4,
            "Description": "No one wants to sort through an entire landfill to find the magic ring sitting amid all the trash, but sometimes that’s the job. Which is why an enterprising mage developed this spell, which alerts the caster to any forms of active magic within the sense’s range. This includes foci, reagents, active spells, wards, alchemical preparations, spirits, and active rituals, but does not include Awakened people, critters, astral signatures, alchemical preparations that have been triggered or lost their potency, or the effects of permanent spells once they have become permanent."
        },
        "Mindlink": {
            "Range": "Touch",
            "Type": "Mana",
            "Duration": "Sustained",
            "DV": 3,
            "Description": "Commlinks and text messaging? So passé. Just throw your thoughts into someone else’s mind for the ultimate in rapid communication! As long as you get a hit on the Sorcery + Magic test, you have a link, and you can share mental communication in whatever form makes sense to you and subject of this spell. The caster and the subject must remain within range of each other for the link to continue functioning; if they move out of sense range and then come back into it, they can pick up the communication again, as long as the spell was continuously sustained."
        },
        "Mind Probe": {
            "Range": "Touch",
            "Type": "Physical",
            "Duration": "Sustained",
            "DV": 5,
            "Description": "The subject of this spell can dig into a target’s mind, seeing how many of their thoughts they can discern—while also attempting to sort what is true from the lies they tell themselves. Roll Sorcery + Magic vs. Willpower + Logic; net hits determine how much information the subject pulls out of the target’s head. The Mind Probe Results table shows the type of information this spell delivers."
        }
    },
    "Health Spells": {
        "Antidote": {
            "Range": "Touch",
            "Type": "P",
            "Duration": "P",
            "DV": 5,
            "Description": "Sends mana coursing through the body to find and purge toxins. Roll a Sorcery + Magic (toxin power) Extended test. Each net hit reduces the toxin power by one; once the power hits zero, any ongoing effects of the toxin are eliminated."
        },
        "Cleansing Heal": {
            "Range": "Touch",
            "Type": "P",
            "Duration": "P",
            "DV": 5,
            "Description": "Has the same healing effect as the Heal spell (roll Sorcery + Magic [5 – Essence], heal 1 box of Stun, Physical, or Overflow damage per net hit). In addition, this variant of the spell adds a cleansing element that eliminates the Corroded status on the targeted individual. Injuries can only be affected once by any healing spell."
        },
        "Cooling Heal": {
            "Range": "Touch",
            "Type": "P",
            "Duration": "P",
            "DV": 5,
            "Description": "Has the same healing effect as the Heal spell (roll Sorcery + Magic [5 – Essence], heal 1 box of Stun, Physical, or Overflow damage per net hit). In addition, this variant of the spell adds a cooling element that eliminates the Burning status on the targeted individual. Injuries can only be affected once by any healing spell."
        },
        "Decrease Attribute": {
            "Range": "Touch",
            "Type": "P",
            "Duration": "S",
            "DV": 3,
            "Description": "Weakens, slows, or stupefies the target, temporarily lowering one of their attributes. Roll a Sorcery + Magic vs. Willpower + targeted attribute. They can select how many net hits they actually apply to the target at a rate of 1 point of decrease per net hit; for each net hit applied beyond the first, the Drain Value of the spell increases by 1. The spell cannot affect Edge, Essence, Magic, or Resonance."
        },
        "Heal": {
            "Range": "Touch",
            "Type": "P",
            "Duration": "P",
            "DV": 3,
            "Description": "Repairs damage. Roll Sorcery + Magic with a threshold of (5 – Essence). Heal 1 box of Stun, Physical, or Overflow damage per net hit. Injuries can only be affected once by any Heal spell (including Cleansing Heal, Cooling Heal, and Warming Heal)."
        },
        "Increase Attribute": {
            "Range": "Touch",
            "Type": "P",
            "Duration": "S",
            "DV": 3,
            "Description": "Strengthens, speeds, or enlightens the target, temporarily raising one of their attributes. Roll a Sorcery + Magic (5 – Essence) test. They can select how many net hits they actually apply to the target to increase the selected attribute, at a rate of 1 point of increase per net hit (maximum bonus +4); for each net hit applied beyond the first, the Drain Value of the spell increases by 1. The spell cannot affect Edge, Essence, Magic, or Resonance."
        },
        "Increase Reflexes": {
            "Range": "Touch",
            "Type": "P",
            "Duration": "S",
            "DV": 5,
            "Description": "Increases reaction time and speed, making the target better able to anticipate and respond to others. Roll a Sorcery + Magic (5 – Essence) test. They can select how many net hits they actually apply to the target to increase both their Reaction score and the number of Initiative Dice, at a rate of 1 point of increase and 1 Initiative Die per net hit; for each net hit applied beyond the first, the Drain Value of the spell increases by 1."
        },
        "Resist Pain": {
            "Range": "Touch",
            "Type": "M",
            "Duration": "S",
            "DV": 3,
            "Description": "Allows the target to ignore the effects of damage, reducing dice-pool modifiers from damage by 1 per net hit. Roll Sorcery + Magic (5 – Essence)."
        },
        "Stabilize": {
            "Range": "Touch",
            "Type": "M",
            "Duration": "P",
            "DV": 3,
            "Description": "Used when someone is in Overflow damage and is sustaining an ongoing damaging effect or status. Roll Sorcery + Magic, with a threshold of the number of Overflow boxes of damage the target has. Meeting the threshold means the target is stabilized, and all Overflow damage is removed. The net hits can only affect Overflow damage and cannot heal regular damage."
        },
        "Warming Heal": {
            "Range": "Touch",
            "Type": "P",
            "Duration": "P",
            "DV": 5,
            "Description": "Has the same healing effect as the Heal spell (roll Sorcery + Magic [5 – Essence], heal 1 box of Stun, Physical, or Overflow damage per net hit). In addition, this variant of the spell adds a warming element that eliminates the Chilled status on the targeted individual. Injuries can only be affected once by any healing spell."
        }
    },
    "Illusion Spells": {
        "Agony": {
            "Category": "Illusion",
            "Sense": "Single-Sense",
            "Range": "LOS",
            "Type": "Mana",
            "Duration": "S",
            "DV": 3,
            "Description": "Brings pain but not actual damage. Each net hit acts like an additional box of damage in both the Physical and Stun Condition Monitors for the purposes of determining penalties due to injuries. Target stays conscious but unable to act if one or both Condition Monitors are filled. No ongoing effect once the spell is dropped."
        },
        "Confusion": {
            "Category": "Illusion",
            "Sense": "Multi-Sense",
            "Range": "LOS",
            "Type": "Mana",
            "Duration": "S",
            "DV": 3,
            "Description": "Hits the target with a swirl of images and emotions, leaving them disoriented and confused. Target gains the Confused (#) status, with the number equaling the net hits on the test. Experiences a dice pool penalty equal to that number on all tests besides Damage Resistance tests."
        },
        "Chaos": {
            "Category": "Illusion",
            "Sense": "Multi-Sense",
            "Range": "LOS",
            "Type": "Physical",
            "Duration": "S",
            "DV": 4,
            "Description": "Similar to Confusion but also affects cameras, microphones, and other technology. Can be cast as an area spell with Increase Area effect."
        },
        "Hush": {
            "Category": "Illusion",
            "Sense": "Single-Sense",
            "Range": "Touch",
            "Type": "Mana",
            "Duration": "S",
            "DV": 3,
            "Description": "Silence descends on the target, making them unable to make noise. Gives targets the Silent (#) status, with the number equaling the net hits on the Sorcery + Magic test. Acts as a threshold for any attempts to hear the character."
        },
        "Silence": {
            "Category": "Illusion",
            "Sense": "Single-Sense",
            "Range": "Touch",
            "Type": "Physical",
            "Duration": "S",
            "DV": 4,
            "Description": "Similar to Hush but also affects microphones and other technology. Gives the Silent (Improved) (#) status."
        },
        "Invisibility": {
            "Category": "Illusion",
            "Sense": "Single-Sense",
            "Range": "Touch",
            "Type": "Mana",
            "Duration": "S",
            "DV": 3,
            "Description": "Makes the target transparent, allowing them to move unnoticed. Gives the Invisible (#) status, where the number after the status becomes the threshold on any tests to see the character."
        },
        "Improved Invisibility": {
            "Category": "Illusion",
            "Sense": "Single-Sense",
            "Range": "Touch",
            "Type": "Physical",
            "Duration": "S",
            "DV": 4,
            "Description": "Similar to Invisibility but also works against cameras and other technology. Gives the Improved Invisibility (#) status."
        },
        "Mask": {
            "Category": "Illusion",
            "Sense": "Multi-Sense",
            "Range": "Touch",
            "Type": "Mana",
            "Duration": "S",
            "DV": 3,
            "Description": "Changes the appearance, sound, and scent of the target. Threshold for seeing through the illusion is determined by the number of hits on the Sorcery + Magic test."
        },
        "Physical Mask": {
            "Category": "Illusion",
            "Sense": "Multi-Sense",
            "Range": "Touch",
            "Type": "Physical",
            "Duration": "S",
            "DV": 4,
            "Description": "Similar to Mask but also affects cameras and other technology."
        },
        "Phantasm": {
            "Category": "Illusion",
            "Sense": "Multi-Sense",
            "Range": "LOS (A)",
            "Type": "Mana",
            "Duration": "S",
            "DV": 3,
            "Description": "Projects a particular image into the area of effect along with accompanying sounds and smells. Threshold of any tests to see through the illusion is determined by the net hits on the Sorcery + Magic test."
        },
        "Trid Phantasm": {
            "Category": "Illusion",
            "Sense": "Multi-Sense",
            "Range": "LOS (A)",
            "Type": "Physical",
            "Duration": "S",
            "DV": 4,
            "Description": "Similar to Phantasm but also affects cameras and other technology."
        },
        "Sensor Sneak": {
            "Category": "Illusion",
            "Sense": "Multi-Sense",
            "Range": "Touch",
            "Type": "Physical",
            "Duration": "S",
            "DV": 2,
            "Description": "Gives the target a version of the Invisible (Improved) (#) status, but has no effect on living beings, only technology-based sensors."
        }
    },
    "Manipulation Spells": {
        "Animate Metal": {
            "Range": "LOS",
            "Type": "P",
            "Duration": "L",
            "DV": 6,
            "Description": "A chunk of material of the affected type comes to life, moving as commanded by the spellcaster. Roll Sorcery + Magic vs. Object Resistance of the item/material being animated. The material can move according to its form, but generally it should not be faster than 5 meters per combat round unless it is a wheeled vehicle or something else with innate speed."
        },
        "Animate Plastic": {
            "Range": "LOS",
            "Type": "P",
            "Duration": "L",
            "DV": 3,
            "Description": "A chunk of material of the affected type comes to life, moving as commanded by the spellcaster. Roll Sorcery + Magic vs. Object Resistance of the item/material being animated. The material can move according to its form, but generally it should not be faster than 5 meters per combat round unless it is a wheeled vehicle or something else with innate speed."
        },
        "Animate Stone": {
            "Range": "LOS",
            "Type": "P",
            "Duration": "L",
            "DV": 5,
            "Description": "A chunk of material of the affected type comes to life, moving as commanded by the spellcaster. Roll Sorcery + Magic vs. Object Resistance of the item/material being animated. The material can move according to its form, but generally it should not be faster than 5 meters per combat round unless it is a wheeled vehicle or something else with innate speed."
        },
        "Animate Wood": {
            "Range": "LOS",
            "Type": "P",
            "Duration": "L",
            "DV": 4,
            "Description": "A chunk of material of the affected type comes to life, moving as commanded by the spellcaster. Roll Sorcery + Magic vs. Object Resistance of the item/material being animated. The material can move according to its form, but generally it should not be faster than 5 meters per combat round unless it is a wheeled vehicle or something else with innate speed."
        },
        "Armor": {
            "Range": "Touch",
            "Type": "P",
            "Duration": "S",
            "DV": 4,
            "Description": "Your magic fills the body of the target, hardening it and making it better able to absorb damage. Roll Sorcery + Magic and add net hits to the target’s Defense Rating."
        },
        "Control Actions": {
            "Range": "LOS",
            "Type": "M",
            "Duration": "L",
            "DV": 4,
            "Description": "The spellcaster acts as master puppeteer, taking control of another person and making them dance to their tune. Roll Sorcery + Magic vs. Willpower + Logic; net hits give the maximum duration of the spell in minutes."
        },
        "Control Thoughts": {
            "Range": "LOS",
            "Type": "M",
            "Duration": "L",
            "DV": 4,
            "Description": "Similar to Control Actions but more insidious, this puts the spellcaster inside the head of the target, making them think what the spellcaster wants them to. Roll Sorcery + Magic vs. Willpower + Logic; net hits give the maximum duration of the spell in minutes."
        },
        "Darkness": {
            "Range": "LOS(A)",
            "Type": "P",
            "Duration": "S",
            "DV": 3,
            "Description": "These spells are two sides of the same coin, changing the light level of your environment to suit you. For each net hit, you can raise (using Light) or lower (using Darkness) the light level of the surrounding area, which may help gain when it comes to determining Edge based on Environment and Visibility."
        },
        "Light": {
            "Range": "LOS(A)",
            "Type": "P",
            "Duration": "S",
            "DV": 3,
            "Description": "These spells are two sides of the same coin, changing the light level of your environment to suit you. For each net hit, you can raise (using Light) or lower (using Darkness) the light level of the surrounding area, which may help gain when it comes to determining Edge based on Environment and Visibility."
        },
        "Elemental Armor": {
            "Range": "Touch",
            "Type": "M",
            "Duration": "S",
            "DV": 5,
            "Description": "This works the same as the Armor spell, though it provides an added bonus. When casting the spell, you choose one element to protect the target from."
        },
        "Fling": {
            "Range": "LOS",
            "Type": "P",
            "Duration": "I",
            "DV": 5,
            "Description": "If you ever thought, “If I had magic powers, I definitely would catapult objects into the sky, only without a catapult,” then you’re our sort of person, and this spell is for you."
        },
        "Focus Burst": {
            "Range": "Touch",
            "Type": "M",
            "Duration": "L",
            "DV": 7,
            "Description": "Foci can be powerful aids for magicians, but who hasn’t found themselves wanting to eke out a little more power from them every now and then?"
        },
        "Levitate": {
            "Range": "LOS",
            "Type": "P",
            "Duration": "S",
            "DV": 6,
            "Description": "It may not be exactly the same as flight, but hey, it’s defying gravity, and it’s a blast."
        },
        "Mana Barrier": {
            "Range": "LOS(A)",
            "Type": "M",
            "Duration": "S",
            "DV": 5,
            "Description": "Want a spirit-free room? Want a way to enforce your bar’s “no foci” policy? Then a mana barrier is the way to go."
        },
        "Mystic Armor": {
            "Range": "Touch",
            "Type": "P",
            "Duration": "S",
            "DV": 3,
            "Description": "Your magic fills the astral form of the target, hardening it and making it better able to absorb damage."
        },
        "Overclock": {
            "Range": "LOS",
            "Type": "P",
            "Duration": "S",
            "DV": 4,
            "Description": "Magic does not always get along with tech, but sometimes they find a way to combine forces. With this spell, a mage can briefly amp up an electronic device’s power, making it run better and faster."
        },
        "Physical Barrier": {
            "Range": "LOS (A)",
            "Type": "P",
            "Duration": "S",
            "DV": 6,
            "Description": "Builds a wall where you want it to be, with a Structure rating equal to (Magic + hits on a Sorcery + Magic test). The base spell casts a barrier that is two meters by two meters, two centimeters thick. The Increase Area effect can be applied to add up to two meters in length and width (but not depth) for each time the effect is chosen."
        },
        "Shape Metal": {
            "Range": "LOS",
            "Type": "P",
            "Duration": "S",
            "DV": 5,
            "Description": "Allows you to make metal malleable, shaping it as long as the spell is sustained. Roll Sorcery + Magic vs. Object Resistance; the amount of material you can shape is determined by net hits on that test."
        },
        "Shape Plastic": {
            "Range": "LOS",
            "Type": "P",
            "Duration": "S",
            "DV": 2,
            "Description": "Allows you to make plastic malleable, shaping it as long as the spell is sustained. Roll Sorcery + Magic vs. Object Resistance; the amount of material you can shape is determined by net hits on that test."
        },
        "Shape Stone": {
            "Range": "LOS",
            "Type": "P",
            "Duration": "S",
            "DV": 4,
            "Description": "Allows you to make stone malleable, shaping it as long as the spell is sustained. Roll Sorcery + Magic vs. Object Resistance; the amount of material you can shape is determined by net hits on that test."
        },
        "Shape Wood": {
            "Range": "LOS",
            "Type": "P",
            "Duration": "S",
            "DV": 3,
            "Description": "Allows you to make wood malleable, shaping it as long as the spell is sustained. Roll Sorcery + Magic vs. Object Resistance; the amount of material you can shape is determined by net hits on that test."
        },
        "Strengthen Wall": {
            "Range": "LOS (A)",
            "Type": "P",
            "Duration": "S",
            "DV": 4,
            "Description": "Makes an existing wall stronger. Roll Sorcery + Magic vs. Object Resistance for the wall you are trying to affect; net hits increase the Structure rating by 1 per net hit."
        },
        "Thunder": {
            "Range": "LOS (A)",
            "Type": "P",
            "Duration": "S",
            "DV": 3,
            "Description": "Shapes sound waves into a noise of your choice, creating a distraction. The basic area affected by the spell is a two-meter-radius sphere; this can be expanded with the Increase Area effect."
        },
        "Vehicle Armor": {
            "Range": "Touch",
            "Type": "M",
            "Duration": "S",
            "DV": 6,
            "Description": "Increases the vehicle’s effective Armor by 1 per net hit. Roll Sorcery + Magic vs. Object Resistance of the vehicle."
        }
    }
}
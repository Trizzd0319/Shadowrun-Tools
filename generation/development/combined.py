combined_dict = {
    "Attributes": {
        "Physical": [
            "Agility",
            "Strength",
            "Body",
            "Reaction"
        ],
        "Mental": [
            "Willpower",
            "Intuition",
            "Charisma",
            "Logic"
        ],
        "Initiative": [
            "Initiative, Astral",
            "Initiative, Matrix",
            "Initiative, Physical"
        ],
        "Other": [
            "Magic",
            "Essence",
            "Edge",
            "Resonance"
        ]
    },
    "Skills": {
        "Astral": {
            "Specializations": [
                "Astral Combat",
                "Astral Signatures",
                "Emotional States",
                "Spirit Types"
            ],
            "Untrained": false,
            "Linked Attributes": {
                "Primary": "Intuition",
                "Secondary": "Willpower"
            },
            "Description": "Used by magicians, adepts, and mystic adepts with Astral Perception adept power for assensing astral auras and combat."
        },
        "Athletics": {
            "Specializations": [
                "Climbing",
                "Flying",
                "Gymnastics",
                "Sprinting",
                "Swimming",
                "Throwing"
            ],
            "Untrained": true,
            "Linked Attributes": {
                "Primary": "Agility",
                "Secondary": "Strength"
            },
            "Description": "Covers physical grace and prowess, including sprinting, full defense actions, and thrown weapon attacks."
        },
        "Biotech": {
            "Specializations": [
                "Biotechnology",
                "Cybertechnology",
                "First Aid",
                "Medicine"
            ],
            "Untrained": false,
            "Linked Attributes": {
                "Primary": "Agility",
                "Secondary": "Strength"
            },
            "Description": "Covers medical and technological applications, including first aid and cybertechnology."
        },
        "Close Combat": {
            "Specializations": [
                "Blades",
                "Clubs",
                "Unarmed Combat"
            ],
            "Untrained": false,
            "Linked Attributes": {
                "Primary": "Agility"
            },
            "Description": "Used for close-quarters combat with blades, clubs, or unarmed strikes."
        },
        "Con": {
            "Specializations": [
                "Acting",
                "Disguise",
                "Impersonation",
                "Performance"
            ],
            "Untrained": true,
            "Linked Attributes": {
                "Primary": "Charisma"
            },
            "Description": "Involves persuasion through deception or acting, convincing others of false identities or intentions."
        },
        "Conjuring": {
            "Specializations": [
                "Banishing",
                "Binding",
                "Summoning"
            ],
            "Untrained": false,
            "Linked Attributes": {
                "Primary": "Magic"
            },
            "Description": "Used for summoning, binding, and banishing spirits."
        },
        "Cracking": {
            "Specializations": [
                "Cybercombat",
                "Electronic Warfare",
                "Hacking"
            ],
            "Untrained": false,
            "Linked Attributes": {
                "Primary": "Logic"
            },
            "Description": "Involves illegal actions in the Matrix, such as hacking and cyber warfare."
        },
        "Electronics": {
            "Specializations": [
                "Computer",
                "Hardware",
                "Software"
            ],
            "Untrained": true,
            "Linked Attributes": {
                "Primary": "Logic",
                "Secondary": "Intuition"
            },
            "Description": "Covers legal Matrix activities like software manipulation and hardware maintenance."
        },
        "Enchanting": {
            "Specializations": [
                "Alchemy",
                "Artificing",
                "Disenchanting"
            ],
            "Untrained": false,
            "Linked Attributes": {
                "Primary": "Magic"
            },
            "Description": "Involves crafting magical items like foci and imbuing objects with magical properties."
        },
        "Engineering": {
            "Specializations": [
                "Aeronautics Mechanic",
                "Automotive Mechanic",
                "Demolitions",
                "Gunnery",
                "Industrial Mechanic",
                "Lockpicking",
                "Nautical Mechanic"
            ],
            "Untrained": true,
            "Linked Attributes": {
                "Primary": "Logic",
                "Secondary": "Intuition, Agility"
            },
            "Description": "Encompasses building, repairing, and modifying mechanical systems."
        },
        "Exotic Weapons": {
            "Specializations": [],
            "Untrained": false,
            "Linked Attributes": {
                "Primary": "Agility"
            },
            "Description": "Covers specialized weaponry requiring specific training."
        },
        "Firearms": {
            "Specializations": [
                "Automatics",
                "Longarms",
                "Pistols",
                "Rifles",
                "Shotguns"
            ],
            "Untrained": true,
            "Linked Attributes": {
                "Primary": "Agility"
            },
            "Description": "Involves proficiency with various ranged weapons."
        },
        "Influence": {
            "Specializations": [
                "Etiquette",
                "Instruction",
                "Intimidation",
                "Leadership",
                "Negotiation"
            ],
            "Untrained": true,
            "Linked Attributes": {
                "Primary": "Charisma",
                "Secondary": "Logic"
            },
            "Description": "Involves shaping opinions through persuasion or intimidation."
        },
        "Outdoors": {
            "Specializations": [
                "Navigation",
                "Survival",
                "Tracking",
                "by Environment (Woods, Desert, Urban Areas, etc.)"
            ],
            "Untrained": true,
            "Linked Attributes": {
                "Primary": "Intuition"
            },
            "Description": "Used for navigating natural environments and survival techniques."
        },
        "Perception": {
            "Specializations": [
                "Visual",
                "Aural",
                "Tactile",
                "by Environment (Woods, Desert, Urban, etc.)"
            ],
            "Untrained": true,
            "Linked Attributes": {
                "Primary": "Intuition",
                "Secondary": "Logic"
            },
            "Description": "Involves observing and noticing details in the environment."
        },
        "Piloting": {
            "Specializations": [
                "Ground Craft",
                "Aircraft",
                "Watercraft"
            ],
            "Untrained": true,
            "Linked Attributes": {
                "Primary": "Reaction"
            },
            "Description": "Used for operating vehicles, including ground, air, and watercraft."
        },
        "Sorcery": {
            "Specializations": [
                "Counterspelling",
                "Ritual Spellcasting",
                "Spellcasting"
            ],
            "Untrained": false,
            "Linked Attributes": {
                "Primary": "Magic"
            },
            "Description": "Involves casting spells and manipulating magical energies."
        },
        "Stealth": {
            "Specializations": [
                "Disguise",
                "Palming",
                "Sneaking"
            ],
            "Untrained": true,
            "Linked Attributes": {
                "Primary": "Agility"
            },
            "Description": "Covers activities characters perform that they do not want others to notice."
        },
        "Tasking": {
            "Specializations": [
                "Compiling",
                "Decompiling",
                "Registering"
            ],
            "Untrained": false,
            "Linked Attributes": {
                "Primary": "Resonance"
            },
            "Description": "Skill technomancers use for various technomancer activities."
        }
    }
}
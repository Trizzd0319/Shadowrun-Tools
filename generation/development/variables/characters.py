import json

metatype = {
    'Human': {
        'Priority': 'E',
        'Body': '-',
        'Strength': '-',
        'Quickness': '-',
        'Intelligence': '-',
        'Willpower': '-',
        'Charisma': '-',
        'Running Multiplier': '×3',
        'Other': '1:10 Karma Pool accumulation',
        'Origin': 'anywhere',
        'Average Height_cm': 170,
        'Average Mass_kg': 70,
        'Height Range_low_cm': 130,
        'Height Range_high_cm': 221,
        'Mass Range_low_kg': 31,
        'Mass Range_high_kg': 153,
        'Average Height_ft': "5'7\"",
        'Average Mass_lb': 154,
        'Height Range_low_ft': "4'3\"",
        'Height Range_high_ft': "7'3\"",
        'Mass Range_low_lb': 68,
        'Mass Range_high_lb': 337,
        'Life Expectancy': '55 years',
        'Percentage Population': '81%'
    },
    'Dwarf': {
        'Priority': 'D',
        'Body': '+1',
        'Strength': '+2',
        'Quickness': '-',
        'Intelligence': '-',
        'Willpower': '+1',
        'Charisma': '-',
        'Running Multiplier': '×2',
        'Other': 'Thermographic vision, Resistance (+2 Body) to any disease or toxin',
        'Origin': 'anywhere',
        'Average Height_cm': 120,
        'Average Mass_kg': 44,
        'Height Range_low_cm': 95,
        'Height Range_high_cm': 151,
        'Mass Range_low_kg': 22,
        'Mass Range_high_kg': 89,
        'Average Height_ft': "3'11\"",
        'Average Mass_lb': 97,
        'Height Range_low_ft': "3'1\"",
        'Height Range_high_ft': "4'11\"",
        'Mass Range_low_lb': 49,
        'Mass Range_high_lb': 196,
        'Life Expectancy': 'estimated at 120–150 years',
        'Percentage Population': '3%'
    },
    'Elf': {
        'Priority': 'C',
        'Body': '-',
        'Strength': '-',
        'Quickness': '+1',
        'Intelligence': '-',
        'Willpower': '-',
        'Charisma': '+2',
        'Running Multiplier': '×3',
        'Other': 'Low-Light Vision',
        'Origin': 'anywhere',
        'Average Height_cm': 190,
        'Average Mass_kg': 78,
        'Height Range_low_cm': 146,
        'Height Range_high_cm': 247,
        'Mass Range_low_kg': 35,
        'Mass Range_high_kg': 171,
        'Average Height_ft': "6'3\"",
        'Average Mass_lb': 172,
        'Height Range_low_ft': "4'9\"",
        'Height Range_high_ft': "8'1\"",
        'Mass Range_low_lb': 77,
        'Mass Range_high_lb': 377,
        'Life Expectancy': 'estimated at 300–500 years',
        'Percentage Population': '5%'
    },
    'Ork': {
        'Priority': 'D',
        'Body': '+3',
        'Strength': '+2',
        'Quickness': '-',
        'Intelligence': '-1',
        'Willpower': '-',
        'Charisma': '-1',
        'Running Multiplier': '×3',
        'Other': 'Low-Light Vision',
        'Origin': 'anywhere',
        'Average Height_cm': 190,
        'Average Mass_kg': 125,
        'Height Range_low_cm': 147,
        'Height Range_high_cm': 244,
        'Mass Range_low_kg': 58,
        'Mass Range_high_kg': 266,
        'Average Height_ft': "6'3\"",
        'Average Mass_lb': 276,
        'Height Range_low_ft': "4'10\"",
        'Height Range_high_ft': "8'0\"",
        'Mass Range_low_lb': 128,
        'Mass Range_high_lb': 587,
        'Life Expectancy': '38 years',
        'Percentage Population': '9%'
    },
    'Troll': {
        'Priority': 'C',
        'Body': '+5',
        'Strength': '+4',
        'Quickness': '-1',
        'Intelligence': '-2',
        'Willpower': '-',
        'Charisma': '-2',
        'Running Multiplier': '×3',
        'Other': 'Thermographic Vision, +1 Reach for Armed/Unarmed Combat, Dermal Armor (+1 Body)',
        'Origin': 'anywhere',
        'Average Height_cm': 280,
        'Average Mass_kg': 491,
        'Height Range_low_cm': 219,
        'Height Range_high_cm': 357,
        'Mass Range_low_kg': 236,
        'Mass Range_high_kg': 1017,
        'Average Height_ft': "9'2\"",
        'Average Mass_lb': 1082,
        'Height Range_low_ft': "7'2\"",
        'Height Range_high_ft': "11'8\"",
        'Mass Range_low_lb': 520,
        'Mass Range_high_lb': 2242,
        'Life Expectancy': '50 years',
        'Percentage Population': '2%'
    }
}

priority_data = {
    'A': {'Races': {'Dwarf': 13, 'Ork': 13, 'Troll': 13}, 'Attributes': 24, 'Skills': 32,
          'Magic/Resonance': {'Full': 4, 'Aspected': 5, 'Mystic Adept': 4, 'Adept': 4, 'Technomancer': 4},
          'Resources': 450000},
    'B': {'Races': {'Dwarf': 11, 'Elf': 11, 'Ork': 11, 'Troll': 11}, 'Attributes': 16, 'Skills': 24,
          'Magic/Resonance': {'Full': 3, 'Aspected': 4, 'Mystic Adept': 3, 'Adept': 3, 'Technomancer': 3},
          'Resources': 275000},
    'C': {'Races': {'Dwarf': 9, 'Elf': 9, 'Human': 9, 'Ork': 9, 'Troll': 9}, 'Attributes': 12, 'Skills': 20,
          'Magic/Resonance': {'Full': 2, 'Aspected': 3, 'Mystic Adept': 2, 'Adept': 2, 'Technomancer': 2},
          'Resources': 150000},
    'D': {'Races': {'Dwarf': 4, 'Elf': 4, 'Human': 4, 'Ork': 4, 'Troll': 4}, 'Attributes': 8, 'Skills': 16,
          'Magic/Resonance': {'Full': 1, 'Aspected': 2, 'Mystic Adept': 1, 'Adept': 1, 'Technomancer': 1},
          'Resources': 50000},
    'E': {'Races': {'Dwarf': 1, 'Elf': 1, 'Human': 1, 'Ork': 1, 'Troll': 1}, 'Attributes': 2, 'Skills': 10,
          'Magic/Resonance': 'Mundane', 'Resources': 8000}
}

skills = {
    "Astral": {
        "Specializations": ["Astral Combat", "Astral Signatures", "Emotional States", "Spirit Types"],
        "Untrained": "False",
        "Linked Attributes": {
            "Primary": "Intuition",
            "Secondary": "Willpower"
        },
        "Description": "Used by magicians, adepts, and mystic adepts with Astral Perception adept power for assensing astral auras and combat."
    },
    "Athletics": {
        "Specializations": ["Climbing", "Flying", "Gymnastics", "Sprinting", "Swimming", "Throwing"],
        "Untrained": "True",
        "Linked Attributes": {
            "Primary": "Agility",
            "Secondary": "Strength"
        },
        "Description": "Covers physical grace and prowess, including sprinting, full defense actions, and thrown weapon attacks."
    },
    "Biotech": {
        "Specializations": ["Biotechnology", "Cybertechnology", "First Aid", "Medicine"],
        "Untrained": "False",
        "Linked Attributes": {
            "Primary": "Agility",
            "Secondary": "Strength"
        },
        "Description": "Covers medical and technological applications, including first aid and cybertechnology."
    },
    "Close Combat": {
        "Specializations": ["Blades", "Clubs", "Unarmed Combat"],
        "Untrained": "False",
        "Linked Attributes": {
            "Primary": "Agility"
        },
        "Description": "Used for close-quarters combat with blades, clubs, or unarmed strikes."
    },
    "Con": {
        "Specializations": ["Acting", "Disguise", "Impersonation", "Performance"],
        "Untrained": "True",
        "Linked Attributes": {
            "Primary": "Charisma"
        },
        "Description": "Involves persuasion through deception or acting, convincing others of false identities or intentions."
    },
    "Conjuring": {
        "Specializations": ["Banishing", "Binding", "Summoning"],
        "Untrained": "False",
        "Linked Attributes": {
            "Primary": "Magic"
        },
        "Description": "Used for summoning, binding, and banishing spirits."
    },
    "Cracking": {
        "Specializations": ["Cybercombat", "Electronic Warfare", "Hacking"],
        "Untrained": "False",
        "Linked Attributes": {
            "Primary": "Logic"
        },
        "Description": "Involves illegal actions in the Matrix, such as hacking and cyber warfare."
    },
    "Electronics": {
        "Specializations": ["Computer", "Hardware", "Software"],
        "Untrained": "True",
        "Linked Attributes": {
            "Primary": "Logic",
            "Secondary": "Intuition"
        },
        "Description": "Covers legal Matrix activities like software manipulation and hardware maintenance."
    },
    "Enchanting": {
        "Specializations": ["Alchemy", "Artificing", "Disenchanting"],
        "Untrained": "False",
        "Linked Attributes": {
            "Primary": "Magic"
        },
        "Description": "Involves crafting magical items like foci and imbuing objects with magical properties."
    },
    "Engineering": {
        "Specializations": ["Aeronautics Mechanic", "Automotive Mechanic", "Demolitions",
                            "Gunnery", "Industrial Mechanic", "Lockpicking", "Nautical Mechanic"],
        "Untrained": "True",
        "Linked Attributes": {
            "Primary": "Logic",
            "Secondary": "Intuition, Agility"
        },
        "Description": "Encompasses building, repairing, and modifying mechanical systems."
    },
    "Exotic Weapons": {
        "Specializations": [],
        "Untrained": "False",
        "Linked Attributes": {
            "Primary": "Agility"
        },
        "Description": "Covers specialized weaponry requiring specific training."
    },
    "Firearms": {
        "Specializations": ["Automatics", "Longarms", "Pistols", "Rifles", "Shotguns"],
        "Untrained": "True",
        "Linked Attributes": {
            "Primary": "Agility"
        },
        "Description": "Involves proficiency with various ranged weapons."
    },
    "Influence": {
        "Specializations": ["Etiquette", "Instruction", "Intimidation", "Leadership", "Negotiation"],
        "Untrained": "True",
        "Linked Attributes": {
            "Primary": "Charisma",
            "Secondary": "Logic"
        },
        "Description": "Involves shaping opinions through persuasion or intimidation."
    },
    "Outdoors": {
        "Specializations": ["Navigation", "Survival", "Tracking", "by Environment (Woods, Desert, Urban Areas, etc.)"],
        "Untrained": "True",
        "Linked Attributes": {
            "Primary": "Intuition"
        },
        "Description": "Used for navigating natural environments and survival techniques."
    },
    "Perception": {
        "Specializations": ["Visual", "Aural", "Tactile", "by Environment (Woods, Desert, Urban, etc.)"],
        "Untrained": "True",
        "Linked Attributes": {
            "Primary": "Intuition",
            "Secondary": "Logic"
        },
        "Description": "Involves observing and noticing details in the environment."
    },
    "Piloting": {
        "Specializations": ["Ground Craft", "Aircraft", "Watercraft"],
        "Untrained": "True",
        "Linked Attributes": {
            "Primary": "Reaction"
        },
        "Description": "Used for operating vehicles, including ground, air, and watercraft."
    },
    "Sorcery": {
        "Specializations": ["Counterspelling", "Ritual Spellcasting", "Spellcasting"],
        "Untrained": "False",
        "Linked Attributes": {
            "Primary": "Magic"
        },
        "Description": "Involves casting spells and manipulating magical energies."
    },
    "Stealth": {
        "Specializations": ["Disguise", "Palming", "Sneaking"],
        "Untrained": "True",
        "Linked Attributes": {
            "Primary": "Agility"
        },
        "Description": "Covers activities characters perform that they do not want others to notice."
    },
    "Tasking": {
        "Specializations": ["Compiling", "Decompiling", "Registering"],
        "Untrained": "False",
        "Linked Attributes": {
            "Primary": "Resonance"
        },
        "Description": "Skill technomancers use for various technomancer activities."
    }
}

combined_att_skills = {
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
            "Untrained": "False",
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
            "Untrained": "True",
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
            "Untrained": "False",
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
            "Untrained": "False",
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
            "Untrained": "True",
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
            "Untrained": "False",
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
            "Untrained": "False",
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
            "Untrained": "True",
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
            "Untrained": "False",
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
            "Untrained": "True",
            "Linked Attributes": {
                "Primary": "Logic",
                "Secondary": "Intuition, Agility"
            },
            "Description": "Encompasses building, repairing, and modifying mechanical systems."
        },
        "Exotic Weapons": {
            "Specializations": [],
            "Untrained": "False",
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
            "Untrained": "True",
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
            "Untrained": "True",
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
            "Untrained": "True",
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
            "Untrained": "True",
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
            "Untrained": "True",
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
            "Untrained": "False",
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
            "Untrained": "True",
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
            "Untrained": "False",
            "Linked Attributes": {
                "Primary": "Resonance"
            },
            "Description": "Skill technomancers use for various technomancer activities."
        }
    }
}

lifestyles = {
    "Street": {
        "Cost": "Free",
        "Description": "You have no place to rest your head. Whether you’re crashing on someone’s couch or sleeping out under the stars, you grab rest where you can and food where it’s available. You have no place to store stuff—if you don’t carry it with you, it likely will be stolen by the time you come back to pick it up. It’s a tough way to live, but it’s cheap! If you haven’t paid for a lifestyle in the current month, then you’re living on the street."
    },
    "Squatter": {
        "Cost": "500 nuyen a month",
        "Description": "The Sixth World has been through a lot—disease, disaster, warfare, and economic boom and bust. Many of the people who departed this world left space behind them, empty buildings that can be used as long as you can find a way in—and put up with substandard conditions (buildings fall out of use for a reason). Security is going to be poor to nonexistent—you can try to get a door to lock, but the wall might be deteriorated enough that would-be burglars will just come in through there instead. Plumbing and heat are just pipe dreams. But if you’re lucky, the place will stay dry, and you might be able to slip some change to your neighbors to keep an eye on your stuff (after all, the discarded people of the world gotta stick together). Squatter food is a step better than street-level, in that you’re not pulling stuff from dumpsters, but it’s mostly soy packets and other flavorless drek—the modern equivalent of orphan’s gruel."
    },
    "Low": {
        "Cost": "2,000 nuyen a month",
        "Description": "Now we’re getting somewhere. With this lifestyle, you live in a place that was actually intended to be a residence. Sure, it may have started life as a shipping container, but it was constructed as a home at some point, and it has electricity, running water (though it may be rotated off sometimes during low-supply days), and just enough heat to keep you alive. The doors lock, there’s an official address, and you usually can get the food delivery guy to bring you some McHugh’s soyburgers. Which, incidentally, you sometimes can afford to eat! Plenty of shadowrunners live at this level, along with the workers of the world that the higher-ups prefer to ignore whenever possible."
    },
    "Middle": {
        "Cost": "5,000 nuyen a month",
        "Description": "The good life is now starting to come in reach. Electricity and water around the clock, police officers that do more than chuckle derisively when you report a crime, flavor injections with most meals, and low odds of being mugged when you’re near your home. Is it spectacular? No, but it’s safe, and that’s a rare enough thing in the Sixth World that many people make all sorts of bargains to gain it."
    },
    "High": {
        "Cost": "10,000 nuyen a month",
        "Description": "Flying on an airplane in economy class means watching trid entertainments that are interrupted every five to ten minutes or so by ads that leave you wondering who the hell buys the stuff on display. Aromatherapy foot massagers? Button-free wine bottle opener? Split-rock backyard fire pit? People with a High lifestyle are the targeted customers. They have money to spend and space to put the things they buy. They also have a deep need to not let their peers’ homes be more impressive than theirs. They eat well, sleep comfortably, and have trouble understanding people who complain about the state of the world, because it seems just fine to them. Living among them is a sure sign that you’ve made it, but don’t sleep too well—their tolerance for interlopers is low, and they have ways of pushing out those who they feel don’t belong. The extra security you pay for may well be needed."
    },
    "Luxury": {
        "Cost": "100,000 nuyen a month",
        "Description": "The top. The crème de la crème. People with this lifestyle spend more in a month than squatters and street people earn in several years, or even a lifetime. They do all the things people in the lower lifestyle categories dream about. They eat real meat regularly. They float on boats in the Caribbean and dive off them into azure waters. They stay at hotels where armies of staffers scuttle quickly to meet their needs. They have trid producers hoping to film tours of their homes. Their daily reality is surreal, but any existential angst that might arise can be lulled away with the smoothest liquors, the softest pillows, and the best views money can buy. And remember, the key principle of the Sixth World is that money can buy anything."
    }
}



transformed_priority_data = {
    "Races": [
        {
            "Priority": "A",
            "Dwarf": 13,
            "Ork": 13,
            "Troll": 13
        },
        {
            "Priority": "B",
            "Dwarf": 11,
            "Elf": 11,
            "Ork": 11,
            "Troll": 11
        },
        {
            "Priority": "C",
            "Dwarf": 9,
            "Elf": 9,
            "Human": 9,
            "Ork": 9,
            "Troll": 9
        },
        {
            "Priority": "D",
            "Dwarf": 4,
            "Elf": 4,
            "Human": 4,
            "Ork": 4,
            "Troll": 4
        },
        {
            "Priority": "E",
            "Dwarf": 1,
            "Elf": 1,
            "Human": 1,
            "Ork": 1,
            "Troll": 1
        }
    ],
    "Attributes": [
        {
            "Priority": "A",
            "Value": 24
        },
        {
            "Priority": "B",
            "Value": 16
        },
        {
            "Priority": "C",
            "Value": 12
        },
        {
            "Priority": "D",
            "Value": 8
        },
        {
            "Priority": "E",
            "Value": 2
        }
    ],
    "Skills": [
        {
            "Priority": "A",
            "Value": 32
        },
        {
            "Priority": "B",
            "Value": 24
        },
        {
            "Priority": "C",
            "Value": 20
        },
        {
            "Priority": "D",
            "Value": 16
        },
        {
            "Priority": "E",
            "Value": 10
        }
    ],
    "Magic/Resonance": [
        {
            "Priority": "A",
            "Type": "Full",
            "Value": 4
        },
        {
            "Priority": "A",
            "Type": "Aspected",
            "Value": 5
        },
        {
            "Priority": "A",
            "Type": "Mystic Adept",
            "Value": 4
        },
        {
            "Priority": "A",
            "Type": "Adept",
            "Value": 4
        },
        {
            "Priority": "A",
            "Type": "Technomancer",
            "Value": 4
        },
        {
            "Priority": "B",
            "Type": "Full",
            "Value": 3
        },
        {
            "Priority": "B",
            "Type": "Aspected",
            "Value": 4
        },
        {
            "Priority": "B",
            "Type": "Mystic Adept",
            "Value": 3
        },
        {
            "Priority": "B",
            "Type": "Adept",
            "Value": 3
        },
        {
            "Priority": "B",
            "Type": "Technomancer",
            "Value": 3
        },
        {
            "Priority": "C",
            "Type": "Full",
            "Value": 2
        },
        {
            "Priority": "C",
            "Type": "Aspected",
            "Value": 3
        },
        {
            "Priority": "C",
            "Type": "Mystic Adept",
            "Value": 2
        },
        {
            "Priority": "C",
            "Type": "Adept",
            "Value": 2
        },
        {
            "Priority": "C",
            "Type": "Technomancer",
            "Value": 2
        },
        {
            "Priority": "D",
            "Type": "Full",
            "Value": 1
        },
        {
            "Priority": "D",
            "Type": "Aspected",
            "Value": 2
        },
        {
            "Priority": "D",
            "Type": "Mystic Adept",
            "Value": 1
        },
        {
            "Priority": "D",
            "Type": "Adept",
            "Value": 1
        },
        {
            "Priority": "D",
            "Type": "Technomancer",
            "Value": 1
        },
        {
            "Priority": "E",
            "Type": "Mundane",
            "Value": "Mundane"
        }
    ],
    "Resources": [
        {
            "Priority": "A",
            "Value": 450000
        },
        {
            "Priority": "B",
            "Value": 275000
        },
        {
            "Priority": "C",
            "Value": 150000
        },
        {
            "Priority": "D",
            "Value": 50000
        },
        {
            "Priority": "E",
            "Value": 8000
        }
    ]
}

# # New structure
# transformed_priority_data = {
#     "Races": [],
#     "Attributes": [],
#     "Skills": [],
#     "Magic/Resonance": [],
#     "Resources": []
# }

# # Transform the data
# for priority, details in priority_data.items():
#     if "Races" in details:
#         transformed_priority_data["Races"].append({"Priority": priority, **details["Races"]})
#     if "Attributes" in details:
#         transformed_priority_data["Attributes"].append({"Priority": priority, "Value": details["Attributes"]})
#     if "Skills" in details:
#         transformed_priority_data["Skills"].append({"Priority": priority, "Value": details["Skills"]})
#     if "Magic/Resonance" in details:
#         # Magic/Resonance can be a string (for 'E') or a dictionary
#         if isinstance(details["Magic/Resonance"], dict):
#             for magic_type, value in details["Magic/Resonance"].items():
#                 transformed_priority_data["Magic/Resonance"].append({"Priority": priority, "Type": magic_type, "Value": value})
#         else:  # It's a string for 'E'
#             transformed_priority_data["Magic/Resonance"].append({"Priority": priority, "Type": "Mundane", "Value": details["Magic/Resonance"]})
#     if "Resources" in details:
#         transformed_priority_data["Resources"].append({"Priority": priority, "Value": details["Resources"]})
#
# # Now, 'transformed_priority_data' holds the reorganized structure.
#
# with open('char_transformed_priority_data.json', 'w', encoding='utf-8') as file:
#     json.dump(transformed_priority_data, file, ensure_ascii=False, indent=4)
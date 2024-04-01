from tkinter import filedialog, messagebox

import yaml


class CharacterProfileManager:
    def __init__(self, filepath="character_profile.yaml"):
        self.filepath = filepath
        self.data = self.default_character_data()
        self.load_priorities()  # Ensure priorities are loaded upon initialization

    @staticmethod
    def default_character_data():
        return {
            "attributes": {
                "Physical": {
                    "Body": 0,
                    "Agility": 0,
                    "Reaction": 0,
                    "Strength": 0,
                },
                "Mental": {
                    "Willpower": 0,
                    "Logic": 0,
                    "Intuition": 0,
                    "Charisma": 0,
                },
            },
            "equipment": {
                "armor": {},
                "cyberdeck": {},
                "firearms": {},
                "grenades": {},
                "helmet": {},
                "melee": {},
                "shields": {},
            },
            "karma": {
                "current": None,
                "temporary": None,
                "total": None,
            },
            "Initiative": {
                "Astral": 0,
                "Matrix AR": 0,
                "Matrix Cold Sim VR": 0,
                "Matrix Hot Sim VR": 0,
                "Physical": 0,
                "Rigging AR": 0,
            },
            "level": 0,
            "magic": {
                "Astral": 0,
                "Magic": 0,
                "Resonance": 0,
            },
            "metatype": '',
            "name": '',
            "player_name": '',
            "priorities": {
                "attributes": '',
                "magic": '',
                "metatype": '',
                "resources": '',
                "skills": '',
            },
            "resources": {
                "nuyen": None,
                "spent": None,
            },
            "skills": {
                "Agility": {
                    "Athletics": {
                        "Specializations": [
                            "Climbing",
                            "Flying",
                            "Gymnastics",
                            "Sprinting",
                            "Swimming",
                            "Throwing"
                        ],
                        "Rank": 0,
                        "Untrained": "True",
                        "Description": "Covers physical grace and prowess, including sprinting, full defense actions, and thrown weapon attacks."
                    },
                    "Close Combat": {
                        "Specializations": ["Blades", "Clubs", "Unarmed Combat"],
                        "Rank": 0,
                        "Untrained": "False",
                        "Description": "Used for close-quarters combat with blades, clubs, or unarmed strikes."
                    },
                    "Exotic Weapons": {
                        "Specializations": [],
                        "Rank": 0,
                        "Untrained": "False",
                        "Description": "Covers specialized weaponry requiring specific training."
                    },
                    "Firearms": {
                        "Specializations": ["Automatics", "Longarms", "Pistols", "Rifles", "Shotguns"],
                        "Rank": 0,
                        "Untrained": "True",
                        "Description": "Involves proficiency with various ranged weapons."
                    },
                    "Stealth": {
                        "Specializations": ["Disguise", "Palming", "Sneaking"],
                        "Rank": 0,
                        "Untrained": "True",
                        "Description": "Covers activities characters perform that they do not want others to notice."
                    }
                },
                "Strength": {
                    "Athletics": {
                        "Specializations": [
                            "Climbing",
                            "Flying",
                            "Gymnastics",
                            "Sprinting",
                            "Swimming",
                            "Throwing"
                        ],
                        "Rank": 0,
                        "Untrained": "True",
                        "Description": "Covers physical grace and prowess, including sprinting, full defense actions, and thrown weapon attacks."
                    }
                },
                "Body": {
                    "Athletics": {
                        "Specializations": [
                            "Climbing",
                            "Flying",
                            "Gymnastics",
                            "Sprinting",
                            "Swimming",
                            "Throwing"
                        ],
                        "Rank": 0,
                        "Untrained": "True",
                        "Description": "Covers physical grace and prowess, including sprinting, full defense actions, and thrown weapon attacks."
                    }
                },
                "Reaction": {
                    "Piloting": {
                        "Specializations": ["Ground Craft", "Aircraft", "Watercraft"],
                        "Rank": 0,
                        "Untrained": "True",
                        "Description": "Used for operating vehicles, including ground, air, and watercraft."
                    }
                },
                "Willpower": {
                    "Astral": {
                        "Specializations": [
                            "Astral Combat",
                            "Astral Signatures",
                            "Emotional States",
                            "Spirit Types"
                        ],
                        "Rank": 0,
                        "Untrained": "False",
                        "Description": "Used by magicians, adepts, and mystic adepts with Astral Perception adept power for assensing astral auras and combat."
                    }
                },
                "Intuition": {
                    "Astral": {
                        "Specializations": [
                            "Astral Combat",
                            "Astral Signatures",
                            "Emotional States",
                            "Spirit Types"
                        ],
                        "Rank": 0,
                        "Untrained": "False",
                        "Description": "Used by magicians, adepts, and mystic adepts with Astral Perception adept power for assensing astral auras and combat."
                    },
                    "Outdoors": {
                        "Specializations": ["Navigation", "Survival", "Tracking",
                                            "by Environment (Woods, Desert, Urban Areas, etc.)"],
                        "Rank": 0,
                        "Untrained": "True",
                        "Description": "Used for navigating natural environments and survival techniques."
                    },
                    "Perception": {
                        "Specializations": ["Visual", "Aural", "Tactile",
                                            "by Environment (Woods, Desert, Urban, etc.)"],
                        "Rank": 0,
                        "Untrained": "True",
                        "Description": "Involves observing and noticing details in the environment."
                    }
                },
                "Charisma": {
                    "Con": {
                        "Specializations": ["Acting", "Disguise", "Impersonation", "Performance"],
                        "Rank": 0,
                        "Untrained": "True",
                        "Description": "Involves persuasion through deception or acting, convincing others of false identities or intentions."
                    },
                    "Influence": {
                        "Specializations": [
                            "Etiquette",
                            "Instruction",
                            "Intimidation",
                            "Leadership",
                            "Negotiation"
                        ],
                        "Rank": 0,
                        "Untrained": "True",
                        "Description": "Involves shaping opinions through persuasion or intimidation."
                    }
                },
                "Logic": {
                    "Cracking": {
                        "Specializations": ["Cybercombat", "Electronic Warfare", "Hacking"],
                        "Rank": 0,
                        "Untrained": "False",
                        "Description": "Involves illegal actions in the Matrix, such as hacking and cyber warfare."
                    },
                    "Electronics": {
                        "Specializations": ["Computer", "Hardware", "Software"],
                        "Rank": 0,
                        "Untrained": "True",
                        "Description": "Covers legal Matrix activities like software manipulation and hardware maintenance."
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
                        "Rank": 0,
                        "Untrained": "True",
                        "Description": "Encompasses building, repairing, and modifying mechanical systems."
                    },
                    "Perception": {
                        "Specializations": ["Visual", "Aural", "Tactile",
                                            "by Environment (Woods, Desert, Urban, etc.)"],
                        "Rank": 0,
                        "Untrained": "True",
                        "Description": "Involves observing and noticing details in the environment."
                    }
                },
                "Magic": {
                    "Conjuring": {
                        "Specializations": ["Banishing", "Binding", "Summoning"],
                        "Rank": 0,
                        "Untrained": "False",
                        "Description": "Used for summoning, binding, and banishing spirits."
                    },
                    "Enchanting": {
                        "Specializations": ["Alchemy", "Artificing", "Disenchanting"],
                        "Rank": 0,
                        "Untrained": "False",
                        "Description": "Involves crafting magical items like foci and imbuing objects with magical properties."
                    },
                    "Sorcery": {
                        "Specializations": ["Counterspelling", "Ritual Spellcasting", "Spellcasting"],
                        "Rank": 0,
                        "Untrained": "False",
                        "Description": "Involves casting spells and manipulating magical energies."
                    }
                },
                "Resonance": {
                    "Tasking": {
                        "Specializations": ["Compiling", "Decompiling", "Registering"],
                        "Rank": 0,
                        "Untrained": "False",
                        "Description": "Skill technomancers use for various technomancer activities."
                    },
                },
            },
        },
        "spells_known": {},
        }

        def get_section_data(self, section):
            return self.data.get(section, {})

        def update_section_data(self, section, updated_data):
            if section in self.data and isinstance(updated_data, dict):
                self.data[section] = updated_data

        def load_profile(self, filepath=None):
            """
            Loads profile data from a file and updates the current data.
            If filepath is not specified, prompt the user to select a file.
            """
            if not filepath:  # If no filepath is given, prompt the user to select a file
                filepath = filedialog.askopenfilename(
                    title="Select Profile File",
                    filetypes=(("YAML Files", "*.yaml"), ("All Files", "*.*"))
                )
                if not filepath:  # If the user cancels, return early
                    return False

            try:
                with open(filepath, 'r') as file:
                    self.data = yaml.safe_load(file)
                self.filepath = filepath  # Update the current filepath to the loaded file
                return True
            except Exception as e:
                messagebox.showerror("Load Error", f"Failed to load profile: {e}")
                return False

        def save_profile(self, filepath=None):
            # If no filepath is provided, prompt the user with a file dialog
            if not filepath:
                filepath = filedialog.asksaveasfilename(
                    defaultextension=".yaml",
                    filetypes=[("YAML files", "*.yaml"), ("All files", "*.*")],
                    title="Save Character Profile"
                )
                # If the user cancels the dialog, filepath will be an empty string
                if not filepath:  # User cancelled the save dialog
                    return False

            # Proceed to save the file
            try:
                with open(filepath, 'w') as file:
                    yaml.safe_dump(self.data, file, default_flow_style=False)
                return True
            except Exception as e:
                messagebox.showerror("Save Error", f"Failed to save profile: {e}")
                return False

        def load_priorities(self):
            with open("variables/char_priorities.yaml", "r") as file:
                self.priorities_data = yaml.safe_load(file)

        def get_attribute_priority_rank(self):
            # Ensure priorities_data is available
            if not hasattr(self, 'priorities_data'):
                print("Priorities data not loaded.")
                return "No priority data available"

            priority_level = self.data['priorities']['attributes']

            if not priority_level:  # If priority_level is empty or not valid
                return "Priority not set for attributes"

            # Assuming a valid priority_level, proceed with fetching the rank
            try:
                return self.priorities_data[priority_level]['Attributes']
            except KeyError:
                return f"Invalid priority level: {priority_level}"
    # Example usage:
    # profile_manager = CharacterProfileManager()
    # section_data = profile_manager.get_section_data('attributes')
    # section_data['Physical']['Agility'] = 5
    # profile_manager.update_section_data('attributes', section_data)
    # profile_manager.save_profile('path_to_save/updated_character_profile.yaml')

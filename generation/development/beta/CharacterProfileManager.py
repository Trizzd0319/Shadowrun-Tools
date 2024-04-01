import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import yaml

class CharacterProfileManager:
    def __init__(self, filepath="character_profile.yaml"):
        self.filepath = filepath
        self.data = self.default_character_data()

    @staticmethod
    def default_character_data():
        return {
            "attributes": {
                "Astral": 0,
                "Initiative": {
                    "Astral": 0,
                    "Matrix AR": 0,
                    "Matrix Cold Sim VR": 0,
                    "Matrix Hot Sim VR": 0,
                    "Physical": 0,
                    "Rigging AR": 0,
                },
                "Mental": {
                    "Charisma": 0,
                    "Intuition": 0,
                    "Logic": 0,
                    "Willpower": 0,
                },
                "Physical": {
                    "Agility": 0,
                    "Body": 0,
                    "Reaction": 0,
                    "Strength": 0,
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
            "level": 0,
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
                "Agility": {},
                "Charisma": {},
                "Intuition": {},
                "Logic": {},
                "Reaction": {},
                "Resonance": {},
            },
            "spells_known": {},
        }

    def get_section_data(self, section):
        return self.data.get(section, {})

    def update_section_data(self, section, updated_data):
        if section in self.data and isinstance(updated_data, dict):
            self.data[section] = updated_data

    def save_profile(self, filepath=None):
        filepath = filepath or self.filepath
        try:
            with open(filepath, 'w') as file:
                yaml.safe_dump(self.data, file, default_flow_style=False)
            return True
        except Exception as e:
            print(f"Error saving profile: {e}")
            return False

# Example usage:
# profile_manager = CharacterProfileManager()
# section_data = profile_manager.get_section_data('attributes')
# section_data['Physical']['Agility'] = 5
# profile_manager.update_section_data('attributes', section_data)
# profile_manager.save_profile('path_to_save/updated_character_profile.yaml')

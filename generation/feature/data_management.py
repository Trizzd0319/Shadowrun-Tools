import tkinter as tk

import pandas as pd


class DataManagement:
    def initialize_attributes(self):
        attributes_df = pd.DataFrame({
            'Attribute': ['Body', 'Agility', 'Reaction', 'Strength', 'Willpower', 'Logic', 'Intuition', 'Charisma',
                          'Edge'],
            'LevelVar': [tk.IntVar() for _ in range(9)]
        })
        return attributes_df

    def initialize_skills(self):
        skills_df = pd.DataFrame({
            'Skill': ['Pistols', 'Hacking', 'Spellcasting', 'Negotiation', 'First Aid'],
            'LevelVar': [tk.IntVar() for _ in range(5)]
        })
        return skills_df

    def initialize_priority(self):
        priority_dict = {
            'PRIORITY': ['A', 'B', 'C', 'D', 'E'],
            'ATTRIBUTES': [24, 20, 16, 14, 12],
            'RESOURCES': [450000, 275000, 140000, 50000, 6000]
        }
        return priority_dict

    def get_initial_karma(self):
        return 25

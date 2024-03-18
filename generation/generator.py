import json
from tkinter import Tk, Frame, Button, Label, Entry, ttk, Canvas, Scrollbar, VERTICAL, IntVar, filedialog

import pandas as pd
import pdfrw
import reportlab


class CharacterBuilderGUI:
    def __init__(self, root):
        self.root = root
        self.attributes_priority_label = None  # Placeholder for the dynamic label
        self.magic_priority_label = None  # Placeholder for the dynamic label
        self.metatype_priority_label = None  # Placeholder for the dynamic label
        self.resources_priority_label = None  # Placeholder for the dynamic label
        self.skills_priority_label = None  # Placeholder for the dynamic label
        self.attributes_priority_points = 0  # Current available points
        self.initial_attributes_priority_points = 0  # Initial points from priority selection
        self.skills_priority_points = 0  # Initialize in __init__
        self.total_karma = 50  # Assuming 50 is the starting total karma
        # Initial values for attributes (including Karma and Edge)
        initial_values = [0] * 8 + [50, 3]  # 8 attributes set to 0, Karma to 50, Edge to 3
        self.attributes_df = pd.DataFrame({
            'Attribute': ['Body', 'Agility', 'Reaction', 'Strength', 'Willpower', 'Logic', 'Intuition', 'Charisma',
                          'Karma', 'Edge'],
            'LevelVar': [IntVar(value=val) for val in initial_values]
        })
        self.priority = {
            'PRIORITY': ['A', 'B', 'C', 'D', 'E'],
            'RACES': ['Dwarf, Ork, Troll (13)', 'Dwarf, Elf, Ork, Troll (11)', 'Dwarf, Elf, Human, Ork, Troll (9)',
                      'Dwarf, Elf, Human, Ork, Troll (4)', 'Dwarf, Elf, Human, Ork, Troll (1)'],
            'ATTRIBUTES': [24, 16, 12, 8, 2],
            'SKILLS': [32, 24, 20, 16, 10],
            'MAGIC OR RESONANCE': [
                'Full: 4 Magic, Aspected: 5 Magic, Mystic Adept: 4 Magic, Adept: 4 Magic, Technomancer: 4 Resonance',
                'Full: 3 Magic, Aspected: 4 Magic, Mystic Adept: 3 Magic, Adept: 3 Magic, Technomancer: 3 Resonance',
                'Full: 2 Magic, Aspected: 3 Magic, Mystic Adept: 2 Magic, Adept: 2 Magic, Technomancer: 2 Resonance',
                'Full: 1 Magic, Aspected: 2 Magic, Mystic Adept: 1 Magic, Adept: 1 Magic, Technomancer: 1 Resonance',
                'Mundane'],
            'RESOURCES': ['450,000¥', '275,000¥', '150,000¥', '50,000¥', '8,000¥']
        }
        self.qualities_df = pd.read_csv('qualities.csv')
        self.priority_dict = {
            'PRIORITY': ['A', 'B', 'C', 'D', 'E'],
            'ATTRIBUTES': [24, 16, 12, 8, 2],
            'RACES': [13, 11, 9, 4, 1],
            'SKILLS': [32, 24, 20, 16, 10],
            'RESOURCES': [450000, 275000, 150000, 50000, 8000],
            'MAGIC OR RESONANCE': [0, 0, 0, 0, 0]
            # Add other priority information as needed
        }
        skills_attributes = {
            "Astral (Int/Will)": {
                "Attributes-Primary": "Intuition",
                "Attributes-Secondary": "Willpower",
                "Description": "Astral skills govern the ability to perceive and interact with the astral plane, relying on Intuition for awareness and Willpower for mental defense."
            },
            "Athletics (Agi/Str)": {
                "Attributes-Primary": "Agility",
                "Attributes-Secondary": "Strength",
                "Description": "Athletics encompasses physical activities that require Agility for coordination and movement, and Strength for power."
            },
            "Biotech (Log/Int)": {
                "Attributes-Primary": "Logic",
                "Attributes-Secondary": "Intuition",
                "Description": "Biotech involves the application of medical knowledge and technology, using Logic for understanding complex systems and Intuition for diagnostic processes."
            },
            "Close Combat (Agi)": {
                "Attributes-Primary": "Agility",
                "Attributes-Secondary": "Strength",
                "Description": "Close Combat skills determine proficiency in melee fighting, primarily requiring Agility for quick movements and Strength for forceful strikes."
            },
            "Con (Cha)": {
                "Attributes-Primary": "Charisma",
                "Attributes-Secondary": "Logic",
                "Description": "Con skills revolve around deception and persuasion, with Charisma aiding in convincing others and Logic for constructing believable lies."
            },
            "Conjuring (Mag)": {
                "Attributes-Primary": "Magic",
                "Attributes-Secondary": "Willpower",
                "Description": "Conjuring allows the summoning of spirits or magical entities, relying on Magic ability and supported by the caster's Willpower."
            },
            "Cracking (Log)": {
                "Attributes-Primary": "Logic",
                "Attributes-Secondary": "Intuition",
                "Description": "Cracking skills are used for hacking and bypassing security systems, requiring Logic to solve puzzles and Intuition to anticipate system behavior."
            },
            "Electronics (Log)": {
                "Attributes-Primary": "Logic",
                "Attributes-Secondary": "Intuition",
                "Description": "Electronics involve working with complex gadgets, where Logic is used for understanding circuitry and Intuition for troubleshooting."
            },
            "Enchanting (Mag)": {
                "Attributes-Primary": "Magic",
                "Attributes-Secondary": "Logic",
                "Description": "Enchanting is the art of imbuing objects with magical properties, primarily using Magic and Logic to understand magical theory."
            },
            "Engineering (Log/Int)": {
                "Attributes-Primary": "Logic",
                "Attributes-Secondary": "Intuition",
                "Description": "Engineering skills cover the design and maintenance of machinery, demanding Logic for technical knowledge and Intuition for innovative solutions."
            },
            "Exotic Weapons (Agi)": {
                "Attributes-Primary": "Agility",
                "Attributes-Secondary": "Logic",
                "Description": "Handling exotic weapons requires Agility for precision and Logic for understanding unconventional mechanisms."
            },
            "Firearms (Agi)": {
                "Attributes-Primary": "Agility",
                "Attributes-Secondary": "Intuition",
                "Description": "Proficiency with firearms depends on Agility for aiming and Intuition for timing and situational awareness."
            },
            "Influence (Cha/Log)": {
                "Attributes-Primary": "Charisma",
                "Attributes-Secondary": "Logic",
                "Description": "Influence skills involve swaying others through negotiation, leveraging Charisma to appeal emotionally and Logic to argue convincingly."
            },
            "Outdoors (Int)": {
                "Attributes-Primary": "Intuition",
                "Attributes-Secondary": "Strength",
                "Description": "Outdoor skills require Intuition for navigation and environmental awareness, supported by physical Strength for endurance."
            },
            "Perception (Int/Log)": {
                "Attributes-Primary": "Intuition",
                "Attributes-Secondary": "Logic",
                "Description": "Perception covers the ability to notice details and clues, using Intuition for gut feelings and Logic for piecing together information."
            },
            "Piloting (Rea)": {
                "Attributes-Primary": "Reaction",
                "Attributes-Secondary": "Agility",
                "Description": "Piloting vehicles demands quick Reaction to handle dynamic situations and Agility for precise control."
            },
            "Sorcery (Mag)": {
                "Attributes-Primary": "Magic",
                "Attributes-Secondary": "Willpower",
                "Description": "Sorcery encompasses casting spells, requiring a strong Magic foundation and Willpower to control the magical energies."
            },
            "Stealth (Agi)": {
                "Attributes-Primary": "Agility",
                "Attributes-Secondary": "Intuition",
                "Description": "Stealth involves moving unseen and unheard, relying on Agility for silent movements and Intuition for avoiding detection."
            },
            "Tasking (Res)": {
                "Attributes-Primary": "Resonance",
                "Attributes-Secondary": "Logic",
                "Description": "Tasking in the context of technomancy involves using Resonance to interface with technology and Logic to manipulate complex systems."
            }
        }

        # To dynamically include all skills from your DataFrame into this dictionary, you'd typically fetch these mappings from a database or an external file that defines these relationships, as hardcoding them (as done here) might not be scalable or easy to maintain for a large number of skills.

        # Skills initialization
        skills = ["Astral (Int/Will)", "Athletics (Agi/Str)", "Biotech (Log/Int)", "Close Combat (Agi)",
                  "Con (Cha)", "Conjuring (Mag)", "Cracking (Log)", "Electronics (Log)", "Enchanting (Mag)",
                  "Engineering (Log/Int)", "Exotic Weapons (Agi)", "Firearms (Agi)", "Influence (Cha/Log)",
                  "Outdoors (Int)", "Perception (Int/Log)", "Piloting (Rea)", "Sorcery (Mag)", "Stealth (Agi)",
                  "Tasking (Res)"]

        self.skills_df = pd.DataFrame({
            'Skill': skills,
            'LevelVar': [IntVar(value=0) for _ in skills]  # Initial values for each skill
        })
        self.character_creation = True  # Flag to indicate if it's character creation phase
        # Extract attributes and their levels
        attributes = {
            row['Attribute']: row['LevelVar'].get()
            for _, row in self.attributes_df.iterrows()
        }

        # Extract skills and their levels
        skills = {
            row['Skill']: row['LevelVar'].get()
            for _, row in self.skills_df.iterrows()
        }

        character_data = {
            "attributes": attributes,
            "skills": skills
        }
        self.setup_ui()

    def setup_ui(self):
        # Window basic setup
        self.root.title("Character Builder")
        self.root.geometry("800x600")

        # Top Buttons
        self.create_top_buttons()

        # Save/Reset/Load Buttons
        self.create_save_reset_load_buttons()

        # Scrollable Area Setup
        self.create_scrollable_area()

        # Sections Creation
        self.create_sections()

    def create_top_buttons(self):
        pass

    #     # Top buttons frame
    #     top_buttons_frame = Frame(self.root)
    #     top_buttons_frame.pack(fill='x')
    #
    #     # Buttons: New, Open, Save
    #     Button(top_buttons_frame, text="Button 1").grid(row=0, column=0, padx=5, pady=5)
    #     Button(top_buttons_frame, text="Button 2").grid(row=0, column=1, padx=5, pady=5)
    #     Button(top_buttons_frame, text="Button 3").grid(row=0, column=2, padx=5, pady=5)
    def save_character_data(self):
        # Extract attributes and their levels
        attributes = {row['Attribute']: row['LevelVar'].get() for _, row in self.attributes_df.iterrows()}

        # Extract skills and their levels
        skills = {row['Skill']: row['LevelVar'].get() for _, row in self.skills_df.iterrows()}

        # Extract priorities selections
        # Extract priorities selections correctly
        priorities = {category: combobox.get() for category, combobox in
                      self.comboboxes.items()}  # Use .items() for dictionaries

        character_data = {
            "attributes": attributes,
            "skills": skills,
            "priorities": priorities
        }

        filepath = filedialog.asksaveasfilename(defaultextension=".json",
                                                filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if not filepath:  # If the dialog is cancelled, no filepath will be selected.
            return

        with open(filepath, 'w') as f:
            json.dump(character_data, f, indent=4)

    def load_character_data(self):
        filepath = filedialog.askopenfilename(filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if not filepath:
            return

        with open(filepath, 'r') as f:
            character_data = json.load(f)

        # Update attributes
        for attribute, value in character_data["attributes"].items():
            index = self.attributes_df.index[self.attributes_df['Attribute'] == attribute].tolist()
            if index:
                self.attributes_df.at[index[0], 'LevelVar'].set(value)

        # Update skills
        for skill, value in character_data["skills"].items():
            index = self.skills_df.index[self.skills_df['Skill'] == skill].tolist()
            if index:
                self.skills_df.at[index[0], 'LevelVar'].set(value)

        # Assuming character_data["priorities"] is a dictionary like {"Attributes": "A", "Magic/Resonance": "B", ...}
        if "priorities" in character_data:
            for category, selection in character_data["priorities"].items():
                # Ensure we're setting the selection on the combobox widget
                if category in self.comboboxes:
                    self.comboboxes[category].set(selection)

    def create_save_reset_load_buttons(self):
        # Save/Reset/Load buttons frame
        srl_buttons_frame = Frame(self.root)
        srl_buttons_frame.pack(fill='x')

        # Buttons: Save, Reset, Load
        Button(srl_buttons_frame, text="Save", command=self.save_character_data).grid(row=0, column=0, padx=5, pady=5)
        Button(srl_buttons_frame, text="Reset", command=self.reset_form).grid(row=0, column=1, padx=5, pady=5)
        Button(srl_buttons_frame, text="Load", command=self.load_character_data).grid(row=0, column=2, padx=5, pady=5)

    def create_scrollable_area(self):
        # Create a canvas and a scrollbar attached to the root
        self.canvas = Canvas(self.root)
        self.scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview)

        # Pack scrollbar to the right, fill y. Expand canvas to fill the rest
        self.scrollbar.pack(side='right', fill='y')
        self.canvas.pack(side='left', fill='both', expand=True)

        # Configure canvas to be scrollable with the scrollbar
        self.canvas.configure(scrollregion=self.canvas.bbox("all"))

        # Bind canvas region to all
        self.canvas.bind('<Configure>', lambda e: self.canvas.configure(scrollregion=self.canvas.bbox('all')))

        # Create a frame inside the canvas
        self.scrollable_frame = Frame(self.canvas)

        # Add the frame to the canvas
        self.canvas_frame = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')

        # Enable mousewheel scrolling on Windows/Linux
        self.scrollable_frame.bind('<Enter>', lambda e: self.canvas.bind_all('<MouseWheel>', self.on_mousewheel))
        self.scrollable_frame.bind('<Leave>', lambda e: self.canvas.unbind_all('<MouseWheel>'))

    def on_mousewheel(self, event):
        """Handle mouse wheel scroll for Windows/Linux."""
        self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")

    def create_sections(self):
        # Defined sections
        sections = [
            "Priority Selections", "Player Info", "Personal", "Attributes", "Skills",
            "IDs/Lifestyle/Currency", "Core Combat Info", "Qualities", "Contacts",
            "Weapons, Ranged", "Weapons, Melee", "Armor", "Augmentations", "Gear",
            "Vehicles", "Matrix Stats", "Spells / Preparations / Rituals / Complex Forms", "Adept Powers"
        ]

        # Sections creation with special handling for Priority Selections
        for section in sections:
            if section == "Priority Selections":
                self.create_priority_selection_section()
            # if section == "Player Info":
            # self.create_player_section()
            if section == "Personal":
                self.create_personal_section()
            if section == "Attributes":
                self.create_attributes_section()
            if section == "Skills":
                self.create_skills_section()
            # if section == "IDs/Lifestyle/Currency":
            #     self.create_ids_selection_section()
            # if section == "Core Combat Info":
            #     self.create_core_combat_selection_section()
            # if section == "Qualities":
            #     self.create_priority_selection_section()
            # if section == "Contacts":
            #     self.create_contacts_selection_section()
            # if section == "Weapons, Ranged":
            #     self.create_weapons_ranged_selection_section()
            # if section == "Weapons, Melee":
            #     self.create_weapons_melee_selection_section()
            # if section == "Armor":
            #     self.create_armor_selection_section()
            # if section == "Augmentations":
            #     self.create_augmentations_selection_section()
            # if section == "Gear":
            #     self.create_gear_selection_section()
            # if section == "Vehicles":
            #     self.create_vehicles_selection_section()
            # if section == "Matrix Stats":
            #     self.create_matrix_selection_section()
            # if section == "Spells / Preparations / Rituals / Complex Forms":
            #     self.create_spells_selection_section()
            # if section == "Adept Powers":
            #     self.create_adept_selection_section()
            else:
                section_frame = Frame(self.scrollable_frame, height=50, bd=1, relief="solid")
                section_frame.pack(fill='x', padx=10, pady=5, expand=True)
                Label(section_frame, text=section).pack(side="left", padx=5, pady=5)
                # Button(section_frame, text=f"Button for {section}").pack(side="right", padx=5, pady=5)

    # def extract_priority_value_from_label(self, label):
    #     """Extracts and returns the numerical priority value from a label's text."""
    #     # Assuming the label's text format is "Category - Value"
    #     try:
    #         _, value = label.cget("text").split(" - ")
    #         return int(value)  # Convert the extracted value to an integer
    #     except ValueError:
    #         # If the value cannot be converted to an integer or the text does not follow the expected format,
    #         # this block will catch the exception.
    #         return None  # You could return a default value or None if the extraction fails

    def extract_priority_value_from_label(self, label):
        try:
            # Directly get the label's text
            value = label.cget("text")
            # Attempt to convert the text to an integer
            return int(value)
        except ValueError:
            # Return None or a default value if conversion fails
            return None

    def update_attributes_priority_points(self):
        # Extract the value from the label
        value = self.extract_priority_value_from_label(self.attributes_priority_label)
        if value is not None:
            self.attributes_priority_points = value
        else:
            # Handle case where no valid number is extracted
            self.attributes_priority_points = 0  # Or appropriate default value

    def synchronize_attributes_priority_points_from_label(self):
        try:
            # Attempt to extract and convert the label's text to an integer
            self.attributes_priority_points = int(self.attributes_priority_label.cget("text"))
        except ValueError:
            # Handle cases where the label does not contain a valid integer
            self.attributes_priority_points = 0

    def synchronize_skills_priority_points_from_label(self):
        try:
            self.skills_priority_points = int(self.skills_priority_label.cget("text"))
        except ValueError:
            self.skills_priority_points = 0

    def increment_attribute_level(self, var, index):
        # Ensure points are synchronized with the label
        self.synchronize_attributes_priority_points_from_label()

        attribute_name = self.attributes_df.loc[index, 'Attribute']
        if attribute_name != "Edge":
            next_level_cost = (var.get() + 1) * 5
            karma_index = self.attributes_df[self.attributes_df['Attribute'] == 'Karma'].index[0]
            karma_available = self.attributes_df.at[karma_index, 'LevelVar'].get()

            if var.get() < 6:
                priority_points_used = min(self.attributes_priority_points, next_level_cost)
                next_level_cost -= priority_points_used
                self.attributes_priority_points -= priority_points_used

                if 0 < next_level_cost <= karma_available:
                    new_karma_value = karma_available - next_level_cost
                    self.attributes_df.at[karma_index, 'LevelVar'].set(new_karma_value)
                    var.set(var.get() + 1)
                elif next_level_cost == 0:
                    var.set(var.get() + 1)

                # Update the label with the new priority points value
                self.attributes_priority_label.config(text=str(self.attributes_priority_points))

    def increment_skill_level(self, var, index):
        self.synchronize_skills_priority_points_from_label()
        next_level_cost = (var.get() + 1) * 5
        karma_index = self.attributes_df[self.attributes_df['Attribute'] == 'Karma'].index[0]
        karma_available = self.attributes_df.at[karma_index, 'LevelVar'].get()

        # Attempt to use skill priority points first
        if self.skills_priority_points >= next_level_cost:
            self.skills_priority_points -= next_level_cost
            var.set(var.get() + 1)
        else:
            # Calculate remaining cost after using available skill priority points
            remaining_cost = next_level_cost - self.skills_priority_points
            # Use up all available skill priority points
            self.skills_priority_points = 0

            # Now attempt to use Karma for any remaining cost
            if karma_available >= remaining_cost:
                karma_available -= remaining_cost
                self.attributes_df.at[karma_index, 'LevelVar'].set(karma_available)
                var.set(var.get() + 1)

        # Update the skills label with the new priority points value
        self.skills_priority_label.config(text=str(self.skills_priority_points))
        # Assuming there's a label for Karma similar to skills_priority_label
        karma_available = self.attributes_df.at[karma_index, 'LevelVar'].get()

        # Ensure Karma doesn't exceed total_karma
        if karma_available > self.total_karma:
            excess_karma = karma_available - self.total_karma
            self.skills_priority_points += excess_karma // 5  # Assuming conversion rate is 1:1
            karma_available = self.total_karma
            self.attributes_df.at[karma_index, 'LevelVar'].set(karma_available)
            self.skills_priority_label.config(text=str(self.skills_priority_points))
            new_karma_value = karma_available - next_level_cost
            self.attributes_df.at[karma_index, 'LevelVar'].set(new_karma_value)

    def update_attributes_priority_label_with_points(self):
        # Update the label to show the new value of attributes_priority_points
        self.attributes_priority_label.config(text=f"{self.attributes_priority_points}")

    def update_skills_priority_label_with_points(self):
        # Update the label to show the new value of attributes_priority_points
        self.skills_priority_label.config(text=f"{self.skills_priority_points}")

    def decrement_attribute_level(self, var, index):
        attribute_name = self.attributes_df.loc[index, 'Attribute']
        if attribute_name != "Edge" and var.get() > 0:
            current_level_cost = var.get() * 5  # Cost to refund
            karma_index = self.attributes_df[self.attributes_df['Attribute'] == 'Karma'].index[0]
            karma_available = self.attributes_df.at[karma_index, 'LevelVar'].get()

            # Calculate the potential karma after refund
            potential_karma_after_refund = karma_available + current_level_cost

            if potential_karma_after_refund <= self.total_karma:
                # Refund to karma if it doesn't exceed total_karma
                self.attributes_df.at[karma_index, 'LevelVar'].set(potential_karma_after_refund)
            else:
                # Refund the difference to total_karma, the rest goes to priority points
                excess_to_refund = potential_karma_after_refund - self.total_karma
                self.attributes_df.at[karma_index, 'LevelVar'].set(self.total_karma)  # Reset karma to total_karma
                self.attributes_priority_points += excess_to_refund  # // 5  # Assuming direct conversion rate
                # Update the label to reflect the new points
                self.attributes_priority_label.config(text=str(self.attributes_priority_points))

            var.set(var.get() - 1)  # Decrement the attribute level

    def decrement_skill_level(self, var, index):
        current_level_cost = var.get() * 5  # Cost to refund
        if var.get() > 0:
            karma_index = self.attributes_df[self.attributes_df['Attribute'] == 'Karma'].index[0]
            karma_available = self.attributes_df.at[karma_index, 'LevelVar'].get()

            potential_karma_after_refund = karma_available + current_level_cost

            if potential_karma_after_refund <= self.total_karma:
                self.attributes_df.at[karma_index, 'LevelVar'].set(potential_karma_after_refund)
            else:
                excess_to_refund = potential_karma_after_refund - self.total_karma
                self.attributes_df.at[karma_index, 'LevelVar'].set(self.total_karma)  # Reset karma to total_karma
                self.skills_priority_points += excess_to_refund  # // 5  # Assuming direct conversion rate
                # Update the skills label with the new points
                self.skills_priority_label.config(text=str(self.skills_priority_points))

            var.set(var.get() - 1)  # Decrement the skill level

    def create_priority_selection_section(self):
        priority_frame = Frame(self.scrollable_frame, bd=1, relief="solid")
        priority_frame.pack(fill='x', padx=10, pady=5, expand=True)

        # Defining priority categories and choices
        priority_categories = ["Attributes", "Magic/Resonance", "Metatype", "Skills", "Resources"]
        self.priority_choices = ["A", "B", "C", "D", "E"]
        self.comboboxes = {}

        # Creating labels and comboboxes for each category
        for i, category in enumerate(priority_categories):
            Label(priority_frame, text=f"{category} Priority:").grid(row=0, column=i, padx=5, pady=2)
            combobox = ttk.Combobox(priority_frame, values=self.priority_choices, state="readonly",
                                    name=f"{category.lower()}_priority_combobox")
            combobox.grid(row=1, column=i, padx=5, pady=2)
            combobox.set("Select Priority")
            combobox.bind("<<ComboboxSelected>>", self.update_comboboxes)
            self.comboboxes[category] = combobox

    def create_player_info_section(self):
        player_info_frame = Frame(self.scrollable_frame, bd=1, relief="solid")
        player_info_frame.pack(fill='x', padx=10, pady=5, expand=True)

        Label(player_info_frame, text="Player Name").grid(row=0, column=0, padx=5, pady=5)
        Entry(player_info_frame).grid(row=0, column=1, padx=5, pady=5)

        Label(player_info_frame, text="Notes").grid(row=1, column=0, padx=5, pady=5)
        Entry(player_info_frame).grid(row=1, column=1, padx=5, pady=5)

    def create_personal_section(self):
        personal_info_frame = Frame(self.scrollable_frame, bd=1, relief="solid")
        personal_info_frame.pack(fill='x', padx=10, pady=5, expand=True)

        Label(personal_info_frame, text="Player Name").grid(row=0, column=0, padx=5, pady=5)
        Entry(personal_info_frame).grid(row=0, column=1, padx=5, pady=5)

        Label(personal_info_frame, text="Notes").grid(row=1, column=0, padx=5, pady=5)
        Entry(personal_info_frame).grid(row=1, column=1, padx=5, pady=5)

    def create_attributes_section(self):
        attributes_frame = Frame(self.scrollable_frame, bd=1, relief="solid")
        attributes_frame.pack(fill='both', expand=True, padx=10, pady=5)

        Label(attributes_frame, text="Attributes", font=('Arial', 14), justify='center').grid(row=0, columnspan=4,
                                                                                              sticky='ew')
        # # Create a label to display the extracted priority value
        # self.attributes_priority_extracted_label = Label(attributes_frame, text="Priority Value: Not Set")
        # self.attributes_priority_extracted_label.grid(row=0, column=6, columnspan=1, sticky='w')

        attributes_per_row = 4  # Number of attributes per row
        row = 1  # Start from the second row due to the title label

        for i, attribute_row in enumerate(self.attributes_df.itertuples()):
            column_offset = (i % attributes_per_row) * 4  # Space for Attribute Name, -, Level, +

            attribute_name = attribute_row.Attribute
            level_var = attribute_row.LevelVar

            Label(attributes_frame, text=attribute_name).grid(row=row, column=column_offset, padx=5, pady=5)
            Label(attributes_frame, textvariable=level_var, width=5).grid(row=row, column=column_offset + 1, padx=5,
                                                                          pady=5)
            decrement_button = Button(attributes_frame, text="-",
                                      command=lambda var=level_var, idx=i: self.decrement_attribute_level(var, idx))
            decrement_button.grid(row=row, column=column_offset + 2, padx=5, pady=5)

            increment_button = Button(attributes_frame, text="+",
                                      command=lambda var=level_var, idx=i: self.increment_attribute_level(var, idx))
            increment_button.grid(row=row, column=column_offset + 3, padx=5, pady=5)

            # Every 'attributes_per_row' attributes, start a new row
            if (i + 1) % attributes_per_row == 0:
                row += 1

        # Priority label for attributes
        self.attributes_priority_label = Label(attributes_frame, text="Priority: ")
        self.attributes_priority_label.grid(row=0, column=4, padx=10, pady=5, sticky='w')
        self.update_attributes_priority_label()  # Update the priority label initially    def create_skills_section(self):

    def create_skills_section(self):
        skills_frame = Frame(self.scrollable_frame, bd=1, relief="solid")
        skills_frame.pack(fill='both', expand=True, padx=10, pady=5)

        Label(skills_frame, text="Skills", font=('Arial', 14), justify='center').grid(row=0, columnspan=4, sticky='ew')

        skills_per_row = 4  # Number of skills per row
        row = 1  # Start from the second row due to the title label

        for i, skill_row in enumerate(self.skills_df.itertuples()):
            column_offset = (i % skills_per_row) * 4  # Space for Skill Name, -, Level, +

            skill_name = skill_row.Skill
            level_var = skill_row.LevelVar

            Label(skills_frame, text=skill_name).grid(row=row, column=column_offset, padx=5, pady=5)
            Label(skills_frame, textvariable=level_var, width=5).grid(row=row, column=column_offset + 1, padx=5, pady=5)
            decrement_button = Button(skills_frame, text="-",
                                      command=lambda var=level_var, idx=i: self.decrement_skill_level(var, idx))
            decrement_button.grid(row=row, column=column_offset + 2, padx=5, pady=5)
            increment_button = Button(skills_frame, text="+",
                                      command=lambda var=level_var, idx=i: self.increment_skill_level(var, idx))
            increment_button.grid(row=row, column=column_offset + 3, padx=5, pady=5)

            # Every 'skills_per_row' skills, start a new row
            if (i + 1) % skills_per_row == 0:
                row += 1

        # Priority label for skills
        self.skills_priority_label = Label(skills_frame, text="Priority: ")
        self.skills_priority_label.grid(row=0, column=4, padx=10, pady=5, sticky='w')


    # Function to get the priority value based on priority level
    def get_priority_value(self, category, selected_priority):
        """Retrieve the priority value for a given category based on the selected priority level."""
        if selected_priority not in self.priority_dict['PRIORITY']:
            return "Select Priority"  # Or another placeholder value indicating no valid selection

        priority_values = self.priority_dict[category.upper()]  # Categories in priority_dict are uppercase
        priority_index = self.priority_dict['PRIORITY'].index(selected_priority)
        return priority_values[priority_index]

    def get_priority_value_attribute(priority_level, priority_dict):
        """
        Get the priority value for attributes based on the selected priority level.

        Args:
        - priority_level (str): The selected priority level for attributes (A, B, C, D, E).
        - priority_dict (dict): The dictionary containing priority information.

        Returns:
        - int: The attribute priority value corresponding to the selected priority level.
        """
        attribute_priority = priority_dict['ATTRIBUTES']

        # Ensure priority_level is valid
        if priority_level in priority_dict['PRIORITY']:
            index = priority_dict['PRIORITY'].index(priority_level)
            return attribute_priority[index]
        else:
            # Handle invalid priority level gracefully, returning a default value or raising an error
            return None  # Or raise an exception, print a warning, etc.

    def update_attributes_priority_label(self):
        # Get the selected priority level from the combobox
        selected_priority = self.comboboxes["Attributes"].get()

        # Check for a valid selection and retrieve the corresponding value
        if selected_priority in self.priority_dict['PRIORITY']:
            priority_index = self.priority_dict['PRIORITY'].index(selected_priority)
            priority_value = self.priority_dict['ATTRIBUTES'][priority_index]

            # Update the label to show only the priority value, not the category
            self.attributes_priority_label.config(text=f"{priority_value}")
        else:
            # If selection is invalid, set a default message or leave blank
            self.attributes_priority_label.config(text="N/A")  # Adjust based on your preference

    def update_skills_priority_label(self, event=None):
        priority_value = None  # Initialize priority_value to None

        # Determine the priority based on the current attribute values
        current_priority = self.get_priority_value_attribute(self.priority)

        # Check if the current_priority is valid
        if current_priority is not None:
            # Retrieve the priority value from priority_dict based on the current_priority
            priority_value = self.priority_dict['SKILLS'][current_priority]

        # Update the label with the priority value
        self.skills_priority_label.config(text="Priority: " + str(priority_value))

    # def update_comboboxes(self, event):
    #     # Identifying which combobox was updated
    #     updated_combobox = event.widget
    #     updated_category = None
    #     for category, combobox in self.comboboxes.items():
    #         if combobox == updated_combobox:
    #             updated_category = category
    #             break
    #
    #     # Updating all comboboxes to reflect current selections and prevent duplicates
    #     current_selections = [combobox.get() for combobox in self.comboboxes.values() if
    #                           combobox.get() != "Select Priority"]
    #     available_choices = [choice for choice in self.priority_choices if choice not in current_selections]
    #
    #     for combobox in self.comboboxes.values():
    #         current_value = combobox.get()
    #         combobox['values'] = ["Select Priority"] + available_choices
    #         if current_value in self.priority_choices:
    #             combobox.set(current_value)
    #
    #     # Update the appropriate priority label based on the combobox that was updated
    #     if updated_category == "Attributes":
    #         self.attributes_priority_label.config(text=f"Priority: {updated_combobox.get()}")
    #     elif updated_category == "Skills":
    #         self.skills_priority_label.config(text=f"Priority: {updated_combobox.get()}")

    def update_comboboxes(self, event):
        """Update combobox selections and handle priority value display for all categories."""
        updated_combobox = event.widget
        updated_category = None
        for category, combobox in self.comboboxes.items():
            if combobox == updated_combobox:
                updated_category = category
                break

        # Preventing duplicate selections in comboboxes
        # Existing code to update combobox values...

        # Update the appropriate priority label with the value based on the selection
        selected_priority = updated_combobox.get()
        if selected_priority != "Select Priority":
            priority_value = self.get_priority_value(updated_category, selected_priority)
            if updated_category == "Attributes":
                self.attributes_priority_label.config(text=f"{priority_value}")
            elif updated_category == "Skills":
                self.skills_priority_label.config(text=f"{priority_value}")
            # Add similar elif blocks for other categories if they have dedicated labels for displaying priority values

    def reset_form(self):
        # Reset attributes to their initial values, with Karma as 50 and Edge as 3
        initial_values = [0] * 8 + [50, 3]
        for idx, val in enumerate(initial_values):
            self.attributes_df.at[idx, 'LevelVar'].set(val)

        # Reset skills to 0
        for idx in range(len(self.skills_df)):
            self.skills_df.at[idx, 'LevelVar'].set(0)

        # Reset priority comboboxes to "Select Priority"
        for combobox in self.comboboxes.values():  # Make sure to use .values() to access the combobox widgets
            combobox.set("Select Priority")

    # Reset any other stateful GUI elements here


# Placeholder for executing the GUI application
if __name__ == "__main__":
    root = Tk()
    app = CharacterBuilderGUI(root)
    root.mainloop()

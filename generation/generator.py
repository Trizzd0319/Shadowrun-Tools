import json
import tkinter
from tkinter import Tk, Frame, Button, Label, Entry, ttk, Canvas, Scrollbar, VERTICAL, IntVar, filedialog, Text, NORMAL, \
    END, DISABLED, Listbox, WORD

import pandas as pd


class CharacterBuilderGUI:
    def __init__(self, root, qualities_frame=None):
        self.combined_qualities_label = Label(qualities_frame, text="Confirmed Qualities: None")
        self.combined_qualities_label.pack(pady=10)  # Adjust padding as needed
        self.karma_available = 50  # Or whatever your starting karma is
        # Initialize as Labels instead of lists
        self.confirmed_positive_qualities = []
        self.confirmed_negative_qualities = []
        initial_values = [0, 0, 0, 0, 0, 0, 0, 0, 50, 3]  # Default values for attributes, with Karma=50 and Edge=3
        self.attributes_df = pd.DataFrame({
            'Attribute': ['Body', 'Agility', 'Reaction', 'Strength', 'Willpower', 'Logic', 'Intuition', 'Charisma',
                          'Karma', 'Edge'],
            'LevelVar': [IntVar(value=val) for val in initial_values]
        })
        self.attributes_priority_label = None  # Placeholder for the dynamic label
        self.attributes_priority_points = 0  # Current available points
        self.ears_memo = None
        self.height_combobox = None
        self.initial_attributes_priority_points = 0  # Initial points from priority selection
        self.known_for_memo = None
        self.magic_priority_label = None  # Placeholder for the dynamic label
        self.metatype_attributes = {
            "Metatype": ["Human", "Dwarf", "Elf", "Ork", "Troll"],
            "Body_min": [1, 1, 1, 1, 1],
            "Body_max": [6, 7, 6, 8, 9],
            "Agility_min": [1, 1, 1, 1, 1],
            "Agility_max": [6, 6, 7, 6, 5],
            "Reaction_min": [1, 1, 1, 1, 1],
            "Reaction_max": [6, 5, 6, 6, 6],
            "Strength_min": [1, 1, 1, 1, 1],
            "Strength_max": [6, 8, 6, 8, 9],
            "Willpower_min": [1, 1, 1, 1, 1],
            "Willpower_max": [6, 7, 6, 6, 6],
            "Logic_min": [1, 1, 1, 1, 1],
            "Logic_max": [6, 6, 6, 6, 6],
            "Intuition_min": [1, 1, 1, 1, 1],
            "Intuition_max": [6, 6, 6, 6, 6],
            "Charisma_min": [1, 1, 1, 1, 1],
            "Charisma_max": [6, 6, 8, 5, 5],
            "Edge_min": [1, 1, 1, 1, 1],
            "Edge_max": [7, 6, 6, 6, 6]
        }
        self.metatype_combobox = None
        self.metatype_data = {
            "Metatype": ["Dwarf", "Elf", "Human", "Ork", "Troll"],
            "Ears": [
                "Slightly pointy",
                "Pointy",
                "Rounded",
                "Pointy",
                "Slightly pointy, often hidden by horns"
            ],
            "Known for": [
                "Short size; stocky build; perseverance",
                "Slender, lithe build; being attractive and knowing it",
                "Average size; average build; freaking out about people who don’t meet their averages",
                "Big, powerful physique; tusks; constantly being seen as outsiders",
                "Being so big, you guys. Just huge. And horns."
            ],
            "Description": [
                "Often accepted into mainstream society without being fully valued.",
                "Prosperous nations, powerful positions, celebrities.",
                "Majority of sentient beings, create definitions of 'normal'.",
                "Make people nervous, kept from building collective strength.",
                "Imposing, difficult to assimilate due to physical differences."
            ],
            "Average Height (feet)": [3.94, 6.23, 5.74, 6.23, 8.20],
            "Average Weight (pounds)": [119.05, 176.37, 171.96, 282.19, 661.39],
            "Quality #1": ["Thermographic Vision", "Low-Light Vision", "", "Low-Light Vision", "Thermographic Vision"],
            "Quality #2": ["Toxin Resistance", "", "", "Built Tough 1", "Built Tough 1"],
            "Quality #3": ["", "", "", "", "Dermal Deposits"],
        }
        self.negative_qualities_frame = None
        self.positive_qualities_frame = None
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
        self.priority_dict = {
            'PRIORITY': ['A', 'B', 'C', 'D', 'E'],
            'ATTRIBUTES': [24, 16, 12, 8, 2],
            'RACES': [13, 11, 9, 4, 1],
            'SKILLS': [32, 24, 20, 16, 10],
            'RESOURCES': [450000, 275000, 150000, 50000, 8000],
            'MAGIC OR RESONANCE': [0, 0, 0, 0, 0]
            # Add other priority information as needed
        }
        self.qualities = pd.read_csv('qualities.csv')
        self.racial_quality_labels = []  # Initialize the list for racial quality labels
        self.racial_qualities_memo = None
        self.resources_priority_label = None  # Placeholder for the dynamic label
        self.root = root
        self.skills_priority_label = None  # Placeholder for the dynamic label
        self.skills_priority_points = 0  # Initialize in __init__
        self.total_karma = 50  # Assuming 50 is the starting total karma
        self.weight_combobox = None

        # To dynamically include all skills from your DataFrame into this dictionary, you'd typically fetch these
        # mappings from a database or an external file that defines these relationships, as hardcoding them (as done
        # here) might not be scalable or easy to maintain for a large number of skills.

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
        self.racial_quality_labels = []  # Initialize the list for racial quality labels
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

        # Create the qualities frame here
        qualities_frame = Frame(self.scrollable_frame)
        qualities_frame.pack(pady=10, expand=True, fill="both")

        # Now you can safely initialize racial_quality_labels with Labels in qualities_frame
        self.racial_quality_labels = [Label(qualities_frame, text="") for _ in range(3)]
        for label in self.racial_quality_labels:
            label.pack(side="left")

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
            if section == "Qualities":
                self.create_qualities_section()  # Call to create the Racial Qualities section
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

    def calculate_range_for_height(self, average, percentage):
        start = average * (1 - percentage)
        end = average * (1 + percentage)
        start_inches = int(start * 12)
        end_inches = int(end * 12)
        range_values = [f"{inches // 12}' {inches % 12}\"" for inches in range(start_inches, end_inches + 1)]
        print(f"Height Options: {range_values}")
        return range_values

    def calculate_range_for_weight(self, average, percentage):
        start = average * (1 - percentage)
        end = average * (1 + percentage)
        range_values = [f"{lbs} lbs" for lbs in range(int(start), int(end) + 1)]
        print(f"Weight Options: {range_values}")
        return range_values

    def setup_personal_info_label(self, frame, label_text, row):
        info_label = Label(frame, text="", width=50, anchor="w")  # Width can be adjusted as needed
        Label(frame, text=label_text).grid(row=row, column=0, padx=5, pady=5)
        info_label.grid(row=row, column=1, padx=5, pady=5, sticky="W")
        return info_label

    def create_personal_section(self):
        personal_frame = Frame(self.scrollable_frame)
        personal_frame.pack(fill='x', padx=10, pady=5)

        # Metatype combobox setup
        Label(personal_frame, text="Metatype:").grid(row=0, column=0, padx=5, pady=5)
        self.metatype_combobox = ttk.Combobox(personal_frame, state="readonly", values=self.metatype_data['Metatype'])
        self.metatype_combobox.grid(row=0, column=1, padx=5, pady=5)
        self.metatype_combobox.bind("<<ComboboxSelected>>", self.update_personal_section_based_on_metatype)
        # Add the following line to also update racial qualities when a new metatype is selected
        self.metatype_combobox.bind("<<ComboboxSelected>>", self.update_racial_qualities)

        # Setup for Ears, Known for, and Description labels
        self.ears_label = self.setup_personal_info_label(personal_frame, "Ears:", 1)
        self.known_for_label = self.setup_personal_info_label(personal_frame, "Known for:", 2)
        self.description_label = self.setup_personal_info_label(personal_frame, "Description:", 3)

        # Height and Weight combobox setup
        self.height_combobox = ttk.Combobox(personal_frame, state="readonly")
        self.weight_combobox = ttk.Combobox(personal_frame, state="readonly")
        Label(personal_frame, text="Height:").grid(row=1, column=2, padx=5, pady=5)
        self.height_combobox.grid(row=1, column=3, padx=5, pady=5)
        Label(personal_frame, text="Weight:").grid(row=2, column=2, padx=5, pady=5)
        self.weight_combobox.grid(row=2, column=3, padx=5, pady=5)

    def update_personal_section_based_on_metatype(self, event=None):
        metatype_selection = self.metatype_combobox.get()
        metatype_index = self.metatype_data["Metatype"].index(metatype_selection)

        # Update Ears, Known for, and Description labels
        self.ears_label.config(text=self.metatype_data['Ears'][metatype_index])
        self.known_for_label.config(text=self.metatype_data['Known for'][metatype_index])
        self.description_label.config(text=self.metatype_data['Description'][metatype_index])

        # Update Quality labels
        for i, quality_label in enumerate(self.racial_quality_labels, start=1):
            quality_text = self.metatype_data[f"Quality #{i}"][metatype_index]
            quality_label.config(text=quality_text or "N/A")  # Use "N/A" or similar if the quality is empty

        # Update height and weight comboboxes as previously shown
        height_range = self.calculate_range_for_height(self.metatype_data['Average Height (feet)'][metatype_index], 0.1)
        weight_range = self.calculate_range_for_weight(self.metatype_data['Average Weight (pounds)'][metatype_index],
                                                       0.1)
        self.height_combobox['values'] = height_range
        self.weight_combobox['values'] = weight_range
        if height_range:
            self.height_combobox.set(height_range[0])
        if weight_range:
            self.weight_combobox.set(weight_range[0])

        # Updating attribute maximum values
        self.update_attribute_max_values(metatype_selection)
        # Update racial qualities based on the selected metatype
        self.update_racial_qualities(metatype_selection)



    def update_attribute_max_values(self, metatype):
        metatype_index = self.metatype_data["Metatype"].index(metatype)

        for attribute_name in ['Body', 'Agility', 'Reaction', 'Strength', 'Willpower', 'Logic', 'Intuition', 'Charisma',
                               'Edge']:
            max_value = self.metatype_attributes[f"{attribute_name}_max"][metatype_index]

            # Check if the attribute_label exists in the dictionary and update it
            if attribute_name in self.attribute_labels:
                self.attribute_labels[attribute_name].config(text=f"{attribute_name} (Max: {max_value})")
            else:
                print(f"Label for {attribute_name} not found")  # For debugging purposes

    def update_memo_box(self, memo_box, text):
        memo_box.config(state=NORMAL)
        memo_box.delete('1.0', END)
        memo_box.insert('1.0', text)
        memo_box.config(state=DISABLED)

    def create_attributes_section(self):
        self.attribute_labels = {}  # Initialize a dictionary to hold references to the attribute labels
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
            attribute_name = attribute_row.Attribute
            column_offset = (i % attributes_per_row) * 4  # Space for Attribute Name, -, Level, +

            attribute_name = attribute_row.Attribute
            level_var = attribute_row.LevelVar

            # Create and store a reference to the attribute label including its max value
            attribute_label = Label(attributes_frame, text=f"{attribute_name} (Max: N/A)")
            attribute_label.grid(row=row, column=column_offset, padx=5, pady=5)
            self.attribute_labels[attribute_name] = attribute_label
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

        # Adjust the key for metatype-related information if the category is 'Metatype'
        if category == "Metatype":
            category_key = 'RACES'  # Use 'RACES' as the key for metatype information
        else:
            category_key = category.upper()  # Categories in priority_dict are uppercase

        priority_values = self.priority_dict[category_key]  # Access the correct entry
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

    def update_racial_qualities(self, event=None):  # Adjusted to optionally accept an event argument
        metatype_selection = self.metatype_combobox.get()
        if metatype_selection:
            metatype_index = self.metatype_data["Metatype"].index(metatype_selection)
            racial_qualities = [
                self.metatype_data["Quality #1"][metatype_index],
                self.metatype_data["Quality #2"][metatype_index],
                self.metatype_data["Quality #3"][metatype_index],
            ]

            # Ensure you don't exceed the bounds of the racial_quality_labels list
            for i, quality in enumerate(racial_qualities):
                if i < len(self.racial_quality_labels):
                    self.racial_quality_labels[i].config(text=quality or "N/A")  # Handle empty or None quality
                else:
                    break  # Exit loop if there are more qualities than labels

    def update_quality_comboboxes(self, updated=None):
        # Gather all qualities
        positive_qualities = self.qualities[self.qualities['Type'] == 'Positive']['Quality'].tolist()
        negative_qualities = self.qualities[self.qualities['Type'] == 'Negative']['Quality'].tolist()

        # Find what's currently selected
        selected_positive = self.positive_qualities_cb.get()
        selected_negative = self.negative_qualities_cb.get()

        # Update combobox options based on what's selected
        if updated == 'positive' and selected_positive in negative_qualities:
            negative_qualities.remove(selected_positive)
        elif updated == 'negative' and selected_negative in positive_qualities:
            positive_qualities.remove(selected_negative)

        self.positive_qualities_cb['values'] = positive_qualities
        self.negative_qualities_cb['values'] = negative_qualities

        # Restore selected values if still valid
        if selected_positive in positive_qualities:
            self.positive_qualities_cb.set(selected_positive)
        if selected_negative in negative_qualities:
            self.negative_qualities_cb.set(selected_negative)

    def create_qualities_section(self):
        qualities_frame = Frame(self.scrollable_frame)
        qualities_frame.pack(pady=10, expand=True, fill="both")

        # Creating the memo box for displaying descriptions
        self.description_memo_box = Text(qualities_frame, height=10, width=50, state=DISABLED)
        self.description_memo_box.pack(side="left", padx=5)

        # Initialize comboboxes for positive and negative qualities
        self.positive_qualities_cb = ttk.Combobox(qualities_frame, state="readonly")
        self.negative_qualities_cb = ttk.Combobox(qualities_frame, state="readonly")

        # Fill comboboxes with initial values
        self.update_quality_comboboxes()

        self.positive_qualities_cb.pack(side="left", fill="y", expand=True, padx=5)
        self.negative_qualities_cb.pack(side="left", fill="y", expand=True, padx=5)

        # Bind the selection event to update available options
        self.positive_qualities_cb.bind("<<ComboboxSelected>>", lambda e: self.update_quality_comboboxes('positive'))
        self.negative_qualities_cb.bind("<<ComboboxSelected>>", lambda e: self.update_quality_comboboxes('negative'))

        # Confirm button to finalize the selection of qualities
        confirm_btn = Button(qualities_frame, text="Confirm Qualities", command=self.confirm_qualities_selection)
        confirm_btn.pack(side="left", pady=5)

        # Label to display the selected qualities and karma counter
        self.selected_qualities_label = Label(qualities_frame, text="Selected Qualities: None")
        self.selected_qualities_label.pack(side="left", pady=5)

        self.karma_counter_label = Label(qualities_frame, text=f"Karma Available: {self.karma_available}")
        self.karma_counter_label.pack(side="left", pady=5)

    def update_memo_box_with_description(self, event):
        # Fetch the widget that triggered the event
        w = event.widget
        # Determine if any item is selected
        if len(w.curselection()) > 0:
            index = int(w.curselection()[0])
            quality_name = w.get(index)
            # Fetch the description from the qualities DataFrame
            description = self.qualities.loc[self.qualities['Quality'] == quality_name, 'Description'].values[0]
            # Update the memo box with the description
            self.description_memo_box.config(state=NORMAL)
            self.description_memo_box.delete('1.0', END)
            self.description_memo_box.insert('1.0', description)
            self.description_memo_box.config(state=DISABLED)

    def confirm_qualities_selection(self):
        # Handle the logic to confirm selections and update karma.
        # This is a placeholder for the selection confirmation logic.
        # You would include here the logic for updating confirmed qualities and the karma counter,
        # similar to the outline provided in the previous instructions.

        # Example placeholder for updating the label:
        self.karma_counter_label.config(text='Karma Available: Updated Value')

        # Example for retrieving selected qualities:
        selected_positives = [self.positive_qualities_lb.get(i) for i in self.positive_qualities_lb.curselection()]
        selected_negatives = [self.negative_qualities_lb.get(i) for i in self.negative_qualities_lb.curselection()]

        # Example for updating confirmed qualities and calculating karma -- you'd replace this with your actual logic:
        print("Selected Positive Qualities:", selected_positives)
        print("Selected Negative Qualities:", selected_negatives)
        # Here, you would invoke your karma calculation method, like update_karma_available()

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
        if updated_category == "Metatype":
            self.update_metatype_options()

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

    def update_metatype_options(self):
        priority = self.comboboxes["Metatype"].get()
        if priority == "A":
            options = ['Troll', 'Ork', 'Dwarf']
        elif priority == "B":
            options = ['Ork', 'Dwarf', 'Elf']
        elif priority == "C":
            options = ['Elf', 'Dwarf', 'Human']
        elif priority == "D":
            options = ['Human', 'Dwarf']
        else:  # priority == "E"
            options = ['Human']

        self.metatype_combobox['values'] = options
        if options:
            self.metatype_combobox.set(options[0])
        else:
            self.metatype_combobox.set('')

    def update_karma_available(self):
        # Calculate the total karma cost of confirmed positive qualities
        total_positive_cost = sum(
            self.qualities.loc[self.qualities['Quality'] == q, 'Cost'].values[0] * 2
            for q in self.confirmed_positive_qualities
        )

        # Calculate the total karma gain from confirmed negative qualities, capped at 25
        total_negative_gain = sum(
            -self.qualities.loc[self.qualities['Quality'] == q, 'Cost'].values[0]
            for q in self.confirmed_negative_qualities
        )
        total_negative_gain = min(total_negative_gain, 25)  # Cap the gain at 25 karma

        # Calculate the net karma impact
        net_karma_change = total_negative_gain - total_positive_cost

        # Find the index in the DataFrame for the 'Karma' attribute
        karma_index = self.attributes_df[self.attributes_df['Attribute'] == 'Karma'].index

        # Calculate the new karma value ensuring it doesn't drop below zero
        new_karma_value = max(0, self.attributes_df.loc[karma_index, 'LevelVar'].values[0] + net_karma_change)

        # Update the DataFrame with the new karma value
        self.attributes_df.at[karma_index, 'LevelVar'].values[0] = new_karma_value

        # Print the new karma value to the terminal for verification
        print(f"Updated Karma Value: {new_karma_value}")

        # Assuming you have a label that displays the current karma, update it to reflect the new value
        self.karma_label.config(text=f"Karma: {new_karma_value}")

    # Reset any other stateful GUI elements here


# Placeholder for executing the GUI application
if __name__ == "__main__":
    root = Tk()
    app = CharacterBuilderGUI(root)
    root.mainloop()

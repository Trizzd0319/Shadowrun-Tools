import tkinter as tk
from tkinter import ttk

from SectionBase import SectionBase


class SectionSkills(SectionBase):
    def __init__(self, root, title, position, scrollable=False, **kw):
        character_profile = kw.pop('character_profile', None)
        super().__init__(root, title, position, character_profile, **kw)  # Pass character_profile here
        self.character_profile = character_profile  # Assigning the character_profile attribute

        self.skill_row_counter = 1
        self.skill_widgets = []

        self.skills_data = self.merge_skills_data()
        self.skill_vars = {}  # Dictionary to hold IntVar instances for each skill
        self.initialize_skill_vars()  # Initialize IntVars based on skills_data

        self.initialize_skills_section()

    def initialize_skill_vars(self):
        # Assuming self.skills_data is structured as {'Attribute': {'Skill': {'level': int, 'description': str}, ...}, ...}
        for attribute, skills in self.skills_data.items():
            for skill, details in skills.items():
                self.skill_vars[skill] = tk.IntVar(value=details.get('level', 0))

    def merge_skills_data(self):
        # Placeholder for logic to merge skills data from YAML and character profile
        if 'skills' in self.character_profile.character_data:
            return self.character_profile.character_data['skills']
        return {}

    def collect_data(self):
        """Collect data from the attributes section."""
        # Implementation to collect and return the section's data
        return {"attributes_data": ...}

    def initialize_skills_section(self):
        self.skills_frame = ttk.Frame(self.frame)
        self.skills_frame.grid(row=0, column=0, sticky="ew")

        self.skills_sort_combobox = ttk.Combobox(self.frame,
                                                 values=["Sort Skills by Attribute", "Sort Skills Alphabetically"],
                                                 state="readonly")
        self.skills_sort_combobox.grid(row=0, column=1, padx=5, pady=5)
        self.skills_sort_combobox.bind('<<ComboboxSelected>>', self.on_sorting_combobox_select)
        self.skills_sort_combobox.set("Sort Skills by Attribute")

        self.display_skills_by_attribute()

    def display_skills_by_attribute(self):
        self.clear_skills_section()
        row_counter = self.skill_row_counter
        for attribute, skills_dict in sorted(self.skills_data.items()):
            # Display the attribute label
            attribute_label = tk.Label(self.skills_frame, text=attribute, font=('Arial', 10, 'bold'))
            attribute_label.grid(row=row_counter, column=0, sticky="w", padx=5, pady=5)
            self.skill_widgets.append(attribute_label)
            row_counter += 1

            for skill_name, skill_details in sorted(skills_dict.items()):
                # Display the skill name and a short description
                skill_label_text = f"{skill_name} - {skill_details['Description'][:50]}..."
                skill_label = tk.Label(self.skills_frame, text=skill_label_text, anchor="w")
                skill_label.grid(row=row_counter, column=0, sticky="w", padx=5, pady=2)
                self.skill_widgets.append(skill_label)

                # Retrieve the current skill level from the character profile
                skill_level = self.character_profile.get_skill_level(skill_name)

                # Create a spinner widget linked to the skill's current level
                skill_var = tk.IntVar(value=skill_level)
                skill_spinner = tk.Spinbox(self.skills_frame, from_=0, to=6, wrap=True, width=5, textvariable=skill_var)
                skill_spinner.grid(row=row_counter, column=1, sticky="w", padx=5, pady=2)
                self.skill_widgets.append(skill_spinner)

                row_counter += 1

        self.skill_row_counter = row_counter

    def display_skills_sorted_alphabetically(self):
        self.clear_skills_section()
        # Flatten the skills data structure into a list of (skill_name, skill_var) tuples.
        # Here, we assume each skill's details are correctly stored in the character profile,
        # and we're not relying on `skills_data` for levels.
        all_skills = [(skill_name, self.skill_vars[skill_name]) for attribute, skills_dict in self.skills_data.items()
                      for skill_name in skills_dict.keys()]
        # Sort the list of tuples alphabetically by skill name.
        sorted_skills = sorted(all_skills, key=lambda x: x[0])

        row_counter = self.skill_row_counter
        for skill_name, skill_var in sorted_skills:
            # Display the skill name.
            skill_label = tk.Label(self.skills_frame, text=skill_name, anchor="w")
            skill_label.grid(row=row_counter, column=0, sticky="w", padx=5, pady=2)
            self.skill_widgets.append(skill_label)

            # Retrieve the current skill level from the character profile to set the spinner's value.
            skill_level = self.character_profile.get_skill_level(skill_name)
            skill_var.set(skill_level)  # Assuming skill_var is an IntVar associated with this skill.

            # Display the spinner linked to the skill level variable.
            skill_spinner = tk.Spinbox(self.skills_frame, from_=0, to=6, wrap=True, width=5, textvariable=skill_var)
            skill_spinner.grid(row=row_counter, column=1, sticky="w", padx=5, pady=2)
            self.skill_widgets.append(skill_spinner)

            row_counter += 1

        self.skill_row_counter = row_counter

    def update_skill_level(self, skill_name, skill_var):
        try:
            new_level = int(skill_var.get())
            self.character_profile.update_attribute(f'skills.{skill_name}.rank', new_level)
            self.character_profile.save_character_data()
        except ValueError:
            # Handle non-integer inputs
            pass

    def clear_skills_section(self):
        for widget in self.skill_widgets:
            widget.destroy()
        self.skill_widgets.clear()
        self.skill_row_counter = 1

    def on_sorting_combobox_select(self, event):
        if self.skills_sort_combobox.get() == "Sort Skills by Attribute":
            self.display_skills_by_attribute()
        else:
            self.display_skills_sorted_alphabetically()

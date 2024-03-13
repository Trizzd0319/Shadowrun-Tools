import tkinter as tk
from tkinter import ttk
import json
from tkinter import filedialog
from priority_selection_window import PrioritySelectionWindow
from metatype_selection_window import MetatypeSelectionWindow
from variables import priority_data


class CharacterCreationOptionsWindow:
    def __init__(self, parent, callback, priority_data):
        self.master = None
        self.reset_variables = None
        self.divider = None
        self.reset_button = None
        self.adjustment_points_button = None
        self.parent = parent
        self.callback = callback
        self.priority_data = priority_data
        self.ui_components = {
            "attributes": {},
            "details": {},
            "priorities": {},
            "skills": {}
        }
        self.character_configuration = {
            "priorities": {
                "A": "Filler",
                "B": "Filler",
                "C": "Filler",
                "D": "Filler",
                "E": "Filler"
            },
            "details": [
                "Metatype",
                "Level",
                "Experience",
                "Class",
                "Name",
                "Age",
                "Reputation",
                "Karma",
                "Ethnicity",
                "Height",
                "Weight",
                "Sex"
            ],
            "attributes": {
                "Strength": 0,
                "Agility": 0,
                "Body": 0,
                "Intelligence": 0,
                "Wisdom": 0,
                "Charisma": 0
            },
            "skills": [
                "Athletics",
                "Astral",
                "Biotech",
                "Close Combat",
                "Con",
                "Conjuring",
                "Cracking",
                "Electronics",
                "Engineering",
                "Exotic Weapon",
                "Firearms",
                "Influence",
                "Outdoors",
                "Perception",
                "Piloting",
                "Sorcery",
                "Stealth",
                "Tasking"
            ]
        }
        self.priority_data = {
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

        self.root = tk.Tk()
        self.root.title("Character Creation Options")
        self.priority_comboboxes = {}  # Initialize the dictionary to store comboboxes

        self.priority_selection_window = None  # Ensure this is defined here for scope visibility

        self.initialize_ui()

    def initialize_ui(self, next_row=None):
        # Priority Section Label
        self.priority_section_label = ttk.Label(self.root, text="Priority Selection")
        self.priority_section_label.grid(row=8, column=0, padx=10, pady=5, columnspan=3)

        self.divider = ttk.Separator(self.root, orient="horizontal")
        self.divider.grid(row=4, column=0, columnspan=3, sticky="ew", padx=10, pady=10)
        self.divider = ttk.Separator(self.root, orient="horizontal")
        self.divider.grid(row=9, column=0, columnspan=3, sticky="ew", padx=10, pady=10)
        self.divider = ttk.Separator(self.root, orient="horizontal")
        self.divider.grid(row=17, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

        self.buttons_frame = ttk.Frame(self.root)
        self.buttons_frame.grid(row=5, column=0, columnspan=3, padx=10, pady=10)
        self.update_combobox_options()

        button_configs = [
            ('Priority', self.open_priority_selection),
            ('Metatype', self.open_metatype_selection),
            ('Attributes', self.open_attributes_selection),
            ('Skills', self.open_skills_selection),
            ('Personal Choices', self.open_personal_selection)
        ]
        self.divider = ttk.Separator(self.root, orient="horizontal")
        self.divider.grid(row=7, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

        for i, (text, command) in enumerate(button_configs):
            self.create_button(self.buttons_frame, text, command, i // 2, i % 2)


        self.reset_button = self.create_button(self.root, "Reset", self.reset_variables, 2, 0)


        self.divider = ttk.Separator(self.root, orient="horizontal")
        self.divider.grid(row=4, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

        # Additional UI setup for sections below the divider...
        self.setup_additional_ui()
        self.setup_save_load_ui()
        self.initialize_priority_ui()
        # Create and place priority labels
        self.priority_section_label = ttk.Label(self.root, text="Priority Selection")
        self.priority_section_label.grid(row=8, column=0,padx=10, pady=10, columnspan=3)

        self.priority_section_label = ttk.Label(self.root, text="Priority Selection")
        self.priority_section_label.grid(row=8, column=0,padx=10, pady=10, columnspan=3)

    def initialize_priority_ui(self):
        priority_data = self.priority_data
        self.priority_labels = {}
        self.priority_comboboxes = {}
        priority_options = list(self.priority_data.keys())  # Assuming priority_data is accessible

        # Starting row for priority UI elements
        row_index = 10

        for priority in self.priority_data.keys():
            # Create and place a label for each priority
            label = ttk.Label(self.root, text=f"Priority {priority}:")
            label.grid(row=row_index, column=0, padx=10, pady=5)

            # Create and place a combobox for each priority
            combobox = ttk.Combobox(self.root, values=list(self.priority_data.keys()), state="readonly")
            combobox.grid(row=row_index, column=1, padx=10, pady=5, sticky="ew")
            self.priority_comboboxes[priority] = combobox

            # Increment row_index for the next priority label and combobox
            row_index += 1  # Increment row_index for the next priority label and combobox

        # Ensure that you bind an event to comboboxes if needed, for example:
        # combobox.bind("<<ComboboxSelected>>", self.on_priority_selection)

    # Example handler for combobox selection
    def update_combobox_options(self, event=None):
        selected_options = {combobox.get() for combobox in self.priority_comboboxes.values()}
        all_options = set(sum([list(options.keys()) for options in priority_data.values()], []))

        for priority, combobox in self.priority_comboboxes.items():
            current_value = combobox.get()
            available_options = list((all_options - selected_options) | {current_value})
            combobox['values'] = available_options
            if current_value not in available_options:
                combobox.set('')

    def save_configuration(self, filename):
        # Assuming character_configuration is now an attribute of the class
        with open(filename, 'w') as file:
            json.dump(self.character_configuration, file, indent=4)
        print(f"Configuration saved to {filename}")

    def load_configuration(self, filename):
        with open(filename, 'r') as file:
            self.character_configuration = json.load(file)
        print(f"Configuration loaded from {filename}")
        self.update_ui_with_loaded_configuration()  # Make sure to implement this method to update your UI based on the loaded configuration

    def setup_save_load_ui(self):
        # Example setup for Save and Load buttons
        self.save_button = self.create_button(self.root, "Save", self.save_configuration_with_dialog, 2, 1,
                                              columnspan=1)
        self.load_button = self.create_button(self.root, "Load", self.load_configuration_with_dialog, 2, 2,
                                              columnspan=1)

    def create_button(self, frame, text, command, row, column, columnspan=1):
        # Simplified button creation logic
        button = ttk.Button(frame, text=text, command=command)
        button.grid(row=row, column=column, padx=5, pady=5, sticky="ew", columnspan=columnspan)
        return button

    def update_ui_with_loaded_configuration(self):
        # Update priorities display
        priorities_text = ""
        for priority, value in self.character_configuration["priorities"].items():
            priorities_text += f"{priority}: {value}\n"
        self.priorities_display_label.config(text=priorities_text.strip())

        # Update attributes
        for attr, value in self.character_configuration["attributes"].items():
            if attr in self.ui_components["attributes"]:
                self.ui_components["attributes"][attr].set(value)  # Assuming ttk.Entry; use .set for ttk.Combobox

        # Update details - handling both Entries and Comboboxes
        for detail in self.character_configuration.get("details", []):
            if detail in self.ui_components["details"]:
                ui_element = self.ui_components["details"][detail]
                # Update the UI element with the corresponding value from the configuration
                # Adjust this part based on the type of UI element you're using
                ui_element.delete(0, tk.END)  # Clear the entry
                ui_element.insert(0, value)  # Insert the new value

    def setup_additional_ui(self):
        # priority_keys = list(priority_data['A'].keys())
        priority_values = list(priority_data['A'].values())
        self.priority_section_label = ttk.Label(self.root, text="Priority Selection")
        self.priority_section_label.grid(row=8, column=0, padx=10, pady=10, columnspan=3)
        # self.priorities_label = {}
        # # row_index = 8
        # for priority in self.character_configuration["priorities"]:
        #     label = ttk.Label(self.root, text=priority)
        #     label.grid(row=row_index, column=0, padx=10, pady=5, sticky="w")
        #     entry = ttk.Label(self.root, width=20)  # You can use Entry or any other widget you prefer
        #     entry.grid(row=row_index, column=1, padx=10, pady=5, sticky="w")
        #     self.priorities_label[priority] = entry  # Changed from detail_labels to priorities_label
        #     row_index += 1

        self.detail_label = ttk.Label(self.root, text="Character Configuration Details")
        self.detail_label.grid(row=18, column=0, padx=10, pady=10, columnspan=3)
        self.detail_label = {}
        row_index = 19
        for detail in self.character_configuration["details"]:
            label = ttk.Label(self.root, text=detail)
            label.grid(row=row_index, column=0, padx=10, pady=5, sticky="w")
            entry = ttk.Label(self.root, width=20)  # You can use Entry or any other widget you prefer
            entry.grid(row=row_index, column=1, padx=10, pady=5, sticky="w")
            self.detail_label[detail] = entry
            row_index += 1
    # Additional UI setup...

    def open_priority_selection(self):
        """
        Open the priority selection window.
        """
        if not self.priority_selection_window:
            self.priority_selection_window = PrioritySelectionWindow(self.root, self.handle_priority_selection)
        else:
            self.priority_selection_window.root.lift()

    def handle_priority_selection(self, selected_priority_options):
        """
        Handle selections from the PrioritySelectionWindow.
        """
        # Update character_configuration["priorities"] based on selected options
        self.character_configuration["priorities"] = selected_priority_options

        # Additional logic to update UI based on selected options
        self.update_priority_options(selected_priority_options)
        #  self.update_points_label(selected_priority_options)

    def update_priority_options(self, selected_priority_options):
        """
        Logic to update the main window based on selections from the PrioritySelectionWindow.
        """
        # This is just an example. You'll need to tailor it to your application.
        display_text = "\n".join(f"{priority}: {option}" for priority, option in selected_priority_options.items())
        self.priorities_display_label.config(text=display_text)

    def open_metatype_selection(self):
        def handle_metatype_selection(selected_metatype):
            print(f"Selected metatype: {selected_metatype}")  # Placeholder action
            self.character_configuration["details"]["Metatype"] = selected_metatype
            # Update UI or internal state as needed

        if not self.metatype_selection_window:
            self.metatype_selection_window = MetatypeSelectionWindow(
                self.root,
                handle_metatype_selection,
                None,  # If you have an adjustment callback, use it here
                "",  # Initial selected metatype, if any
                available_metatypes
            )
        else:
            self.metatype_selection_window.root.deiconify()

    def open_attributes_selection(self):
        # Your logic to open the attributes selection window goes here
        pass

    def open_skills_selection(self):
        # Your logic to open the attributes selection window goes here
        pass

    def open_adjustment_points(self):
        # Your logic to open the attributes selection window goes here
        pass
    def open_personal_selection(self):
        # Your logic to open the personal selection window goes here
        pass

    def save_configuration_with_dialog(self):
        filename = filedialog.asksaveasfilename(defaultextension=".json",
                                                filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if filename:
            self.save_configuration(filename)

    def load_configuration_with_dialog(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON files", "*.json"), ("All files", "*.*")])
        if filename:
            self.load_configuration(filename)

    def update_combobox_options(self, event=None):
        selected_options = set()
        for combobox in self.priority_comboboxes.values():
            selected_options.add(combobox.get())

        available_options = list(priority_data['A'].keys())

        for combobox in self.priority_comboboxes.values():
            current_value = combobox.get()
            combobox['values'] = list(available_options.union({current_value})) if current_value else list(
                available_options)
            combobox.event_generate("<<ComboboxSelected>>")

    def on_priority_selection(self, event=None):
        # Update logic based on combobox selection
        pass


# Metatype selection logic...

# Placeholder methods for attributes, skills selection, adjustment points, resetting variables, etc.

if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterCreationOptionsWindow(root, None, priority_data)
    root.mainloop()

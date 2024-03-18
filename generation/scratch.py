from tkinter import Tk, Frame, Button, Label, ttk, Canvas, Scrollbar, VERTICAL, IntVar

import pandas as pd


class CharacterBuilderGUI:
    def __init__(self, root):
        self.root = root
        self.attributes_priority_label = None
        self.skills_priority_label = None
        self.priority_dict = {
            'PRIORITY': ['A', 'B', 'C', 'D', 'E'],
            'ATTRIBUTES': [24, 16, 12, 8, 2],
            'SKILLS': [32, 24, 20, 16, 10],
            'RESOURCES': [450000, 275000, 150000, 50000, 8000],
            'MAGIC OR RESONANCE': [0, 0, 0, 0, 0]
        }
        self.create_initial_data()
        self.setup_ui()

    def create_initial_data(self):
        # Initial values for attributes (including Karma and Edge)
        initial_values = [0] * 8 + [50, 3]
        self.attributes_df = pd.DataFrame({
            'Attribute': ['Body', 'Agility', 'Reaction', 'Strength', 'Willpower', 'Logic', 'Intuition', 'Charisma',
                          'Karma', 'Edge'],
            'LevelVar': [IntVar(value=val) for val in initial_values]
        })
        self.skills_df = pd.DataFrame({
            'Skill': ["Astral (Int/Will)", "Athletics (Agi/Str)", "Biotech (Log/Int)", "Close Combat (Agi)",
                      "Con (Cha)", "Conjuring (Mag)", "Cracking (Log)", "Electronics (Log)", "Enchanting (Mag)",
                      "Engineering (Log/Int)", "Exotic Weapons (Agi)", "Firearms (Agi)", "Influence (Cha/Log)",
                      "Outdoors (Int)", "Perception (Int/Log)", "Piloting (Rea)", "Sorcery (Mag)", "Stealth (Agi)",
                      "Tasking (Res)"],
            'LevelVar': [IntVar(value=0) for _ in range(19)]
        })

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
        sections = [
            "Priority Selections", "Player Info", "Personal", "Attributes", "Skills",
            "IDs/Lifestyle/Currency", "Core Combat Info", "Qualities", "Contacts",
            "Weapons, Ranged", "Weapons, Melee", "Armor", "Augmentations", "Gear",
            "Vehicles", "Matrix Stats", "Spells / Preparations / Rituals / Complex Forms", "Adept Powers"
        ]

        for section in sections:
            if section == "Priority Selections":
                self.create_priority_selection_section()
            if section == "Player Info":
                self.create_player_info_section()
            if section == "Personal":
                self.create_personal_section()
            if section == "Attributes":
                self.create_attributes_section()
            if section == "Skills":
                self.create_skills_section()
            else:
                section_frame = Frame(self.scrollable_frame, height=50, bd=1, relief="solid")
                section_frame.pack(fill='x', padx=10, pady=5, expand=True)
                Label(section_frame, text=section, font=("Arial", 12, "bold")).pack()

    def create_priority_selection_section(self):
        priority_frame = Frame(self.scrollable_frame, bd=1, relief="solid")
        priority_frame.pack(fill='x', padx=10, pady=5, expand=True)

        priority_categories = ["Attributes", "Magic/Resonance", "Metatype", "Skills", "Resources"]

        self.priority_choices = ["A", "B", "C", "D", "E"]
        self.comboboxes = {}

        for i, category in enumerate(priority_categories):
            Label(priority_frame, text=f"{category} Priority:").grid(row=0, column=i, padx=5, pady=2)
            combobox = ttk.Combobox(priority_frame, values=self.priority_choices, state="readonly",
                                    name=f"{category.lower()}_priority_combobox")
            combobox.grid(row=1, column=i, padx=5, pady=2)
            combobox.set("Select Priority")
            combobox.bind("<<ComboboxSelected>>", self.update_comboboxes)
            self.comboboxes[category] = combobox

    def update_comboboxes(self, event):
        updated_combobox = event.widget
        updated_category = None
        for category, combobox in self.comboboxes.items():
            if combobox == updated_combobox:
                updated_category = category
                break

        current_selections = [combobox.get() for combobox in self.comboboxes.values() if
                              combobox.get() != "Select Priority"]
        available_choices = [choice for choice in self.priority_choices if choice not in current_selections]

        for combobox in self.comboboxes.values():
            current_value = combobox.get()
            combobox['values'] = ["Select Priority"] + available_choices
            if current_value in self.priority_choices:
                combobox.set(current_value)

    def get_priority_value(self, priority_level):
        if priority_level in self.priority_dict['PRIORITY']:
            index = self.priority_dict['PRIORITY'].index(priority_level)
            return self.priority_dict['ATTRIBUTES'][index]
        else:
            return None

    def save_character_data(self):
        pass

    def reset_form(self):
        pass

    def load_character_data(self):
        pass

    def create_personal_section(self):
        pass


# Placeholder for executing the GUI application
if __name__ == "__main__":
    root = Tk()
    app = CharacterBuilderGUI(root)
    root.mainloop()

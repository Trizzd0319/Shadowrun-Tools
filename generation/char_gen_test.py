# Correcting the previous code by adding pass statements in the placeholder methods to avoid syntax errors.

import tkinter as tk
from tkinter import Toplevel
from tkinter import ttk

import pandas as pd

# Create a DataFrame for the priority options
priority_data = {
    "PRIORITY": ["A", "B", "C", "D", "E"],
    "METATYPE": [
        "Dwarf, Ork, Troll (13)",
        "Dwarf, Elf, Ork, Troll (11)",
        "Dwarf, Elf, Human, Ork, Troll (9)",
        "Dwarf, Elf, Human, Ork, Troll (4)",
        "Dwarf, Elf, Human, Ork, Troll (1)"
    ],
    "ATTRIBUTES": [24, 16, 12, 8, 2],
    "SKILLS": [32, 24, 20, 16, 10],
    "MAGIC OR RESONANCE": [
        "Full: 4 Magic, Aspected: 5 Magic, Mystic Adept: 4 Magic, Adept: 4 Magic, Technomancer: 4 Resonance",
        "Full: 3 Magic, Aspected: 4 Magic, Mystic Adept: 3 Magic, Adept: 3 Magic, Technomancer: 3 Resonance",
        "Full: 2 Magic, Aspected: 3 Magic, Mystic Adept: 2 Magic, Adept: 2 Magic, Technomancer: 2 Resonance",
        "Full: 1 Magic, Aspected: 2 Magic, Mystic Adept: 1 Magic, Adept: 1 Magic, Technomancer: 1 Resonance",
        "Mundane"
    ],
    "RESOURCES": ["450,000¥", "275,000¥", "150,000¥", "50,000¥", "8,000¥"]
}
priority_df = pd.DataFrame(priority_data)

metatype_attributes_data = {
    "Metatype": ["Human", "Dwarf", "Elf", "Ork", "Troll"],
    "Body": ["1–6", "1–7", "1–6", "1–8", "1–9"],
    "Agility": ["1–6", "1–6", "1–7", "1–6", "1–5"],
    "Reaction": ["1–6", "1–5", "1–6", "1–6", "1–6"],
    "Strength": ["1–6", "1–8", "1–6", "1–8", "1–9"],
    "Willpower": ["1–6", "1–7", "1–6", "1–6", "1–6"],
    "Logic": ["1–6", "1–6", "1–6", "1–6", "1–6"],
    "Intuition": ["1–6", "1–6", "1–6", "1–6", "1–6"],
    "Charisma": ["1–6", "1–6", "1–8", "1–5", "1–5"],
    "Edge": ["1–7", "1–6", "1–6", "1–6", "1–6"],
    "Racial Qualities": [
        "None",
        "Toxin Resistance, Thermographic Vision",
        "Low-light Vision",
        "Low-light Vision, Built Tough 1",
        "Dermal Deposits, Thermographic Vision, Built Tough 2"
    ]
}

metatype_attributes_df = pd.DataFrame(metatype_attributes_data)

# Create a dictionary where each metatype's attributes and racial qualities are directly tied to the metatype key
metatype_attributes_dict = {
    metatype: {
        "Body": body,
        "Agility": agility,
        "Reaction": reaction,
        "Strength": strength,
        "Willpower": willpower,
        "Logic": logic,
        "Intuition": intuition,
        "Charisma": charisma,
        "Edge": edge,
        "Racial Qualities": racial_qualities
    } for metatype, body, agility, reaction, strength, willpower, logic, intuition, charisma, edge, racial_qualities in
    zip(
        metatype_attributes_df["Metatype"],
        metatype_attributes_df["Body"],
        metatype_attributes_df["Agility"],
        metatype_attributes_df["Reaction"],
        metatype_attributes_df["Strength"],
        metatype_attributes_df["Willpower"],
        metatype_attributes_df["Logic"],
        metatype_attributes_df["Intuition"],
        metatype_attributes_df["Charisma"],
        metatype_attributes_df["Edge"],
        metatype_attributes_df["Racial Qualities"]
    )
}


# Adjusting the ComplexGUIApp class to use labels with up/down arrows for attributes values adjustment.

# Adjusting the ComplexGUIApp class to include a scrollbar for the main content area.
# GUI Layout and Functionality
class PrioritySelectionApp:
    def __init__(self, root):
        self.root = root
        self.setup_ui()
        self.priority_df = priority_df  # Make the DataFrame accessible externally


    def setup_ui(self):
        self.root.title("Priority Selection")
        self.main_frame = tk.Frame(self.root)
        self.main_frame.pack(padx=10, pady=10)

        # Get all keys from the priority_data for combobox options, including "PRIORITY"
        self.combobox_options = sorted([key for key in priority_data.keys() if key != "PRIORITY"])

        self.comboboxes = []

        # Creating labels and comboboxes in a 2x2x1 grid layout
        for i, label_text in enumerate(["A", "B", "C", "D", "E"]):
            label = tk.Label(self.main_frame, text=f"Priority {label_text}")
            cb = ttk.Combobox(self.main_frame, textvariable=tk.StringVar(), values=self.combobox_options,
                              state="readonly")
            cb.bind("<<ComboboxSelected>>", self.update_comboboxes)
            row, column = divmod(i, 2) if i < 4 else (2, 0)

            label.grid(row=row, column=column * 2, padx=5, pady=5)
            cb.grid(row=row, column=column * 2 + 1, padx=5, pady=5)
            self.comboboxes.append(cb)

        self.reset_button = tk.Button(self.main_frame, text="Reset", command=self.reset_comboboxes)
        self.reset_button.grid(row=3, column=2, columnspan=2, pady=10)
        self.confirm_button = tk.Button(self.main_frame, text="Confirm", command=self.confirm_selections)
        self.confirm_button.grid(row=3, columnspan=3, pady=10)

    def confirm_selections(self):
        selections = {f"Label {chr(65 + i)}": cb.get() for i, cb in enumerate(self.comboboxes)}
        self.ComplexGUIApp.update_selected_section(selections)

    def update_comboboxes(self, event=None):
        selected_options = [cb.get() for cb in self.comboboxes if cb.get()]
        for cb in self.comboboxes:
            current_selection = cb.get()
            available_options = [option for option in self.combobox_options if
                                 option not in selected_options or option == current_selection]
            cb['values'] = available_options

    def reset_comboboxes(self):
        for cb in self.comboboxes:
            cb.set('')
            cb['values'] = self.combobox_options  # Reset the values to include all options

class ComplexGUIApp:
    def __init__(self, root):
        self.root = root
        self.karma_value = tk.IntVar(value=50)  # Initialize karma with 50
        self.setup_ui()
        # self.update_function = update_function  # Function to call on confirm
        self.priority_df = priority_df

    def setup_ui(self):
        self.root.title("Complex GUI Application")
        self.top_buttons_frame = tk.Frame(self.root)
        self.top_buttons_frame.pack(pady=10)
        self.create_top_buttons()
        self.create_action_buttons()
        self.main_frame = tk.Frame(self.root)
        # self.confirm_button = tk.Button(self.main_frame, text="Confirm", command=self.confirm_selections)
        # self.confirm_button.grid(row=4, columnspan=4, pady=10)
        self.main_canvas = tk.Canvas(self.root)
        self.scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.main_canvas.yview)
        self.scrollable_frame = tk.Frame(self.main_canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.main_canvas.configure(scrollregion=self.main_canvas.bbox("all"))
        )
        self.main_canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.main_canvas.configure(yscrollcommand=self.scrollbar.set)
        self.main_canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.create_sections()
        self.setup_priority_selection_button()

    def setup_priority_selection_button(self):
        self.button_priorities = tk.Button(self.root, text="Priorities", command=self.open_priority_selection)
        self.button_priorities.pack()  # Adjust layout as necessary

    def open_priority_selection(self):
        priority_window = Toplevel(self.root)
        priority_app = PrioritySelectionApp(priority_window, self)

    def update_selected_section(self, selections):
        for label_text, selection in selections.items():
            if label_text in self.selected_labels:
                self.selected_labels[label_text]['text'] = f"{label_text}: {selection}"

    def create_top_buttons(self):
        button_names = [["Priorities", "Metatype"], ["Stats", "Skills"], ["Spells", "Gear"]]
        for row in range(2):
            for col in range(3):
                if button_names[col][row] == "Priorities":
                    # If the button is for "Priorities", tie it to the open_priority_selection method
                    button = tk.Button(self.top_buttons_frame, text=button_names[col][row],
                                       command=self.open_priority_selection)
                else:
                    # For all other buttons, no specific command is tied here
                    button = tk.Button(self.top_buttons_frame, text=button_names[col][row])
                button.grid(row=row, column=col, padx=5, pady=5)

    def create_action_buttons(self):
        action_buttons_frame = tk.Frame(self.root)
        action_buttons_frame.pack(pady=5)
        action_button_names = ["Save", "Reset", "Load"]
        for index, name in enumerate(action_button_names):
            button = tk.Button(action_buttons_frame, text=name)
            button.grid(row=0, column=index, padx=5)

    def create_sections(self):
        section_labels = ["Selected Priorities", "Player Info", "Personal", "Attributes", "Skills",
                          "IDs/Lifestyle/Currency", "Core Combat Info", "Qualities", "Contacts",
                          "Weapons, Ranged", "Weapons, Melee", "Armor", "Augmentations", "Gear",
                          "Vehicles", "Matrix Stats", "Spells / Preparations / Rituals / Complex Forms",
                          "Adept Powers"]
        for index, label in enumerate(section_labels):
            section_frame = tk.Frame(self.scrollable_frame, borderwidth=1, relief=tk.SOLID)
            section_frame.pack(fill=tk.X, padx=10, pady=5)
            label_widget = tk.Label(section_frame, text=label)
            label_widget.grid(row=0, column=0, sticky=tk.W)
            button = tk.Button(section_frame, text=label)
            button.grid(row=0, column=1)
            if label == "Personal":
                self.create_personal_section(section_frame)
            if label == "Attributes":
                self.create_attributes_section(section_frame)
            if label == "Skills":
                self.create_skills_section(section_frame)
            if label == "Selected Priorities":
                self.create_selected_section(section_frame)

    def create_selected_section(self, parent):
        self.selected_labels = {}
        for i in range(10):  # Create 10 labels in a 5x2 grid
            row, col = divmod(i, 2)
            label_text = f"Label {chr(65 + i)}"  # Label A, Label B, etc.
            self.selected_labels[label_text] = tk.Label(parent, text=label_text)
            self.selected_labels[label_text].grid(row=row, column=col, padx=5, pady=5)

    def create_personal_section(self, parent):
        karma_label = tk.Label(parent, text="Karma")
        karma_label.grid(row=1, column=0, sticky=tk.W, padx=5, pady=2)
        karma_value_label = tk.Label(parent, textvariable=self.karma_value)
        karma_value_label.grid(row=1, column=1, sticky=tk.W, padx=5, pady=2)

    def increment_value(self, var):
        cost = var.get() * 5
        if self.karma_value.get() >= cost and var.get() < 6:
            var.set(var.get() + 1)
            self.karma_value.set(self.karma_value.get() - cost)

    def decrement_value(self, var):
        cost = (var.get() - 1) * 5
        if var.get() > 0:
            var.set(var.get() - 1)
            self.karma_value.set(self.karma_value.get() + cost)

    def create_attributes_section(self, parent):
        attributes = ["Body (P)", "Agility (P)", "Reaction (P)", "Strength (P)", "Willpower (M)",
                      "Logic (M)", "Intuition (M)", "Charisma (M)", "Edge (S)", "Magic (S)",
                      "Resonance (S)", "Essence (S)"]
        for row, attribute in enumerate(attributes, start=1):
            attribute_value = tk.IntVar(parent, value=0)
            label = tk.Label(parent, text=attribute)
            label.grid(row=row, column=0, sticky=tk.W, padx=5, pady=2)
            value_label = tk.Label(parent, textvariable=attribute_value)
            value_label.grid(row=row, column=1, padx=5, pady=2)
            up_button = tk.Button(parent, text="+", command=lambda var=attribute_value: self.increment_value(var))
            up_button.grid(row=row, column=2, padx=2)
            down_button = tk.Button(parent, text="-", command=lambda var=attribute_value: self.decrement_value(var))
            down_button.grid(row=row, column=3, padx=2)

    def create_skills_section(self, parent):
        skills = ["Astral (Int/Will)", "Athletics (Agi/Str)", "Biotech (Log/Int)", "Close Combat (Agi)",
                  "Con (Cha)", "Conjuring (Mag)", "Cracking (Log)", "Electronics (Log)", "Enchanting (Mag)",
                  "Engineering (Log/Int)", "Exotic Weapons (Agi)", "Firearms (Agi)", "Influence (Cha/Log)",
                  "Outdoors (Int)", "Perception (Int/Log)", "Piloting (Rea)", "Sorcery (Mag)", "Stealth (Agi)",
                  "Tasking (Res)"]
        for row, skill in enumerate(skills, start=1):
            skill_value = tk.IntVar(parent, value=0)
            skill_label = tk.Label(parent, text=skill)
            skill_label.grid(row=row, column=0, sticky=tk.W, padx=5, pady=2)
            value_label = tk.Label(parent, textvariable=skill_value)
            value_label.grid(row=row, column=1, padx=5, pady=2)
            up_button = tk.Button(parent, text="+", command=lambda var=skill_value: self.increment_value(var))
            up_button.grid(row=row, column=2, padx=2)
            down_button = tk.Button(parent, text="-", command=lambda var=skill_value: self.decrement_value(var))
            down_button.grid(row=row, column=3, padx=2)

    def increment_skill(self, var):
        if var.get() < 9:
            var.set(var.get() + 1)

    def decrement_skill(self, var):
        if var.get() > 0:
            var.set(var.get() - 1)


# Decrement function remains the same

# Uncomment to test the application
root = tk.Tk()
app = ComplexGUIApp(root)
root.mainloop()

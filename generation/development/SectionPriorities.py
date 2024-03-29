import tkinter as tk
from tkinter import ttk

import yaml

from SectionBase import SectionBase


class SectionPriorities(SectionBase):
    def __init__(self, master, title, position, character_profile, shared_data, gui_manager, **kw):
        super().__init__(master, title, position, character_profile, **kw)
        self.shared_data = shared_data
        self.gui_manager = gui_manager
        self.priority_row_counter = 1
        self.priority_widgets = []

        # Load priorities data directly from char_priorities.yaml for simplicity
        with open('variables/char_priorities.yaml', 'r') as file:
            self.char_priorities_data = yaml.safe_load(file)

        # Assuming initial_priority_values are defined as A-E
        self.initial_priority_values = ['A', 'B', 'C', 'D', 'E']
        self.comboboxes = {}  # Store category: combobox pairs

        self.initialize_priorities_section()

    def on_priority_selected(self, event, category):
        # Update shared data via GUIManager
        self.gui_manager.update_shared_data('priorities_selection', {category: self.comboboxes[category].get()})

    def initialize_priorities_section(self):
        """Initializes the priorities section with UI components."""
        self.priorities_frame = ttk.Frame(self.frame)
        self.priorities_frame.grid(row=0, column=0, sticky="ew")

        categories = sorted(['Attributes', 'Magic/Resonance', 'Skills', 'Resources', 'Metatypes'])
        row = 0
        for category in categories:
            tk.Label(self.priorities_frame, text=f"{category}:").grid(row=row, column=0, sticky="w")
            combobox = ttk.Combobox(self.priorities_frame, values=self.initial_priority_values, state="readonly")
            combobox.grid(row=row, column=1, sticky="w")
            combobox.bind('<<ComboboxSelected>>', lambda event, cat=category: self.on_priority_selected(event, cat))
            self.comboboxes[category] = combobox
            row += 1

        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset_priorities)
        self.reset_button.grid(row=row, column=0, columnspan=2)
        # Initialize the labels to display the results
        self.initialize_result_labels()

    def initialize_result_labels(self):
        """Creates labels to display the results of priority selection."""
        self.result_labels = {}
        categories = ['Attributes', 'Magic/Resonance', 'Skills', 'Resources', 'Metatypes']
        row = self.priority_row_counter + len(self.comboboxes) + 1  # Start row after the comboboxes

        for category in categories:
            result_label = tk.Label(self.priorities_frame, text="", anchor="w")
            result_label.grid(row=row, column=0, columnspan=2, sticky="w")
            self.result_labels[category] = result_label
            row += 1

    def update_priority_results(self):
        """Updates labels with the results based on the current priority selections."""
        for category, combobox in self.comboboxes.items():
            selected_priority = combobox.get()
            if selected_priority and selected_priority in self.char_priorities_data:
                # Assuming char_priorities_data structure matches your needs
                result_text = self.char_priorities_data[selected_priority].get(category, 'Not selected')
                self.result_labels[category].config(text=f"{category}: {result_text}")
            else:
                self.result_labels[category].config(text=f"{category}: Not selected")

    def has_selections(self):
        """Check if any priorities have been selected."""
        for combobox in self.comboboxes.values():
            if combobox.get():
                return True
        return False

    def on_priority_selected(self, event, category):
        # Get all currently selected priorities across comboboxes
        selected_priorities = [cb.get() for cb in self.comboboxes.values() if cb.get()]

        # Update each combobox's values excluding the selected ones
        for cat, cb in self.comboboxes.items():
            current_value = cb.get()
            available_values = [v for v in self.initial_priority_values if
                                v not in selected_priorities or v == current_value]
            cb['values'] = available_values

        self.update_priority_results()

    def reset_priorities(self):
        # Reset the combobox selections and make all priorities available again
        for combobox in self.comboboxes.values():
            combobox.set('')
            combobox['values'] = self.initial_priority_values

        # Clear the result labels
        for label in self.result_labels.values():
            label.config(text="")

        # Optionally, you might want to clear or reset any related data

    def save_priorities(self):
        """Saves the chosen priorities to the CharacterProfile."""
        # Extract priority selections from comboboxes
        selected_priorities = {category: combobox.get() for category, combobox in self.comboboxes.items()}
        # Save the selections to the character profile
        self.character_profile.update_priorities(selected_priorities)
        print("Priorities saved!")  # Feedback for successful save operation

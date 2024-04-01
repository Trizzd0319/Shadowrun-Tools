from SectionBase import SectionBase
import tkinter as tk
from tkinter import ttk


class SectionPriorities(SectionBase):
    def __init__(self, master, character_profile_manager, section_name, notify_update_callback):
        self.priority_options = ["A", "B", "C", "D", "E"]
        self.master = master
        self.comboboxes = {}
        # Assuming SectionBase now requires initializing a frame attribute for layout purposes
        self.frame = ttk.Frame(master)
        self.frame.pack(fill=tk.BOTH, expand=True)
        super().__init__(master, character_profile_manager, section_name, notify_update_callback)

    def setup_ui(self):
        # Utilize the add_widget method from SectionBase
        row = 0
        for priority_category in self.section_data.keys():
            # Proper capitalization for labels
            formatted_label = priority_category.replace("_", " ").title()
            combobox = self.add_widget("combobox", formatted_label, row, 0, values=self.priority_options)
            combobox.set(self.section_data[priority_category])

            # Store comboboxes for later reference
            self.comboboxes[priority_category] = combobox

            # Setup combobox to update character data dynamically if selections change
            combobox.bind("<<ComboboxSelected>>", self.on_combobox_selection)

            row += 1

    def update_character_data(self, priority_category):
        current_value = self.comboboxes[priority_category].get()
        self.section_data[priority_category] = current_value
        self.character_profile_manager.update_section_data(self.section_name, self.section_data)

        # Optionally call a notify update callback if provided
        if self.notify_update_callback:
            self.notify_update_callback()

    def on_combobox_selection(self, event):
        # Update character data and combobox options upon selection
        for priority_category, combobox in self.comboboxes.items():
            if combobox is event.widget:
                self.update_character_data(priority_category)
                break
        self.update_combobox_options()

    def update_combobox_options(self):
        # Ensure unique options across comboboxes
        selected_priorities = set(cb.get() for cb in self.comboboxes.values())
        for priority_category, combobox in self.comboboxes.items():
            current_value = combobox.get()
            available_options = [option for option in self.priority_options if
                                 option not in selected_priorities or option == current_value]
            combobox['values'] = available_options

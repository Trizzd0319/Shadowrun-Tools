import tkinter as tk
from tkinter import ttk

class SectionAttributes:
    def __init__(self, master, character_profile_manager, section_name="attributes", notify_update_callback=None, column_span=[0, 1]):
        self.master = master
        self.character_profile_manager = character_profile_manager
        self.section_name = section_name
        self.notify_update_callback = notify_update_callback
        self.column_span = column_span  # Defines where to place the attributes within the grid
        self.section_data = character_profile_manager.get_section_data(section_name)
        self.widgets = {}
        self.all_widgets = []  # Track all widgets for easy clearing

        self.setup_ui()

    def setup_ui(self):
        self.clear_widgets()  # Ensure a clean slate before setting up UI components

        row = 1  # Start from the first row; adjust as needed
        for category, attributes in self.section_data.items():
            if isinstance(attributes, dict):  # Check for nested attribute structure
                # Create and place a category header
                header_label = tk.Label(self.master, text=category.title(), font=("Arial", 12, "bold"))
                header_label.grid(row=row, column=self.column_span[0], columnspan=2, sticky="W", pady=(10, 5))
                self.all_widgets.append(header_label)
                row += 1

                for attribute, value in attributes.items():
                    # Generate a readable label for each attribute
                    label_text = attribute.replace("_", " ").title()
                    attribute_label = tk.Label(self.master, text=label_text)
                    attribute_label.grid(row=row, column=self.column_span[0], padx=5, pady=2, sticky="nsew")
                    self.all_widgets.append(attribute_label)

                    # Create a spinner or entry for editing attribute values
                    spinner = tk.Spinbox(self.master, from_=0, to=10)
                    spinner.delete(0, "end")
                    spinner.insert(0, str(value))
                    spinner.grid(row=row, column=self.column_span[1], padx=5, pady=2, sticky="ew")
                    self.widgets[attribute] = spinner  # Facilitate direct access to this spinner
                    self.all_widgets.append(spinner)

                    row += 1  # Prepare for the next attribute

    def clear_widgets(self):
        """Destroys all widgets in the UI to prevent duplication."""
        for widget in self.all_widgets:
            widget.destroy()
        self.all_widgets.clear()

    def refresh_ui(self):
        """Refreshes the UI, typically after data updates."""
        self.clear_widgets()
        self.setup_ui()

    def update_section_data(self):
        """Updates the section data based on UI inputs."""
        for attribute, spinner in self.widgets.items():
            try:
                # Assuming values are integers; adjust parsing as necessary for your data
                self.section_data[attribute] = int(spinner.get())
            except ValueError:
                pass  # Handle or log error as needed
        self.character_profile_manager.update_section_data(self.section_name, self.section_data)

        if self.notify_update_callback:
            self.notify_update_callback()

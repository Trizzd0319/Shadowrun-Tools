import tkinter as tk
from tkinter import ttk

class SectionSkills:
    def __init__(self, master, character_profile_manager, section_name="skills", notify_update_callback=None, column_span=[2, 3]):
        self.master = master
        self.character_profile_manager = character_profile_manager
        self.section_name = section_name
        self.notify_update_callback = notify_update_callback
        self.column_span = column_span  # Defines where to place the skills within the grid
        self.section_data = character_profile_manager.get_section_data(section_name)
        self.widgets = {}
        self.all_widgets = []  # Track all widgets for easy clearing

        self.setup_ui()

    def setup_ui(self):
        self.clear_widgets()  # Clear the existing UI components

        row = 1  # Start from the first row; adjust if necessary based on overall layout
        for skill, data in self.section_data.items():
            # Assuming 'data' could be just a value or a dict with more details
            skill_value = data if isinstance(data, int) else data.get("level", 0)

            # Generate a readable label for each skill
            skill_label = tk.Label(self.master, text=skill.replace("_", " ").title())
            skill_label.grid(row=row, column=self.column_span[0], padx=5, pady=2, sticky="nsew")
            self.all_widgets.append(skill_label)

            # Create a spinner for editing skill levels
            spinner = tk.Spinbox(self.master, from_=0, to=10, width=5)
            spinner.delete(0, "end")
            spinner.insert(0, str(skill_value))
            spinner.grid(row=row, column=self.column_span[1], padx=5, pady=2, sticky="ew")
            self.widgets[skill] = spinner  # Facilitate direct access to this spinner
            self.all_widgets.append(spinner)

            row += 1  # Move to the next skill

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
        for skill, spinner in self.widgets.items():
            try:
                # Assuming values are integers; adjust parsing as necessary for your data
                self.section_data[skill] = int(spinner.get())
            except ValueError:
                pass  # Handle or log error as needed
        self.character_profile_manager.update_section_data(self.section_name, self.section_data)

        if self.notify_update_callback:
            self.notify_update_callback()

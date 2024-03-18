import tkinter as tk
from tkinter import ttk
from priority_selection_window import PrioritySelectionWindow
from metatype_selection_window import MetatypeSelectionWindow
from variables import priority_data

class CharacterCreationOptionsWindow:
    def __init__(self, parent, callback, priority_data):
        """
        Initialize the CharacterCreationOptionsWindow.

        Args:
            parent: The parent Tkinter window.
            callback: The callback function.
            priority_data: Data related to character creation priorities.
        """
        self.parent = parent
        self.callback = callback
        self.priority_data = priority_data
        self.attribute_values = {'Strength': 1, 'Agility': 1, 'Intelligence': 1, 'Charisma': 1, 'Willpower': 1}

        self.root = tk.Tk()
        self.root.title("Character Creation Options so far")

        # Create labels and frames
        self.sections_label = ttk.Label(self.root, text="Character Creation Sections")
        self.sections_label.grid(row=0, column=0, padx=10, pady=10, columnspan=3)
        buttons_frame = ttk.Frame(self.root)
        buttons_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Configure buttons
        button_configs = [
            ('Priority', self.open_priority_selection),
            ('Metatype', self.open_metatype_selection),
            ('Attributes', self.open_attributes_selection),
            ('Skills', self.open_skills_selection)
        ]

        # Create buttons
        for i, (text, command) in enumerate(button_configs):
            button = ttk.Button(buttons_frame, text=text, command=command)
            button.grid(row=i // 2, column=i % 2, padx=5, pady=5)

        # Additional buttons and frames
        self.adjustment_points_button = ttk.Button(self.root, text="Adjustment Points",
                                                   command=self.open_adjustment_points)
        self.adjustment_points_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)
        self.reset_button = ttk.Button(self.root, text="Reset", command=self.reset_variables)
        self.reset_button.grid(row=3, column=0, columnspan=3, padx=10, pady=10)
        self.divider = ttk.Separator(self.root, orient="horizontal")
        self.divider.grid(row=4, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

        # Sections below the divider
        self.section1_frame = ttk.LabelFrame(self.root, text="Priority Selection")
        self.section1_frame.grid(row=5, column=0, padx=10, pady=10, sticky="ew", columnspan=3)
        self.section1_label = ttk.Label(self.section1_frame, text="")
        self.section1_label.pack(fill='x')

        self.section2_frame = ttk.LabelFrame(self.root, text="Metatype Selection")
        self.section2_frame.grid(row=6, column=0, padx=10, pady=10, sticky="ew", columnspan=3)
        self.section2_label = ttk.Label(self.section2_frame, text="")
        self.section2_label.pack(fill='x')

        self.section3_frame = ttk.LabelFrame(self.root, text="Attributes Selection")
        self.section3_frame.grid(row=7, column=0, padx=10, pady=10, sticky="ew", columnspan=3)
        self.points_label = ttk.Label(self.section3_frame, text="Points to Spend: ")
        self.points_label.grid(row=0, column=0, columnspan=3, pady=5)

        # Initialize window instances
        self.priority_selection_window = None
        self.metatype_selection_window = None
        self.attributes_selection_window = None
        self.skills_selection_window = None

    def open_priority_selection(self):
        """
        Open the priority selection window.
        """
        def handle_priority_selection(selected_priority_options):
            self.update_priority_options(selected_priority_options)
            self.update_points_label(selected_priority_options)
            self.generate_selected_metatype(selected_priority_options)

        if not self.priority_selection_window:
            self.priority_selection_window = PrioritySelectionWindow(self.root, handle_priority_selection)
        else:
            self.priority_selection_window.root.lift()

    def open_metatype_selection(self):
        def handle_metatype_selection(selected_metatype_options):
            self.update_metatype_options(selected_metatype_options)

        def handle_adjustment_callback(selected_metatype):
            print(f"Selected metatype: {selected_metatype}")  # Placeholder action, replace with your logic

        selected_priority_options = self.get_selected_priority_options()  # Get selected priority options directly

        self.generate_selected_metatype(selected_priority_options)  # Generate selected metatype options

        # Use the generated available races directly
        available_races = self.available_races

        if not self.metatype_selection_window:
            self.metatype_selection_window = MetatypeSelectionWindow(
                self.root, handle_metatype_selection, handle_adjustment_callback, available_races)
        else:
            self.metatype_selection_window.root.deiconify()

    def get_selected_priority_options(self):
        # Retrieve selected options from the PrioritySelectionWindow or any other source
        # For demonstration, return a sample dictionary
        return {'A': 'Attributes', 'B': 'Magic/Resonance', 'C': 'Races', 'D': 'Resources', 'E': 'Skills'}

    def open_attributes_selection(self):
        """
        Open the attributes selection window.
        """
        pass

    def open_skills_selection(self):
        """
        Open the skills selection window.
        """
        pass

    def adjust_attribute_points(self, selected_metatype, selected_ability):
        """
        Adjust attribute points based on selected metatype and ability.

        Args:
            selected_metatype: The selected metatype.
            selected_ability: The selected ability.

        Returns:
            Dictionary containing adjusted options.
        """
        adjusted_options = {
            'Attributes': {'Strength': 5, 'Agility': 5, 'Intelligence': 5, 'Charisma': 5, 'Willpower': 5}
        }
        return adjusted_options

    def open_adjustment_points(self):
        """
        Open the adjustment points window.
        """
        self.adjustment_points_window = AdjustmentPointsWindow(self.root, self.update_adjustment_options)

    def update_priority_options(self, selected_priority_options):
        """
        Update priority options.

        Args:
            selected_priority_options: Selected priority options.
        """
        section1_text = ""

        for priority, option in selected_priority_options.items():
            if option and priority in self.priority_data and option in self.priority_data[priority]:
                if isinstance(self.priority_data[priority][option], dict):
                    priority_info = self.priority_data[priority][option].get('Attributes', {})
                    for attribute, value in priority_info.items():
                        section1_text += f"{priority}: {option}: {attribute}: {value}\n"
                else:
                    section1_text += f"{priority}: {option}: {self.priority_data[priority][option]}\n"
            else:
                section1_text += f"{priority}: {option}: Invalid Option\n"

        self.section1_label.config(text=section1_text)

    def update_metatype_options(self, selected_metatype_options):
        """
        Update metatype options.

        Args:
            selected_metatype_options: Selected metatype options.
        """
        section2_text = ""

        for metatype, attributes in selected_metatype_options.items():
            section2_text += f"{metatype}\n"
            if isinstance(attributes, dict):
                for key, value in attributes.items():
                    section2_text += f"{key}: {value}\n"
            else:
                section2_text += "None\n"

        self.section2_label.config(text=section2_text)

    def update_adjustment_options(self, selected_adjustment_options):
        """
        Update adjustment options.

        Args:
            selected_adjustment_options: Selected adjustment options.
        """
        pass

    def reset_variables(self):
        """Reset all variables."""
        self.priority_selection_window = None
        self.metatype_selection_window = None
        self.attributes_selection_window = None
        self.skills_selection_window = None
        self.attribute_values = {'Strength': 1, 'Agility': 1, 'Intelligence': 1, 'Charisma': 1, 'Willpower': 1}
        self.update_priority_options({})
        self.update_metatype_options({})
        self.update_points_label()

    def update_points_label(self, selected_priority_options=None):
        """
        Update points label.

        Args:
            selected_priority_options: Selected priority options.
        """
        total_points_allocated = 0
        if selected_priority_options:
            for priority, option in selected_priority_options.items():
                if option and priority in self.priority_data and option in self.priority_data[priority]:
                    if isinstance(self.priority_data[priority][option], dict):
                        total_points_allocated += self.priority_data[priority][option].get('Attributes', {}).get(
                            'Total', 0)
                    else:
                        total_points_allocated += int(self.priority_data[priority][option])

        self.points_label.config(text=f"Points to Spend: {total_points_allocated}")

    def generate_selected_metatype(self, selected_priority_options):
        """
        Generate selected metatype.

        Args:
            selected_priority_options: Selected priority options.
        """
        races_priority = selected_priority_options.get('Races', None)
        race_availability = {
            'A': ['Dwarf', 'Ork', 'Troll'],
            'B': ['Dwarf', 'Elf', 'Ork', 'Troll'],
            'C': ['Dwarf', 'Elf', 'Human', 'Ork', 'Troll'],
            'D': ['Dwarf', 'Elf', 'Human', 'Ork', 'Troll'],
            'E': ['Dwarf', 'Elf', 'Human', 'Ork', 'Troll']
        }
        available_races = race_availability.get(races_priority, [])

if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterCreationOptionsWindow(root, None, priority_data)
    root.mainloop()

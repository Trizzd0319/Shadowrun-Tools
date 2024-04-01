import tkinter as tk
from CharacterProfileManager import CharacterProfileManager
from SectionBase import SectionBase
from SectionPriorities import SectionPriorities
from SectionPlayer import SectionPlayer

# Import other sections similarly...

class GUIManager:
    def __init__(self, root):
        self.root = root
        self.character_profile_manager = CharacterProfileManager(filepath='path_to_character_profile.yaml')
        self.sections = {}
        self.initialize_gui()

    def maximize_window(self):
        # Maximize window logic as before...
        pass

    def initialize_gui(self):
        # Define the positions and any other parameters for your sections
        section_details = {
            "Priorities": {"class": SectionPriorities, "position": (0, 0)},
            "Player Info": {"class": SectionPlayer, "position": (0, 1)},
            # "Attributes": {"class": SectionAttributes, "position": (1, 0)},
            # Continue for other sections...
        }

        # Initialize each section with necessary arguments
        for name, details in section_details.items():
            section_class = details["class"]
            position = details["position"]
            # Initialize section with character profile manager and any required data
            self.sections[name] = section_class(
                master=self.root,
                title=name,
                position=position,
                character_profile=self.character_profile_manager.get_section_data(name.lower()),
                shared_data={},  # Add shared data if necessary
                gui_manager=self  # Pass self if sections need to callback to GUIManager
            )

    def update_shared_data(self, key, value):
        # Method to update shared data between sections...
        pass

    def save_character_profile(self):
        # Method to trigger saving the character profile through CharacterProfileManager
        self.character_profile_manager.save_profile()

# Application initialization
root = tk.Tk()
app = GUIManager(root)
app.maximize_window()
root.mainloop()

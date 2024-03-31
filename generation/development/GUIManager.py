import logging
import os
import tkinter as tk
from logging.handlers import RotatingFileHandler

from SectionAttributes import SectionAttributes
from SectionCombat import SectionCombat
from SectionEquipment import SectionEquipment
from SectionMagic import SectionMagic
from SectionPersonal import SectionPersonal
from SectionPlayer import SectionPlayer
from SectionPriorities import SectionPriorities
from SectionResources import SectionResources
from SectionSkills import SectionSkills
from generation.development.CharacterProfile import CharacterProfile


def configure_root_logger():
    log_directory = "logs"
    log_filename = "application.log"
    os.makedirs(log_directory, exist_ok=True)  # Ensure the log directory exists

    log_format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    log_file_path = os.path.join(log_directory, log_filename)

    # Set up a rotating file handler to limit log file size
    rotating_handler = RotatingFileHandler(log_file_path, maxBytes=5 * 1024 * 1024, backupCount=5)
    rotating_handler.setFormatter(logging.Formatter(log_format))

    logging.basicConfig(level=logging.DEBUG, handlers=[rotating_handler])
    logging.info("Application started and logging configured")


class GUIManager:
    def __init__(self, root, character_profile):  # Add character_profile as an argument
        self.root = root
        # self.character_profile = character_profile  # Store the character profile instance
        self.character_profile = profile
        self.shared_data = {"priorities": {}}
        self.sections = {}
        #     SectionPriorities(root, "Priorities", (0, 0), character_profile=self.character_profile),
        #     SectionPlayer(root, "Player", (1, 0), character_profile=self.character_profile),
        #     SectionPersonal(root, "Personal", (2, 0), character_profile=self.character_profile),
        #     SectionResources(root, "Resources", (3, 0), character_profile=self.character_profile),
        #     SectionAttributes(root, "Attributes", (4, 0), character_profile=self.character_profile),
        #     SectionSkills(root, "Skills", (5, 0), character_profile=self.character_profile),
        #     SectionCombat(root, "Combat", (6, 0), character_profile=self.character_profile),
        #     SectionMagic(root, "Magic", (7, 0), character_profile=self.character_profile),
        #     SectionEquipment(root, "Equipment", (8, 0), character_profile=self.character_profile),
        #     # Add other sections as needed...
        # }
        self.shared_data = {
            'priorities_selection': {}
        }
        self.maximize_window()
        self.callbacks = []
        self.initialize_gui()

    def maximize_window(self):
        # Check the platform and apply the appropriate maximization method
        if self.root.tk.call('tk', 'windowingsystem') == 'win32':  # For Windows
            self.root.state('zoomed')
        elif self.root.tk.call('tk', 'windowingsystem') == 'x11':  # For Linux
            self.root.attributes('-zoomed', True)
        else:  # For macOS and other platforms as a fallback
            # Manually set the window size to the screen's resolution
            screen_width = self.root.winfo_screenwidth()
            screen_height = self.root.winfo_screenheight()
            self.root.geometry(f"{screen_width}x{screen_height}+0+0")

    def initialize_gui(self):
        # Define layout and section parameters
        layout_params = {
            "Priorities": {"position": (0, 0), "scrollable": False},
            "Player Info": {"position": (0, 1), "scrollable": False},
            "Personal": {"position": (1, 0), "scrollable": False},
            "Resources": {"position": (1, 1), "scrollable": False},
            "Attributes": {"position": (2, 0), "scrollable": False},
            "Skills": {"position": (2, 1), "scrollable": False},
            "Combat": {"position": (3, 0), "scrollable": False},
            "Magic": {"position": (3, 1), "scrollable": False},
            "Equipment": {"position": (4, 0), "scrollable": False},
        }

        # Map section names to their respective classes
        section_classes = {
            "Priorities": SectionPriorities,
            "Player Info": SectionPlayer,
            "Personal": SectionPersonal,
            "Resources": SectionResources,
            "Attributes": SectionAttributes,
            "Skills": SectionSkills,
            "Combat": SectionCombat,
            "Magic": SectionMagic,
            "Equipment": SectionEquipment,
            # Add other sections as necessary...
        }

        # Example of initialization with shared data
        self.sections["Priorities"] = SectionPriorities(self.root, "Priorities", (0, 0), self.character_profile,
                                                        shared_data=self.shared_data)
        self.sections["Skills"] = SectionSkills(self.root, "Player", (0, 1), self.character_profile,
                                                shared_data=self.shared_data)
        self.sections["Skills"] = SectionSkills(self.root, "Personal", (1, 0), self.character_profile,
                                                shared_data=self.shared_data)
        self.sections["Skills"] = SectionSkills(self.root, "Resources", (1, 1), self.character_profile,
                                                shared_data=self.shared_data)
        self.sections["Skills"] = SectionSkills(self.root, "Attributes", (2, 0), self.character_profile,
                                                shared_data=self.shared_data)
        self.sections["Skills"] = SectionSkills(self.root, "Skills", (2, 1), self.character_profile,
                                                shared_data=self.shared_data)
        self.sections["Skills"] = SectionSkills(self.root, "Combat", (3, 0), self.character_profile,
                                                shared_data=self.shared_data)
        self.sections["Skills"] = SectionSkills(self.root, "Magic", (3, 1), self.character_profile,
                                                shared_data=self.shared_data)
        self.sections["Skills"] = SectionSkills(self.root, "Equipment", (4, 0), self.character_profile,
                                                shared_data=self.shared_data)
        # Initialize other sections similarly...

        # If using callbacks, provide a way for sections to register callbacks
        self.sections["Priorities"].register_callback(self.priority_updated)

    def priority_updated(self, updated_priorities):
        # This method is called by SectionPriorities to notify about an update
        for callback in self.callbacks:
            callback(updated_priorities)

        # Directly update shared_data if not using callbacks
        self.shared_data["priorities"] = updated_priorities
        self.shared_data["priorities"] = updated_priorities
        self.shared_data["priorities"] = updated_priorities
        self.shared_data["priorities"] = updated_priorities
        self.shared_data["priorities"] = updated_priorities
        self.shared_data["priorities"] = updated_priorities
        self.shared_data["priorities"] = updated_priorities
        self.shared_data["priorities"] = updated_priorities
        self.shared_data["priorities"] = updated_priorities
        self.shared_data["priorities"] = updated_priorities

        # Notify other sections to update based on new priorities
        self.sections["Skills"].update_from_priorities(updated_priorities)

    def update_shared_data(self, key, value):
        # Update shared data structure and notify relevant sections
        self.shared_data[key] = value
        self.sections["Resources"].update_from_shared_data()

        # Iterate through each section and initialize it with the appropriate arguments
        for section_name, section_class in section_classes.items():
            # Assume all sections are positioned at (0, 0) for simplification. Adjust as necessary.
            self.sections[section_name] = section_class(
                root=self.root,
                title=section_name,  # Title is the section name
                position=(0, 0),  # Adjust the position as necessary
                character_profile=self.character_profile,  # Character profile instance
                gui_manager=self  # Pass the GUIManager instance (`self`) as the gui_manager argument
            )

    def save_character_profile(self):
        """Triggered by the 'Save' button in SectionPlayer. Collects and saves data from all sections."""
        for section_name, section_instance in self.sections.items():
            section_data = section_instance.collect_data()  # Assumes each section has a collect_data method
            self.character_profile.aggregate_section_data(section_name, section_data)
        self.character_profile.save_profile_to_file("character_profile.yaml")


# Usage:
root = tk.Tk()
# Create a single instance of CharacterProfile
profile = CharacterProfile('variables/character_profile.yaml')

app = GUIManager(root, profile)  # Pass the CharacterProfile instance to GUIManager
root.mainloop()

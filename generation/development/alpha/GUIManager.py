# GUIManager.py

import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from CharacterProfileManager import CharacterProfileManager
from SectionPriorities import SectionPriorities
from SectionAttributes import SectionAttributes
from SectionSkills import SectionSkills
import yaml


# Assuming CharacterProfileManager is already defined and available
# from CharacterProfileManager import CharacterProfileManager

# Placeholder import for SectionBase subclasses
# from SectionBase import AttributesSection, EquipmentSection, SkillsSection, etc.

# Adding File Menu to GUIManager with "New", "Save", "Load" functionality

class GUIManager:
    def __init__(self, root):
        self.root = root
        self.character_profile_manager = CharacterProfileManager()
        self.sections = {}  # Store instances of section classes

        self.setup_ui()
        self.setup_menu()

    def setup_ui(self):
        # Initialize the notebook if not already done
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both")

        # Create a frame for the 'priorities' section
        priorities_tab = ttk.Frame(self.notebook)
        self.notebook.add(priorities_tab, text='Priorities')

        # Create a frame for the 'attrtibutes' section
        attributes_tab = ttk.Frame(self.notebook)
        self.notebook.add(attributes_tab, text='Attributes & Skills')

        # Now, use 'priorities_tab' as the container for SectionPriorities
        self.sections['priorities'] = SectionPriorities(priorities_tab, self.character_profile_manager, 'priorities',
                                                        self.handle_update_from_sections)
        # Initialize SectionAttributes, placed in columns 0 and 1 of the attributes_tab
        self.sections['attributes'] = SectionAttributes(attributes_tab, self.character_profile_manager, 'attributes',
                                                        self.handle_update_from_sections, column_span=[0, 1])

        # Initialize SectionSkills, placed in columns 2 and 3 of the same attributes_tab
        self.sections['skills'] = SectionSkills(attributes_tab, self.character_profile_manager, 'skills',
                                                self.handle_update_from_sections, column_span=[2, 3])
    def setup_menu(self):
        """
        Setup the menu bar for the application, including file operations.
        """
        self.menubar = tk.Menu(self.root)
        self.root.config(menu=self.menubar)

        # File menu
        file_menu = tk.Menu(self.menubar, tearoff=0)
        file_menu.add_command(label="New", command=self.new_profile)
        file_menu.add_command(label="Save", command=self.save_profile)
        file_menu.add_command(label="Load", command=self.load_profile)
        self.menubar.add_cascade(label="File", menu=file_menu)

    def new_profile(self):
        """
        Resets the application to a new profile with default data.
        """
        self.character_profile_manager.data = self.character_profile_manager.default_character_data()
        self.reload_sections()

    def save_profile(self):
        """
        Saves the current profile data to a file.
        """
        self.character_profile_manager.save_profile()

    def load_profile(self):
        """
        Loads profile data from a file and updates the UI accordingly.
        """
        filepath = filedialog.askopenfilename()
        if filepath:
            try:
                with open(filepath, 'r') as file:
                    self.character_profile_manager.data = yaml.safe_load(file)
                self.reload_sections()
            except Exception as e:
                messagebox.showerror("Load Error", f"Failed to load profile: {e}")

    def reload_sections(self):
        """
        Reloads all sections to reflect any updates to the profile data.
        """
        for section in self.sections.values():
            section.section_data = self.character_profile_manager.get_section_data(section.section_name)
            section.setup_ui()

    def load_sections(self):
        """
        Dynamically load sections based on the character profile.
        For each section in the character profile, create a tab with the corresponding UI.
        """
        # Example sections to load. This could be dynamic based on available data.
        section_classes = {
            "Priorities": SectionPriorities,
            # "Personal": SectionPersonal,
            "Attributes": SectionAttributes,
            # More sections can be added here
        }

        for section_name, SectionClass in section_classes.items():
            tab_frame = ttk.Frame(self.notebook)
            self.notebook.add(tab_frame, text=section_name)

            # Instantiate section class for this tab
            section_instance = SectionClass(tab_frame, self.character_profile_manager, section_name.lower())
            self.sections[section_name] = section_instance

    def notify_section_updates(self):
        # Trigger updates in sections that depend on updated data
        if 'attributes' in self.sections:
            self.sections['attributes'].refresh_ui()

    def handle_update_from_sections(self):
        # Handle updates here, such as refreshing other sections
        if 'attributes' in self.sections:
            self.sections['attributes'].refresh_ui()


# Note: This implementation adds a file menu with "New", "Save", and "Load" options to the GUIManager class.
# "New" resets the character profile to its default state and updates the UI.
# "Save" saves the current state of the character profile to a file.
# "Load" allows the user to load a character profile from a file, updating the UI with the loaded data.
# Additional error handling and user feedback mechanisms may be implemented to enhance usability.


# Main application setup
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Character Profile Manager")
    root.geometry("800x600")

    app = GUIManager(root)

    root.mainloop()

# Note: The implementation of GUIManager assumes the presence of the CharacterProfileManager and specific
# subclasses of SectionBase. These elements work together to dynamically generate the UI based on the
# character profile data. Additional functionality, like saving updates back to the profile, would require
# further implementation detail in both the GUI elements and the interaction with the CharacterProfileManager.

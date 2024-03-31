from Section import Section
from SectionBase import SectionBase
from SectionPriorities import SectionPriorities
from SectionPlayer import SectionPlayer
import tkinter as tk

class GUIManager:
    def __init__(self, root):
        self.root = root
        self.sections = {}
        self.initialize_gui()

    def initialize_gui(self):
        # Mapping of section identifiers to their corresponding classes
        layout_params = {
            "Priorities": {"row": 0, "column": 0, "scrollable": False, "position": (0, 0)},
            "Player Info": {"row": 0, "column": 1, "scrollable": False, "position": (0, 1)},
            # "Personal": {"row": 1, "column": 0, "scrollable": False, "position": (0, 1)},
            # "Resources": {"row": 1, "column": 1, "scrollable": False, "position": (1, 1)},
            # "Attributes": {"row": 2, "column": 0, "scrollable": False, "position": (2, 0)},
            # "Skills": {"row": 2, "column": 1, "scrollable": False, "position": (2, 1)},
            # "Combat": {"row": 3, "column": 0, "scrollable": False, "position": (3, 0)},
            # "Magic": {"row": 3, "column": 1, "scrollable": False, "position": (3, 1)},
            # "Equipment": {"row": 4, "column": 0, "scrollable": False, "position": (4, 0)},
            # Add layout params for other sections...
        }
        section_classes = {
            "Priorities": SectionPriorities,
            "Player Info": SectionPlayer,
            # "Personal": sectionPersonal,
            # "Resources": sectionResources,
            # "Attributes": SectionAttributes,
            # "Skills": SectionSkills,
            # "Combat": sectionCombat,
            # "Magic": sectionMagic,
            # "Equipment": sectionEquipment
            # Add mappings for other sections...
        }

        # Dynamically create and store instances of section classes
        for section_name, SectionClass in section_classes.items():
            params = layout_params.get(section_name, {})
            self.sections[section_name] = SectionClass(self.root, title=section_name, **params)
            # 'row', 'column', and 'scrollable' would be determined based on the specific layout you're aiming for.


# Usage:
root = tk.Tk()
app = GUIManager(root)
root.mainloop()

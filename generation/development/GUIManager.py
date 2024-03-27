from sectionBase import SectionBase
from sectionPriorities import sectionPriorities
from sectionPlayer import sectionPlayer
from sectionPersonal import sectionPersonal
from sectionAttributes import SectionAttributes
from sectionSkills import SectionSkills
from sectionCombat import sectionCombat
from sectionResources import sectionResources
from sectionMagic import sectionMagic
from sectionEquipment import sectionEquipment
import tkinter as tk
class GUIManager:
    def __init__(self, root):
        self.root = root
        self.sections = {}
        self.initialize_gui()

    def initialize_gui(self):
        # Mapping of section identifiers to their corresponding classes
        layout_params = {
            "Priorities": {"row": 0, "column": 0, "scrollable": False},
            "Player Info": {"row": 0, "column": 1, "scrollable": False},
            "Personal": {"row": 1, "column": 0, "scrollable": False},
            "Resources": {"row": 1, "column": 1, "scrollable": False},
            "Attributes": {"row": 2, "column": 0, "scrollable": False},
            "Skills": {"row": 2, "column": 1, "scrollable": False},
            "Combat": {"row": 3, "column": 0, "scrollable": False},
            "Magic": {"row": 3, "column": 1, "scrollable": False},
            "Equipment": {"row": 4, "column": 0, "scrollable": False},
            # Add layout params for other sections...
        }
        section_classes = {
            "Priorities": sectionPriorities,
            "Player Info": sectionPlayer,
            "Personal": sectionPersonal,
            "Resources": sectionResources,
            "Attributes": SectionAttributes,
            "Skills": SectionSkills,
            "Combat": sectionCombat,
            "Magic": sectionMagic,
            "Equipment": sectionEquipment
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
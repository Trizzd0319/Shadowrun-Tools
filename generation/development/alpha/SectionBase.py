# SectionBase.py
from tkinter import ttk
import tkinter as tk


class SectionBase:
    """
    A base class for GUI sections in the character profile management system.
    This class will be subclassed for specific sections of the character profile, such as attributes or equipment.
    """

    def __init__(self, master, character_profile_manager, section_name, notify_update_callback):
        """
        Initialize the section base.

        :param master: The tkinter parent widget.
        :param character_profile_manager: Instance of CharacterProfileManager to load and update character data.
        :param section_name: The name of the section in the character profile this class represents.
        """
        self.master = master
        self.character_profile_manager = character_profile_manager
        self.section_name = section_name
        self.section_data = character_profile_manager.get_section_data(section_name)
        self.notify_update_callback = notify_update_callback
        self.widgets = {}
        self.all_widgets = []
        self.bindings = []
        self.initialize_section = {}

        self.setup_ui()

    def setup_ui(self):
        """
        Setup the UI for the section. To be implemented by subclasses.
        """
        raise NotImplementedError("Subclasses must implement setup_ui.")

    def update_section_data(self):
        """
        Update the section data in the character profile manager.
        """
        self.character_profile_manager.update_section_data(self.section_name, self.section_data)

    def add_widget(self, widget_type, label_text, row, column=0, **options):
        label = ttk.Label(self.frame, text=label_text)
        label.grid(row=row, column=column * 2, padx=5, pady=2, sticky="nsew")

        widget = None
        if widget_type == "entry":
            widget = ttk.Entry(self.frame, **options)
        elif widget_type == "combobox":
            widget = ttk.Combobox(self.frame, **options)
        elif widget_type == "spinner":
            widget = tk.Spinbox(self.frame, **options)
        elif widget_type == "label":
            widget = ttk.Label(self.frame, **options)
        elif widget_type == "checkbox":
            var = tk.BooleanVar(self.frame)
            widget = tk.Checkbutton(self.frame, text=label_text, variable=var, **options)
            self.widgets[label_text] = {'widget': widget, 'variable': var}
        else:
            raise ValueError("Unsupported widget type")

        if widget_type != "checkbox":
            widget.grid(row=row, column=column * 2 + 1, padx=5, pady=2, sticky="ew")
            self.widgets[label_text] = widget

        self.all_widgets.append(widget)
        return widget

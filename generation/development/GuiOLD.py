from Section import Section
from tkinter import Tk, Frame, Button, Label, Entry, ttk, Canvas, Scrollbar, VERTICAL, IntVar, filedialog, Text, NORMAL, \
    END, DISABLED, Listbox, WORD, messagebox
from Logic import priorities_combo_selection, update_personal_metatype
from generation.development import information, Logic
from information import *
import tkinter as tk
from Logic import update_priorities_options


class GUIManager:
    def __init__(self, root):
        self.root = root
        self.sections = {}
        self.combobox_references = {}
        self.personal_metatype = {}  # Add this line
        self.skills_widgets = []  # To track skill-related widgets for easy clearing
        self.skills_sort_combobox = ttk.Combobox(self.root,
                                                 values=["Sort Skills by Attribute", "Sort Skills Alphabetically"],
                                                 state="readonly")
        self.skills_sort_combobox.grid(row=0, column=0, padx=5, pady=5)  # Adjust grid placement as necessary
        self.skills_sort_combobox.bind('<<ComboboxSelected>>', self.on_sorting_combobox_select)
        self.skills_sort_combobox.set("Sort Skills by Attribute")  # Default sorting method

        self.initialize_gui()

    def clear_skills_section(self):
        for widget in self.skills_widgets:
            widget.destroy()
        self.skills_widgets.clear()

    def priorities_combobox_select(self, event, selected_priority, selected_combobox):
        # Update combobox options, passing the selected combobox reference
        update_priorities_options(selected_priority, selected_combobox, self.combobox_references)

    # def on_sorting_combobox_select(self, event):
    #     sort_option = self.skills_sort_combobox.get()
    #
    #     if sort_option == "Sort Skills by Attribute":
    #         sorted_skills = sorted(skills.items(), key=lambda x: (x[1]["Linked Attribute, Primary"], x[0]))
    #     else:
    #         sorted_skills = sorted(skills.items(), key=lambda x: x[0])
    #
    #     self.update_skills_section(sorted_skills)
    #
    # def group_skills_by_attribute(self, skills):
    #     grouped_skills = {}
    #     for skill_name, skill_info in skills.items():
    #         attribute = skill_info["Linked Attribute, Primary"]
    #         if attribute not in grouped_skills:
    #             grouped_skills[attribute] = []
    #         grouped_skills[attribute].append((skill_name, skill_info))
    #     return grouped_skills
    #
    # def display_skills_sorted_by_attribute(self):
    #     specific_attributes = ["Body", "Agility", "Reaction", "Strength"]
    #     grouped_skills = self.group_skills_by_attribute(skills)
    #
    #     self.clear_skills_section()  # Clear existing widgets
    #     self.skills_row_counter = 1  # Reset the row counter for skills section
    #
    #     for attribute in specific_attributes:
    #         skill_list = grouped_skills.get(attribute, [])
    #
    #         # Check if there are any skills for the current attribute
    #         if skill_list:
    #             # Display the attribute name as a header
    #             header_label = tk.Label(self.sections["Skills"].frame, text=f"{attribute} Skills",
    #                                     font=('Arial', 10, 'bold'))
    #             header_label.grid(row=self.skills_row_counter, column=0, columnspan=2, sticky="w", padx=5, pady=5)
    #             self.skills_widgets.append(header_label)
    #             self.skills_row_counter += 1
    #
    #             # Sort skills within this attribute group alphabetically
    #             for skill_name, skill_info in sorted(skill_list, key=lambda x: x[0]):
    #                 self.display_skill(skill_name, skill_info)
    #
    # def display_skill(self, skill_name, skill_info):
    #     # Display skill name
    #     skill_label = tk.Label(self.sections["Skills"].frame, text=skill_name)
    #     skill_label.grid(row=self.skills_row_counter, column=0, sticky="w", padx=5, pady=2)
    #     self.skills_widgets.append(skill_label)
    #
    #     # Display a spinbox for the skill level next to the skill name
    #     skill_level_spinbox = tk.Spinbox(self.sections["Skills"].frame, from_=0, to=6, wrap=True, width=3)
    #     skill_level_spinbox.grid(row=self.skills_row_counter, column=1, sticky="w", padx=5, pady=2)
    #     self.skills_widgets.append(skill_level_spinbox)
    #
    #     self.skills_row_counter += 1  # Increment for the next skill
    #
    # def display_skills_sorted_alphabetically(self):
    #     # Sorting skills alphabetically by name
    #     sorted_skills = sorted(skills.items(), key=lambda x: x[0])
    #     self.update_skills_section(sorted_skills)
    #
    # def update_skills_section(self, sorted_skills):
    #     self.clear_skills_section()  # Clear existing widgets
    #     self.skills_row_counter = 1  # Assuming the first row is used for the sorting combobox
    #
    #     for skill_name, skill_info in sorted_skills:
    #         # Create a label for the skill name
    #         skill_label = tk.Label(self.sections["Skills"].frame, text=skill_name)
    #         skill_label.grid(row=self.skills_row_counter, column=0, sticky="w", padx=5, pady=2)
    #         self.skills_widgets.append(skill_label)  # Add to the widget tracking list
    #
    #         # Replace the info label with a spinbox for setting the skill level
    #         skill_level_spinbox = tk.Spinbox(self.sections["Skills"].frame, from_=0, to=6, wrap=True, width=3)
    #         skill_level_spinbox.grid(row=self.skills_row_counter, column=1, sticky="w", padx=5, pady=2)
    #         self.skills_widgets.append(skill_level_spinbox)  # Add to the widget tracking list
    #
    #         self.skills_row_counter += 1  # Increment for the next skill

    def initialize_gui(self):
        # Define your sections here
        sections = [
            "Priorities", "Player Info",
            "Personal", "Lifestyle",
            "Attributes", "Skills",
            "Qualities", "Contacts",
            "Core Combat Info", "Gear",
            "Matrix Stats", "Spells"
        ]
        priorities_section = Section(self.root, "Priorities", row=1, column=0, scrollable=False)
        self.sections["Priorities"] = Section(self.root, "Priorities", 1, 0, scrollable=False)
        self.sections["Player Info"] = Section(self.root, "Player Info", 1, 1, scrollable=False)
        self.sections["Personal"] = Section(self.root, "Personal", 2, 0, scrollable=False)
        self.sections["Lifestyle"] = Section(self.root, "Lifestyle", 2, 1, scrollable=False)
        self.sections["Attributes"] = Section(self.root, "Attributes", 3, 0, scrollable=True)
        self.sections["Skills"] = Section(self.root, "Skills", 3, 1, scrollable=True)
        self.sections["Qualities"] = Section(self.root, "Qualities", 4, 0, scrollable=True)
        self.sections["Contacts"] = Section(self.root, "Contacts", 4, 1, scrollable=False)
        self.sections["Core Combat Info"] = Section(self.root, "Core Combat Info", 5, 0, scrollable=True)
        self.sections["Gear"] = Section(self.root, "Gear", 5, 1, scrollable=True)

        self.combobox_references = {}  # To store combobox widgets
        self.label_references = {}  # To store label widgets for displaying selections
        # Assign and Create Comboboxes for Priorities and Labels to show the value associated with that Priority
        priorities = ["Attributes", "Magic", "Metatype", "Resources", "Skills"]
        for i, priority in enumerate(priorities):
            combobox = self.sections["Priorities"].add_widget(
                "combobox",
                priority,
                row=i + 1,
                column=0,
                values=['A', 'B', 'C', 'D', 'E']
            )
            self.combobox_references[priority] = combobox
            # Bind the combobox selection event to the update logic
            combobox.bind('<<ComboboxSelected>>',
                          lambda event, p=priority, cb=combobox: self.priorities_combobox_select(event, p, cb))

            # Example: Access the combobox for the "Attributes" priority
            # attributes_combobox = self.combobox_references["Attributes"]
            # To Bind events to these comboboxes, or others created similarly, see below:
            # for priority, combobox in self.combobox_references.items():
            #     combobox.bind('<<ComboboxSelected>>', lambda e, p=priority: self.on_combobox_select(e, p))
            # Add a label for the priority next to its combobox
            self.label_references[priority] = self.sections["Priorities"].add_widget("label", "Not Set Yet", row=i + 1,
                                                                                     column=1)
        # Assign Player Name to Player Section
        player = ["Name"]
        for i, name in enumerate(player):
            self.sections["Player Info"].add_widget("entry", name, row=i + 1)

        # Assign Personal Choices relevant for character creation
        self.sections["Personal"].add_widget("entry", "Name", 1, 0)
        self.personal_metatype = self.sections["Personal"].add_widget("combobox", "Test", 2, 0)
        # Example of how to reference the personal_metatype for usage and reference later
        # personal_metatype['values'] = ['Human', 'Elf']

        # In GuiOLD.py, where you set up the binding:
        # Inside your GUIManager class in GuiOLD.py
        # After initializing all comboboxes and personal_metatype
        for category, combobox in self.combobox_references.items():
            if category == "Metatype":
                # Bind the metatype ComboBox to use the new function
                combobox.bind('<<ComboboxSelected>>',
                              lambda event, p=category: update_personal_metatype(
                                  event.widget.get(), self.personal_metatype, priority_data))
            else:
                # Other ComboBoxes continue to use the existing priorities_combo_selection function
                combobox.bind('<<ComboboxSelected>>',
                              lambda event, cat=category: priorities_combo_selection(
                                  event, cat, self.label_references, self.combobox_references, priority_data,
                                  self.personal_metatype))

        column = 0  # All elements in the same column
        row = 0  # Initialize row to start at the top of the column

        # Process each category and its attributes
        for category, attrs in attributes_upgradable.items():
            # Create a category label
            category_label = self.sections["Attributes"].add_widget("label", category, row=row, column=column)
            row += 1  # Move to the next row for the first attribute in this category

            # Iterate over attributes within the current category
            for attribute in attrs:
                # Create a label for the attribute
                # attribute_label = self.sections["Attributes"].add_widget("label", attribute, row=row, column=column)
                row += 1  # Move to the next row for the spinner

                # Create a spinner for the attribute, placed under its label
                attribute_spinner = self.sections["Attributes"].add_widget("spinner", attribute, row=row, column=column)
                row += 1  # Increment row for the next attribute or category label

        # self.skills_sort_combobox = self.sections["Skills"].add_widget("combobox", "Skills Sort", 0, 0, values=
        # ["Sort Skills by Attribute", "Sort Skills Alphabetically"])
        # self.skills_sort_combobox.set("Sort Skills by Attribute")  # Set default sorting
        # self.skills_sort_combobox.bind('<<ComboboxSelected>>', self.on_sorting_combobox_select)

    def adjust_widget_widths(self):
        max_widths = {}

        # First, determine the maximum width needed for each column
        for widget, column in self.all_widgets:
            widget.update_idletasks()  # Ensure widget sizes are updated
            width = widget.winfo_reqwidth()
            if column not in max_widths or width > max_widths[column]:
                max_widths[column] = width

        # Then, adjust the width of all widgets in each column
        for widget, column in self.all_widgets:
            # For Labels, use 'width' option; calculate approx. characters needed
            if isinstance(widget, tk.Label):
                text_length = len(widget.cget("text"))
                # Assuming a monospace font or aiming for an approximation
                widget.config(width=max(max_widths[column] // 8, text_length))
            # For Entries, adjusting 'width' directly works as it's character count
            elif isinstance(widget, tk.Entry):
                widget.config(width=max_widths[column] // 8)  # Adjust division factor as needed based on your font


if __name__ == "__main__":
    root = Tk()
    app = GUIManager(root)
    root.mainloop()

import tkinter as tk
from tkinter import ttk
from sectionBase import SectionBase

class SectionSkills(SectionBase):
    def __init__(self, root, title, row, column, skills_data):
        super().__init__(root, title, row, column, scrollable=True)
        self.skills_data = skills_data
        self.initialize_skills_section()

    def initialize_skills_section(self):
        self.skills_widgets = []
        self.skills_row_counter = 1

        self.skills_sort_combobox = ttk.Combobox(self.frame,
                                                 values=["Sort Skills by Attribute", "Sort Skills Alphabetically"],
                                                 state="readonly")
        self.skills_sort_combobox.grid(row=0, column=0, padx=5, pady=5)
        self.skills_sort_combobox.bind('<<ComboboxSelected>>', self.on_sorting_combobox_select)
        self.skills_sort_combobox.set("Sort Skills by Attribute")
        self.display_skills_sorted_by_attribute()

    def clear_skills_section(self):
        for widget in self.skills_widgets:
            widget.destroy()
        self.skills_widgets.clear()
        self.skills_row_counter = 1

    def on_sorting_combobox_select(self, event):
        sort_option = self.skills_sort_combobox.get()
        if sort_option == "Sort Skills by Attribute":
            self.display_skills_sorted_by_attribute()
        else:
            self.display_skills_sorted_alphabetically()

    def group_skills_by_attribute(self):
        grouped_skills = {}
        for skill_name, skill_info in self.skills_data.items():
            primary_attr = skill_info.get("Linked Attribute, Primary", "")
            secondary_attr = skill_info.get("Linked Attribute, Secondary", "")
            attr_key = (primary_attr, secondary_attr)
            grouped_skills.setdefault(attr_key, []).append((skill_name, skill_info))
        return grouped_skills

    def display_skills_sorted_by_attribute(self):
        grouped_skills = self.group_skills_by_attribute()
        self.clear_skills_section()

        for attrs, skills in sorted(grouped_skills.items(), key=lambda x: (x[0][0], x[0][1])):
            primary_attr, secondary_attr = attrs
            attr_label = f"{primary_attr} Skills"
            if secondary_attr:
                attr_label += f" / {secondary_attr}"
            header_label = tk.Label(self.frame, text=attr_label, font=('Arial', 10, 'bold'))
            header_label.grid(row=self.skills_row_counter, column=0, columnspan=2, sticky="w", padx=5, pady=5)
            self.skills_row_counter += 1

            for skill_name, skill_info in sorted(skills, key=lambda x: x[0]):
                self.display_skill(skill_name, skill_info)

    def display_skills_sorted_alphabetically(self):
        self.clear_skills_section()

        for skill_name, skill_info in sorted(self.skills_data.items(), key=lambda x: x[0]):
            self.display_skill(skill_name, skill_info)

    def display_skill(self, skill_name, skill_info):
        skill_label = tk.Label(self.frame, text=skill_name, anchor="w")
        skill_label.grid(row=self.skills_row_counter, column=0, sticky="w", padx=5, pady=2)
        self.skills_row_counter += 1

        skill_level_spinbox = tk.Spinbox(self.frame, from_=0, to=6, wrap=True, width=5)
        skill_level_spinbox.grid(row=self.skills_row_counter - 1, column=1, sticky="w", padx=5, pady=2)

        self.skills_widgets.extend([skill_label, skill_level_spinbox])

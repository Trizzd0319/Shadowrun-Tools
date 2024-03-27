import tkinter as tk
from tkinter import ttk
from generation.development.sectionBase import SectionBase

class SectionAttributes(SectionBase):
    def __init__(self, root, attributes_data):
        super().__init__(root, "Attributes", row=3, column=0, scrollable=True)
        self.attributes_data = attributes_data
        self.initialize_attributes_section()

    def initialize_attributes_section(self):
        self.attribute_widgets = []
        self.attribute_row_counter = 1

        self.attributes_sort_combobox = ttk.Combobox(self.frame,
                                                     values=["Sort Attributes by Category", "Sort Attributes Alphabetically"],
                                                     state="readonly")
        self.attributes_sort_combobox.grid(row=0, column=0, padx=5, pady=5)
        self.attributes_sort_combobox.bind('<<ComboboxSelected>>', self.on_sorting_combobox_select)
        self.attributes_sort_combobox.set("Sort Attributes by Category")

        self.display_attributes_sorted_by_category()

    def clear_attributes_section(self):
        for widget in self.attribute_widgets:
            widget.destroy()
        self.attribute_widgets.clear()

    def on_sorting_combobox_select(self, event):
        sort_option = self.attributes_sort_combobox.get()
        if sort_option == "Sort Attributes by Category":
            self.display_attributes_sorted_by_category()
        else:
            self.display_attributes_sorted_alphabetically()

    def display_attributes_sorted_by_category(self):
        self.clear_attributes_section()
        for category, attrs in sorted(self.attributes_data.items()):
            category_label = tk.Label(self.frame, text=category, font=('Arial', 10, 'bold'))
            category_label.grid(row=self.attribute_row_counter, column=0, columnspan=2, sticky="w", padx=5, pady=5)
            self.attribute_row_counter += 1
            for attribute in sorted(attrs):
                attribute_spinner = tk.Spinbox(self.frame, from_=0, to=6, wrap=True, width=5)
                attribute_spinner.grid(row=self.attribute_row_counter, column=0, sticky="w", padx=5, pady=2)
                self.attribute_widgets.append(attribute_spinner)
                attribute_label = tk.Label(self.frame, text=attribute, anchor="w")
                attribute_label.grid(row=self.attribute_row_counter, column=1, sticky="w", padx=5, pady=2)
                self.attribute_widgets.append(attribute_label)
                self.attribute_row_counter += 1

    def display_attributes_sorted_alphabetically(self):
        self.clear_attributes_section()
        sorted_attrs = sorted((attr, category) for category, attrs in self.attributes_data.items() for attr in attrs)
        for attr, category in sorted_attrs:
            attribute_spinner = tk.Spinbox(self.frame, from_=0, to=6, wrap=True, width=5)
            attribute_spinner.grid(row=self.attribute_row_counter, column=0, sticky="w", padx=5, pady=2)
            self.attribute_widgets.append(attribute_spinner)
            attribute_label = tk.Label(self.frame, text=attr, anchor="w")
            attribute_label.grid(row=self.attribute_row_counter, column=1, sticky="w", padx=5, pady=2)
            self.attribute_widgets.append(attribute_label)
            self.attribute_row_counter += 1

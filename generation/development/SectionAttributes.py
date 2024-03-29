import tkinter as tk
from tkinter import ttk

from SectionBase import SectionBase


class SectionAttributes(SectionBase):
    def __init__(self, root, title, position, scrollable=False, **kw):
        character_profile = kw.pop('character_profile', None)
        super().__init__(root, title, position, character_profile, **kw)  # Pass character_profile here
        self.attribute_row_counter = 1
        self.attribute_widgets = []

        self.attributes_data = self.merge_attributes_data()
        self.attribute_vars = {}  # Dictionary to hold IntVar instances for each attribute
        self.initialize_attribute_vars()  # Initialize IntVars based on attributes_data

        self.initialize_attributes_section()

    def initialize_attribute_vars(self):
        # Assuming self.attributes_data is structured as {'Category': {'Attribute': level, ...}, ...}
        for category, attributes in self.attributes_data.items():
            if isinstance(attributes, dict):  # Make sure 'attributes' is a dictionary before iterating
                for attribute, level in attributes.items():
                    self.attribute_vars[attribute] = tk.IntVar(value=level)
            else:
                # Handle the case where 'attributes' is directly an integer (or another non-dict value)
                print(f"Expected a dict for attributes in category '{category}', got: {type(attributes)}")

    def merge_attributes_data(self):
        # Placeholder for logic to merge attribute data from YAML and character profile
        if 'attributes' in self.character_profile.character_data:
            return self.character_profile.character_data['attributes']
        return {}

    def initialize_attributes_section(self):
        self.attributes_frame = ttk.Frame(self.frame)
        self.attributes_frame.grid(row=0, column=0, sticky="ew")

        self.attributes_sort_combobox = ttk.Combobox(self.frame,
                                                     values=["Sort Attributes by Category",
                                                             "Sort Attributes Alphabetically"],
                                                     state="readonly")
        self.attributes_sort_combobox.grid(row=0, column=1, padx=5, pady=5)
        self.attributes_sort_combobox.bind('<<ComboboxSelected>>', self.on_sorting_combobox_select)
        self.attributes_sort_combobox.set("Sort Attributes by Category")

        self.display_attributes_by_category()

    def display_attributes_by_category(self):
        self.clear_attributes_section()
        row_counter = 1
        for category, attributes in sorted(self.attributes_data.items()):
            category_label = tk.Label(self.attributes_frame, text=category, font=('Arial', 10, 'bold'))
            category_label.grid(row=row_counter, column=0, sticky="w", padx=5, pady=5)
            self.attribute_widgets.append(category_label)
            row_counter += 1

            if isinstance(attributes, dict):
                for attribute_name in sorted(attributes.keys()):
                    attribute_level = attributes[attribute_name]

                    attribute_label = tk.Label(self.attributes_frame, text=attribute_name, anchor="w")
                    attribute_label.grid(row=row_counter, column=0, sticky="w", padx=5, pady=2)
                    self.attribute_widgets.append(attribute_label)

                    attribute_spinner = tk.Spinbox(self.attributes_frame, from_=0, to=6, wrap=True, width=5,
                                                   textvariable=tk.StringVar(value=attribute_level))
                    attribute_spinner.grid(row=row_counter, column=1, sticky="w", padx=5, pady=2)
                    self.attribute_widgets.append(attribute_spinner)
                    # Bind a callback function to the spinbox widget to update the value in character_profile.character_data
                    attribute_spinner.bind('<FocusOut>',
                                           lambda event, attr_name=attribute_name, attr_level=attribute_level:
                                           self.update_attribute_level(attr_name, attr_level))

                    row_counter += 1
            else:
                # Handle the case where 'attributes' is directly an integer
                # You can choose to display this differently or skip it
                print(f"Category '{category}' directly contains a non-dict value: {attributes}")

    def flatten_attributes_for_display(self, attributes_data):
        flattened_attributes = []
        for category, attrs in attributes_data.items():
            if isinstance(attrs, dict):
                for attr_name, level in attrs.items():
                    flattened_attributes.append((f"{attr_name} ({category})", level))
            else:
                flattened_attributes.append((category, attrs))
        return sorted(flattened_attributes, key=lambda x: x[0])

    def display_attributes_sorted_alphabetically(self):
        self.clear_attributes_section()
        flattened_attributes = self.flatten_attributes_for_display(self.attributes_data)  # Correctly call the method
        row_counter = 1
        for attribute_name, level in flattened_attributes:  # Directly use the flattened list
            # Retrieve the level directly from character_profile.character_data['attributes']
            attribute_level = self.character_profile.character_data['attributes'].get(attribute_name, level)

            attribute_label = tk.Label(self.attributes_frame, text=attribute_name, anchor="w")
            attribute_label.grid(row=row_counter, column=0, sticky="w", padx=5, pady=2)
            self.attribute_widgets.append(attribute_label)

            attribute_var = tk.StringVar(value=str(attribute_level))  # Use a StringVar to bind to the Spinbox
            attribute_spinner = tk.Spinbox(self.attributes_frame, from_=0, to=6, wrap=True, width=5,
                                           textvariable=attribute_var)
            attribute_spinner.grid(row=row_counter, column=1, sticky="w", padx=5, pady=2)
            self.attribute_widgets.append(attribute_spinner)

            attribute_spinner.bind('<FocusOut>',
                                   lambda event, attr_name=attribute_name, attr_level=attribute_level:
                                   self.update_attribute_level(attr_name, attr_level))

            row_counter += 1

        self.attribute_row_counter = row_counter

    def collect_data(self):
        """Collect data from the attributes section."""
        # Implementation to collect and return the section's data
        return {"attributes_data": ...}

    def clear_attributes_section(self):
        for widget in self.attribute_widgets:
            widget.destroy()
        self.attribute_widgets.clear()
        self.attribute_row_counter = 1

    def on_sorting_combobox_select(self, event):
        if self.attributes_sort_combobox.get() == "Sort Attributes by Category":
            self.display_attributes_by_category()
        else:
            self.display_attributes_sorted_alphabetically()

    def update_attribute_level(self, attribute_name, attribute_var, character_profile):
        try:
            print(character_profile.character_data['attribute'])
            new_level = int(attribute_var.get())
            print(new_level)
            self.character_profile.character_data['attributes'][attribute_name] = new_level
            self.character_profile.save_character_data()  # Save the updated data back to the YAML file
        except ValueError:
            # Handle non-integer inputs
            pass

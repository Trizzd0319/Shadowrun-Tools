from tkinter import Frame, Button, Label, Entry
from tkinter import ttk

class GUIComponents:

    def create_menu(self):
        # Define your menu creation logic here
        pass

    @staticmethod
    def create_priority_selection_section(parent_frame, priority_categories, priority_choices, update_callback):
        priority_frame = Frame(parent_frame, bd=1, relief="solid")
        priority_frame.pack(fill='x', padx=10, pady=5, expand=True)

        # Creating labels and comboboxes for each category
        for i, category in enumerate(priority_categories):
            Label(priority_frame, text=f"{category} Priority:").grid(row=0, column=i, padx=5, pady=2)
            combobox = ttk.Combobox(priority_frame, values=priority_choices, state="readonly",
                                    name=f"{category.lower()}_priority_combobox")
            combobox.grid(row=1, column=i, padx=5, pady=2)
            combobox.set("Select Priority")
            combobox.bind("<<ComboboxSelected>>", update_callback)

    @staticmethod
    def create_player_info_section(parent_frame):
        player_info_frame = Frame(parent_frame, bd=1, relief="solid")
        player_info_frame.pack(fill='x', padx=10, pady=5, expand=True)

        Label(player_info_frame, text="Player Name").grid(row=0, column=0, padx=5, pady=5)
        Entry(player_info_frame).grid(row=0, column=1, padx=5, pady=5)

        Label(player_info_frame, text="Notes").grid(row=1, column=0, padx=5, pady=5)
        Entry(player_info_frame).grid(row=1, column=1, padx=5, pady=5)

    @staticmethod
    def create_personal_section(parent_frame):
        personal_frame = Frame(parent_frame, bd=1, relief="solid")
        personal_frame.pack(fill='x', padx=10, pady=5, expand=True)

        # Add components for the personal section as needed

    @staticmethod
    def create_attributes_section(parent_frame, attributes_df):
        attributes_frame = Frame(parent_frame, bd=1, relief="solid")
        attributes_frame.pack(fill='both', expand=True, padx=10, pady=5)

        Label(attributes_frame, text="Attributes", font=('Arial', 14), justify='center').grid(row=0, columnspan=4,
                                                                                              sticky='ew')

        attributes_per_row = 4  # Number of attributes per row
        row = 1  # Start from the second row due to the title label

        for i, attribute_row in enumerate(attributes_df.itertuples()):
            column_offset = (i % attributes_per_row) * 4  # Space for Attribute Name, -, Level, +

            attribute_name = attribute_row.Attribute
            level_var = attribute_row.LevelVar

            Label(attributes_frame, text=attribute_name).grid(row=row, column=column_offset, padx=5, pady=5)
            decrement_button = Button(attributes_frame, text="-",
                                      command=lambda var=level_var, idx=i: decrement_attribute_level(var, idx))
            decrement_button.grid(row=row, column=column_offset + 1, padx=5, pady=5)
            Label(attributes_frame, textvariable=level_var, width=5).grid(row=row, column=column_offset + 2, padx=5,
                                                                          pady=5)
            increment_button = Button(attributes_frame, text="+",
                                      command=lambda var=level_var, idx=i: increment_attribute_level(var, idx))
            increment_button.grid(row=row, column=column_offset + 3, padx=5, pady=5)

            # Every 'attributes_per_row' attributes, start a new row
            if (i + 1) % attributes_per_row == 0:
                row += 1

    @staticmethod
    def create_skills_section(parent_frame, skills_df):
        skills_frame = Frame(parent_frame, bd=1, relief="solid")
        skills_frame.pack(fill='both', expand=True, padx=10, pady=5)

        Label(skills_frame, text="Skills", font=('Arial', 14), justify='center').grid(row=0, columnspan=4, sticky='ew')

        skills_per_row = 4  # Number of skills per row
        row = 1  # Start from the second row due to the title label

        for i, skill_row in enumerate(skills_df.itertuples()):
            column_offset = (i % skills_per_row) * 4  # Space for Skill Name, -, Level, +

            skill_name = skill_row.Skill
            level_var = skill_row.LevelVar

            Label(skills_frame, text=skill_name).grid(row=row, column=column_offset, padx=5, pady=5)
            Label(skills_frame, textvariable=level_var, width=5).grid(row=row, column=column_offset + 1, padx=5, pady=5)
            decrement_button = Button(skills_frame, text="-",
                                      command=lambda var=level_var, idx=i: decrement_skill_level(var, idx))
            decrement_button.grid(row=row, column=column_offset + 2, padx=5, pady=5)
            increment_button = Button(skills_frame, text="+",
                                      command=lambda var=level_var, idx=i: increment_skill_level(var, idx))
            increment_button.grid(row=row, column=column_offset + 3, padx=5, pady=5)

            # Every 'skills_per_row' skills, start a new row
            if (i + 1) % skills_per_row == 0:
                row += 1

    # Add more static methods for creating additional sections as needed

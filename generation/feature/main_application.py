import tkinter as tk

from character_logic import CharacterLogic
from data_management import DataManagement
from gui_components import GUIComponents


class MainApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Shadowrun Character Creator")
        self.root.geometry("800x600")

        # Initialize data management
        self.data_manager = DataManagement()

        # Initialize character attributes and skills data
        self.attributes_df = self.data_manager.initialize_attributes()
        self.skills_df = self.data_manager.initialize_skills()

        # Initialize priority dictionary
        self.priority_dict = self.data_manager.initialize_priority()

        # Initialize initial karma
        self.initial_karma = self.data_manager.get_initial_karma()

        # Create GUI components
        self.gui_components = GUIComponents()
        self.gui_components.create_menu()
        self.gui_components.create_priority_frame(self.priority_dict)
        self.gui_components.create_attributes_frame(self.attributes_df)
        self.gui_components.create_skills_frame(self.skills_df)
        self.gui_components.create_karma_frame(self.initial_karma)

        # Bind event handlers
        self.gui_components.priority_menu.bind("<<ComboboxSelected>>", self.update_attributes)
        self.gui_components.update_karma_button.bind("<Button-1>", self.update_remaining_karma)

    def update_attributes(self, event):
        selected_priority = self.gui_components.priority_menu.get()
        for index, row in self.attributes_df.iterrows():
            priority_level = self.gui_components.attributes_priority[index].get()
            priority_value = CharacterLogic.calculate_priority_value(priority_level, self.priority_dict)
            row['LevelVar'].set(priority_value)

    def update_remaining_karma(self, event):
        total_karma_spent = CharacterLogic.calculate_total_karma_spent(self.attributes_df, self.skills_df)
        remaining_karma = CharacterLogic.calculate_remaining_karma(total_karma_spent, self.initial_karma)
        self.gui_components.remaining_karma_var.set(remaining_karma)

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    app = MainApplication(root)
    root.mainloop()

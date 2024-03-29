import os
import tkinter as tk
from tkinter import messagebox, filedialog

import yaml


class CharacterProfile:
    def __init__(self, default_file_path='character_profile.yaml'):
        self.default_file_path = default_file_path
        self.file_path = None  # This will be set when saving or explicitly loading a profile
        self.character_data = {}
        self.load_default_data()

    def load_default_data(self):
        """
        Load default character data from the specified YAML file without prompting.
        """
        if os.path.isfile(self.default_file_path):
            with open(self.default_file_path, 'r') as file:
                self.character_data = yaml.safe_load(file) or {}
        else:
            print(f"The default file {self.default_file_path} was not found. Starting with an empty profile.")
            self.character_data = {}

    def load_character_data(self):
        """
        Prompts the user to select a file to load character data from.
        """
        root = tk.Tk()
        root.withdraw()  # Hide the root window
        filename = filedialog.askopenfilename(
            title="Load character profile",
            filetypes=[("YAML files", "*.yaml"), ("All files", "*.*")])
        if filename:
            try:
                with open(filename, 'r') as file:
                    self.character_data = yaml.safe_load(file) or {}
                self.file_path = filename  # Update file_path to the loaded file
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load file: {e}")
        else:
            print("Load operation cancelled.")

    def save_character_data(self):
        """
        Saves the character data, optionally merging with default values first.
        """
        # Prompt user for save file name/location if not previously set
        if not self.file_path:
            root = tk.Tk()
            root.withdraw()  # Hide the root window
            self.file_path = filedialog.asksaveasfilename(
                title="Save character profile",
                defaultextension=".yaml",
                filetypes=[("YAML files", "*.yaml"), ("All files", "*.*")])

        if self.file_path:
            try:
                with open(self.file_path, 'r') as file:
                    yaml.dump(self.character_data, file, default_flow_style=False, allow_unicode=True)
                messagebox.showinfo("Success", f"Profile saved to {self.file_path}")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to save file: {e}")
        else:
            print("Save operation cancelled.")

    def update_priorities(self, priorities):
        """Updates the priorities in the character data."""
        self.character_data['priorities'] = priorities
        # Optionally save to file immediately, or just update the object for now
        # self.save_character_data()

    def save_character_data(self, filepath):
        if not isinstance(self.character_data, dict):
            print("character_data is not a dictionary. Aborting save.")
            return
        file_path = filedialog.asksaveasfilename(
            defaultextension=".yaml",
            filetypes=[("YAML files", "*.yaml"), ("All files", "*.*")],
            title="Save Character Data"
        )

        # Check if a file path was selected
        if file_path:
            try:
                with open(file_path, 'w') as file:
                    yaml.dump(self.character_data, file, default_flow_style=False, allow_unicode=True)
                print(f"Character data saved to {file_path}.")
            except Exception as e:
                print(f"Error saving character data: {e}")
        else:
            print("Save operation cancelled.")

    def get_attribute_level(self, attribute_name):
        """
        Retrieves the level of a specific attribute.

        :param attribute_name: Name of the attribute to retrieve the level for.
        :return: Level of the specified attribute or None if not found.
        """
        # Example: Assuming character_data is a dictionary with an 'attributes' sub-dictionary
        attributes = self.character_data.get('attributes', {})
        # Return the attribute level or None if the attribute is not found
        return attributes.get(attribute_name)

    def get_skill_level(self, skill_name):
        """Retrieve the level (rank) of a specific skill."""
        if 'skills' in self.character_data:
            for attribute_category, skills_dict in self.character_data['skills'].items():
                if skill_name in skills_dict:
                    # Assuming each skill directly contains its rank within the second dictionary layer
                    return skills_dict[skill_name].get('rank', 0)
        return 0

    def get_attribute(self, attribute_path: str):
        """Retrieve a character attribute using a dot-separated path."""
        # self.load_character_data()  # Ensure data is loaded
        try:
            attributes = attribute_path.split('.')
            data = self.character_data
            for attr in attributes:
                data = data[attr]
            return data
        except KeyError:
            print(f"Attribute path '{attribute_path}' not found.")
            return None

    def update_attribute(self, attribute_path: str, value):
        """Update a character attribute based on a dot-separated path."""
        # self.load_character_data()  # Ensure data is loaded
        try:
            attributes = attribute_path.split('.')
            data = self.character_data
            for attr in attributes[:-1]:
                data = data.get(attr, {})
            data[attributes[-1]] = value
        except KeyError:
            print(f"Attribute path '{attribute_path}' not found.")

    def aggregate_section_data(self, section_name, section_data):
        """Aggregate data from a specific section into the character profile."""
        self.character_data[section_name] = section_data

    def save_profile_to_file(self, file_path):
        """Save the aggregated character profile data to a file."""
        with open(file_path, 'w') as file:
            yaml.dump(self.character_data, file)


# Example usage:
if __name__ == "__main__":
    profile = CharacterProfile('variables/character_profile.yaml')

import tkinter as tk
from tkinter import filedialog


class SectionPlayer(tk.Frame):
    def __init__(self, root, title, position, character_profile=None, scrollable=False, **kw):
        super().__init__(root, **kw)
        self.character_profile = character_profile
        self.grid(row=position[0], column=position[1])  # Position the frame according to the given position

        # Optionally use 'title' if needed
        if title:
            self.create_title_label(title)

        self.create_widgets()

    def create_title_label(self, title):
        tk.Label(self, text=title).grid(row=0, column=0, columnspan=2, sticky="ew")

    def create_widgets(self):
        # Player Name
        tk.Label(self, text="Player Name:").grid(row=1, column=0, sticky="w")
        self.player_name_var = tk.StringVar(value=self.character_profile.character_data.get('player_name', ''))
        self.player_name_entry = tk.Entry(self, textvariable=self.player_name_var)
        self.player_name_entry.grid(row=1, column=1, sticky="ew")

        # Save Button
        self.save_button = tk.Button(self, text="Save", command=self.save_data)
        self.save_button.grid(row=2, column=0, sticky="ew")

        # Load Button
        self.load_button = tk.Button(self, text="Load", command=self.load_data)
        self.load_button.grid(row=2, column=1, sticky="ew")

        # Adjust column configuration for resizing
        self.columnconfigure(1, weight=1)

    # def save_data(self):
    #     player_name = self.player_name_var.get().strip()
    #     if player_name:
    #         self.character_profile.character_data[
    #             'player_name'] = player_name  # Update character profile with player name
    #         # Ask for file name and directory
    #         filepath = filedialog.asksaveasfilename(
    #             defaultextension=".yaml",
    #             filetypes=[("YAML files", "*.yaml"), ("All files", "*.*")],
    #         )
    #         if filepath:
    #             self.character_profile.save_character_data(filepath)  # Pass the chosen file path to save method
    #     else:
    #         messagebox.showwarning("Warning", "Player name cannot be empty.")
    def save_data(self):
        # This method is called when the "Save" button is clicked.
        # It should trigger the overall save process.
        self.master.save_character_profile()  # Assuming the root (main application/GUI Manager) has this method

    def load_data(self):
        filepath = filedialog.askopenfilename(
            filetypes=[("YAML files", "*.yaml"), ("All files", "*.*")]
        )
        if filepath:
            self.character_profile.load_character_data(filepath)
            player_name = self.character_profile.character_data.get('player_name', '')
            self.player_name_var.set(player_name)

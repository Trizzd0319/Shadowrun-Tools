import tkinter as tk
from tkinter import ttk


class MetatypeSelectionWindow:
    def __init__(self, parent, callback, adjustment_callback, selected_metatype, available_races):
        """
        Initialize the MetatypeSelectionWindow.

        Args:
            parent: The parent Tkinter window.
            callback: The callback function to handle selected race.
            adjustment_callback: The callback function to handle adjustments based on selected metatype.
            selected_metatype: The initially selected metatype.
            available_races: List of available races.
        """
        self.parent = parent
        self.callback = callback
        self.adjustment_callback = adjustment_callback
        self.selected_metatype = selected_metatype
        self.available_races = available_races
        self.root = None

        # Call the create_window method to create the window when needed
        self.create_window()

    def create_window(self):
        """Create the window for metatype selection."""
        print("Creating MetatypeSelectionWindow...")
        self.root = tk.Toplevel(self.parent)
        self.root.title("Metatype Selection")

        self.radio_frame = ttk.Frame(self.root)
        self.radio_frame.pack(padx=10, pady=10)

        self.metatype_radios = {}

        # Create radio buttons for each available race within the context of the Tkinter application
        for race in self.available_races:
            var = tk.StringVar(value="")
            radio_button = ttk.Radiobutton(self.radio_frame, text=race, variable=var, value=race,
                                           command=lambda race=race: self.update_selected(race))
            radio_button.pack(anchor=tk.W)
            self.metatype_radios[race] = var

        # Create a button to confirm selection
        confirm_button = ttk.Button(self.root, text="Confirm", command=self.confirm_selection)
        confirm_button.pack(pady=10)

    def update_selected(self, race):
        """
        Update the selected metatype.

        Args:
            race: The selected race.
        """
        print(f"Selected race: {race}")
        # Clear any previous selections
        for var in self.metatype_radios.values():
            var.set("")

        # Set the selected race
        self.metatype_radios[race].set(race)
        self.selected_metatype = race  # Update the selected metatype

    def confirm_selection(self):
        """Handle confirmation of metatype selection."""
        selected_race = ""

        for race, var in self.metatype_radios.items():
            if var.get():  # Check if the radio button is selected
                selected_race = race
                break

        self.callback(selected_race)
        self.adjustment_callback(self.selected_metatype)  # Pass the selected metatype for adjustment
        self.root.destroy()


if __name__ == "__main__":
    # Example usage
    available_races = ['Dwarf', 'Elf', 'Human', 'Ork', 'Troll']

    root = tk.Tk()  # Create the root window
    app = MetatypeSelectionWindow(root, lambda selected_race: print(f"Selected race: {selected_race}"),
                                  lambda selected_metatype: print(f"Selected metatype: {selected_metatype}"),
                                  "Elf", available_races)  # Pass the selected metatype here

    root.mainloop()  # Start the main application loop

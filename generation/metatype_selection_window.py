import tkinter as tk
from tkinter import ttk

class MetatypeSelectionWindow:
    def __init__(self, parent, callback, metatype_data):
        self.parent = parent
        self.callback = callback
        self.metatype_data = metatype_data

        self.root = None  # Initialize root as None

        # Call the create_window method to create the window when needed
        self.create_window()

    def create_window(self):
        self.root = tk.Toplevel(self.parent)
        self.root.title("Metatype Selection")

        self.radio_frame = ttk.Frame(self.root)
        self.radio_frame.pack(padx=10, pady=10)

        self.metatype_radios = {}

        # Create radio buttons for each metatype within the context of the Tkinter application
        for metatype, attributes in self.metatype_data.items():
            var = tk.StringVar(value="")
            radio_button = ttk.Radiobutton(self.radio_frame, text=metatype, variable=var, value=metatype,
                                           command=lambda metatype=metatype: self.update_selected(metatype))
            radio_button.pack(anchor=tk.W)
            self.metatype_radios[metatype] = (var, attributes)

        # Create a button to confirm selection
        confirm_button = ttk.Button(self.root, text="Confirm", command=self.print_selected_options)
        confirm_button.pack(pady=10)

    def update_selected(self, metatype):
        # Clear any previous selections
        for var, _ in self.metatype_radios.values():
            var.set("")

        # Set the selected metatype
        self.metatype_radios[metatype][0].set(metatype)

    def print_selected_options(self):
        selected_metatype = ""
        selected_ability = {}

        for metatype, (var, _) in self.metatype_radios.items():
            if var.get():  # Check if the radio button is selected
                selected_metatype = metatype
                selected_ability = self.metatype_data[selected_metatype]
                break

        print(f"Selected Metatype: {selected_metatype}, Ability: {selected_ability}")
        self.callback({'Metatype': selected_metatype, 'Special Attributes': selected_ability})


# Sample metatype data for Shadowrun 6e
metatype_data = {
    'Human': {'Special Attributes': 'None'},
    'Elf': {'Special Attributes': 'Low-Light Vision'},
    'Dwarf': {'Special Attributes': 'Thermographic Vision'},
    'Ork': {'Special Attributes': 'Low-Light Vision'},
    'Troll': {'Special Attributes': 'Thermographic Vision'},
}

# Example usage
if __name__ == "__main__":
    root = tk.Tk()  # Create the root window
    app = MetatypeSelectionWindow(root, lambda selected_options: print(selected_options), metatype_data)
    root.mainloop()  # Start the main application loop

import tkinter as tk
from tkinter import ttk


class PrioritySelectionWindow:
    priority_data = {
        'A': {'Metatype': 'Dwarf, Ork, Troll (13)', 'Attributes': 24, 'Skills': 32,
              'Magic/Resonance': 'Full: 4 Magic, Aspected: 5 Magic, Mystic Adept: 4 Magic, Adept: 4 Magic, Technomancer: 4 Resonance',
              'Resources': '450,000'},
        'B': {'Metatype': 'Dwarf, Elf, Ork, Troll (11)', 'Attributes': 16, 'Skills': 24,
              'Magic/Resonance': 'Full: 3 Magic, Aspected: 4 Magic, Mystic Adept: 3 Magic, Adept: 3 Magic, Technomancer: 3 Resonance',
              'Resources': '275,000'},
        'C': {'Metatype': 'Dwarf, Elf, Human, Ork, Troll (9)', 'Attributes': 12, 'Skills': 20,
              'Magic/Resonance': 'Full: 2 Magic, Aspected: 3 Magic, Mystic Adept: 2 Magic, Adept: 2 Magic, Technomancer: 2 Resonance',
              'Resources': '150,000'},
        'D': {'Metatype': 'Dwarf, Elf, Human, Ork, Troll (4)', 'Attributes': 8, 'Skills': 16,
              'Magic/Resonance': 'Full: 1 Magic, Aspected: 2 Magic, Mystic Adept: 1 Magic, Adept: 1 Magic, Technomancer: 1 Resonance',
              'Resources': '50,000'},
        'E': {'Metatype': 'Dwarf, Elf, Human, Ork, Troll (1)', 'Attributes': 2, 'Skills': 10,
              'Magic/Resonance': 'Mundane', 'Resources': '8,000'}
    }

    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback

        # Create Tkinter window
        self.root = tk.Toplevel(parent)
        self.root.title("Priority Selection")

        # Sample data
        self.priorities = ['A', 'B', 'C', 'D', 'E']
        self.options = ['Metatype', 'Attributes', 'Skills', 'Magic/Resonance', 'Resources']

        # Dictionary to store dropdowns and labels
        self.dropdowns = {}
        self.labels = {}

        # Create label
        label = ttk.Label(self.root, text="Select Priority and Option:")
        label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

        # Create dropdowns for each priority
        for i, priority in enumerate(self.priorities):
            ttk.Label(self.root, text=f"Priority {priority}:").grid(row=i + 1, column=0, padx=10, pady=5, sticky='e')
            self.dropdowns[priority] = ttk.Combobox(self.root, values=self.options, state="readonly")
            self.dropdowns[priority].grid(row=i + 1, column=1, padx=10, pady=5, sticky='w')
            self.dropdowns[priority].bind("<<ComboboxSelected>>", lambda event, index=i, priority=priority: self.handle_dropdown_selection(event, index, priority))
            self.labels[priority] = ttk.Label(self.root, text="")
            self.labels[priority].grid(row=i + 1, column=2, padx=10, pady=5, sticky='w')

        # Create label to display selected option
        self.display_data_label = ttk.Label(self.root, text="")
        self.display_data_label.grid(row=len(self.priorities) + 1, column=0, columnspan=3, padx=10, pady=10)

        # Button to confirm selections
        self.confirm_button = ttk.Button(self.root, text="Confirm Selections", command=self.print_selected_options, state='disabled')
        self.confirm_button.grid(row=len(self.priorities) + 2, column=0, columnspan=3, padx=10, pady=10)

        # Button to reset options
        self.reset_button = ttk.Button(self.root, text="Reset Options", command=self.reset_options)
        self.reset_button.grid(row=len(self.priorities) + 3, column=0, columnspan=3, padx=10, pady=10)

    def handle_dropdown_selection(self, event, index, priority):
        selected_option = event.widget.get()
        self.labels[priority].config(text=self.priority_data[priority][selected_option])
        self.enable_confirm_button()

    def enable_confirm_button(self):
        all_selections_made = all(self.dropdowns[priority].get() != '' for priority in self.priorities)
        self.confirm_button['state'] = 'normal' if all_selections_made else 'disabled'

    def print_selected_options(self):
        selected_priority_options = {priority: self.dropdowns[priority].get() for priority in self.priorities}
        print(selected_priority_options)
        # ccw = CharacterCreationOptionsWindow(self.parent, selected_priority_options)
        # ccw.create_labels()

        self.callback(selected_priority_options)

        self.root.destroy()

    def reset_options(self):
        for priority in self.priorities:
            self.dropdowns[priority].set('')
            self.labels[priority].config(text='')
        self.enable_confirm_button()


# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    app = PrioritySelectionWindow(root, lambda selected_options: print(selected_options))
    root.mainloop()

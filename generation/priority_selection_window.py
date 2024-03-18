import tkinter as tk
from tkinter import ttk
from variables import priority_data


class PrioritySelectionWindow:
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback
        self.root = None

        # Create Tkinter window
        self.root = tk.Toplevel(parent)
        self.root.title("Priority Selection")

        # Sample data
        self.priorities = ['A', 'B', 'C', 'D', 'E']
        self.options = ['Attributes', 'Skills', 'Magic/Resonance', 'Resources', 'Races']
        self.options.sort()  # Sort the options alphabetically

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
            self.dropdowns[priority].bind("<<ComboboxSelected>>",
                                          lambda event, index=i, priority=priority: self.handle_dropdown_selection(
                                              event, index, priority))
            self.labels[priority] = ttk.Label(self.root, text="")
            self.labels[priority].grid(row=i + 1, column=2, padx=10, pady=5, sticky='w')

        # Create label to display selected option
        self.display_data_label = ttk.Label(self.root, text="")
        self.display_data_label.grid(row=len(self.priorities) + 1, column=0, columnspan=3, padx=10, pady=10)

        # Button to confirm selections
        self.confirm_button = ttk.Button(self.root, text="Confirm Selections", command=self.print_selected_options,
                                         state='disabled')
        self.confirm_button.grid(row=len(self.priorities) + 2, column=0, columnspan=3, padx=10, pady=10)

        # Button to reset options
        self.reset_button = ttk.Button(self.root, text="Reset Options", command=self.reset_options)
        self.reset_button.grid(row=len(self.priorities) + 3, column=0, columnspan=3, padx=10, pady=10)

        # Dictionary to track selected options
        self.selected_options = {}

    def handle_dropdown_selection(self, event, index, priority):
        selected_option = event.widget.get()

        # Remove the selected option from other dropdowns
        for p, dropdown in self.dropdowns.items():
            if p != priority:
                values = list(dropdown["values"])
                if selected_option in values:
                    values.remove(selected_option)
                    dropdown["values"] = values

                other_option = dropdown.get()
                if other_option == selected_option:
                    dropdown.set('')
                    self.labels[p].config(text='')

        self.labels[priority].config(text=priority_data[priority][selected_option])
        self.enable_confirm_button()

    def enable_confirm_button(self):
        all_selections_made = all(self.dropdowns[priority].get() != '' for priority in self.priorities)
        self.confirm_button['state'] = 'normal' if all_selections_made else 'disabled'

    def print_selected_options(self):
        selected_priority_options = {priority: self.dropdowns[priority].get() for priority in self.priorities}
        print(selected_priority_options)

        self.callback(selected_priority_options)

        self.root.destroy()

    def reset_options(self):
        # Clear the selection options array
        self.selection_options = {}

        # Reset the dropdowns and labels
        for priority in self.priorities:
            self.dropdowns[priority].set('')
            self.labels[priority].config(text='')
            self.dropdowns[priority]["values"] = self.options

    def confirm_selection(self):
        selected_options = {}
        for priority, dropdown in self.dropdowns.items():
            selected_options[priority] = dropdown.get()
        self.callback(selected_options)  # Call the callback function with selected options
        self.root.destroy()

        # Disable the confirm button
        self.confirm_button['state'] = 'disabled'


# Example usage
if __name__ == "__main__":
    root = tk.Tk()
    app = PrioritySelectionWindow(root, lambda selected_options: print(selected_options))
    root.mainloop()

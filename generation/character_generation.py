import tkinter as tk
from tkinter import ttk
from priority_selection_window import PrioritySelectionWindow
from metatype_selection_window import MetatypeSelectionWindow
from metatype_selection_window import metatype_data  # Importing metatype_data

class CharacterCreationOptionsWindow:
    def __init__(self, parent, callback):
        self.parent = parent
        self.callback = callback

        self.root = tk.Tk()
        self.root.title("Character Creation Options so far")

        self.sections_label = ttk.Label(self.root, text="Character Creation Sections")
        self.sections_label.grid(row=0, column=0, padx=10, pady=10, columnspan=3)

        buttons_frame = ttk.Frame(self.root)
        buttons_frame.grid(row=1, column=0, columnspan=3, padx=10, pady=10)

        # Row 1 buttons
        self.priority_selection_button = ttk.Button(buttons_frame, text="Priority",
                                                    command=self.open_priority_selection)
        self.priority_selection_button.grid(row=0, column=0, padx=5, pady=5)

        self.metatype_button = ttk.Button(buttons_frame, text="Metatype", command=self.open_metatype_selection)
        self.metatype_button.grid(row=0, column=1, padx=5, pady=5)

        # Row 3 button (centered)
        self.adjustment_points_button = ttk.Button(self.root, text="Adjustment Points",
                                                   command=self.open_adjustment_points)
        self.adjustment_points_button.grid(row=2, column=0, columnspan=3, padx=10, pady=10)

        # Horizontal divider
        self.divider = ttk.Separator(self.root, orient="horizontal")
        self.divider.grid(row=3, column=0, columnspan=3, sticky="ew", padx=10, pady=10)

        # Sections below the divider
        self.section1_frame = ttk.LabelFrame(self.root, text="Priority Selection")
        self.section1_frame.grid(row=4, column=0, padx=10, pady=10, sticky="ew", columnspan=3)
        ttk.Label(self.section1_frame, text="").pack()

        self.section2_frame = ttk.LabelFrame(self.root, text="Metatype Selection")
        self.section2_frame.grid(row=5, column=0, padx=10, pady=10, sticky="ew", columnspan=3)
        ttk.Label(self.section2_frame, text="").pack()

        # Initialize treeview
        self.treeview = ttk.Treeview(self.section2_frame, columns=("Attributes"), show="headings")
        self.treeview.heading("#1", text="Attributes")
        self.treeview.pack(fill="both", expand=True)

        self.section7_frame = ttk.LabelFrame(self.root, text="Adjustment Points Selection")
        self.section7_frame.grid(row=6, column=0, padx=10, pady=10, sticky="ew", columnspan=3)
        ttk.Label(self.section7_frame, text="").pack()

        # Initialize PrioritySelectionWindow and MetatypeSelectionWindow instances
        self.priority_selection_window = None
        self.metatype_selection_window = None

    def open_priority_selection(self):
        if not self.priority_selection_window:
            self.priority_selection_window = PrioritySelectionWindow(self.root, self.update_priority_options)
        else:
            self.priority_selection_window.root.lift()

    def open_metatype_selection(self):
        if not self.metatype_selection_window:
            self.metatype_selection_window = MetatypeSelectionWindow(self.root, self.update_metatype_options, metatype_data)
        else:
            self.metatype_selection_window.root.lift()

    def open_adjustment_points(self):
        self.adjustment_points_window = AdjustmentPointsWindow(self.root, self.update_adjustment_options)

    def update_priority_options(self, selected_priority_options):
        section1_text = ""

        for priority, option in selected_priority_options.items():
            if option and priority in PrioritySelectionWindow.priority_data and option in \
                    PrioritySelectionWindow.priority_data[priority]:
                priority_text = f"{PrioritySelectionWindow.priority_data[priority][option]}"
                if option == 'Resources':
                    priority_text += '¥'
                section1_text += f"{priority}: {option}: {priority_text}\n"
            else:
                section1_text += f"{priority}: {option}: Invalid Option\n"  # Handle invalid option

        for widget in self.section1_frame.winfo_children():
            widget.destroy()

        ttk.Label(self.section1_frame, text=section1_text).pack(fill='x')

    def update_metatype_options(self, selected_metatype_options):
        section2_text = ""

        for metatype, attributes in selected_metatype_options.items():
            if isinstance(attributes, list):
                attribute_text = "; ".join(attributes)
            else:
                attribute_text = attributes
            section2_text += f"{metatype}: {attribute_text}\n"

        for widget in self.section2_frame.winfo_children():
            widget.destroy()

        # Remove the dataframe breaks
        section2_text = section2_text.replace("\n", "")

        # Remove the headers
        section2_text = section2_text.replace("Metatype Selected: ", "").replace("Special Attributes: ", "")

        # Remove the column headers
        section2_text = section2_text.replace("Metatype", "").replace("Special Attributes", "")

        ttk.Label(self.section2_frame, text=section2_text).pack(fill='x')

    def open_adjustment_points(self):
        self.adjustment_points_window = AdjustmentPointsWindow(self.root, self.update_adjustment_options)

    def update_adjustment_options(self, selected_adjustment_options):
        # Handle adjustment options update here if needed
        pass

    def run(self):
        self.root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = CharacterCreationOptionsWindow(root, None)
    app.run()

from tkinter import Tk, Frame, Label, ttk, Spinbox, Canvas, Scrollbar, VERTICAL

from variables import *


# from calculations import update_height_options


class GUIManager:
    def __init__(self, root, skills):
        self.root = root
        self.skills = skills
        self.sections = {}
        self.metatype_combobox = None
        self.height_combobox = None
        self.initialize_gui()

    def create_scrollable_section(self, name, row, column, rowspan=1, columnspan=1):
        outer_frame = Frame(self.root, borderwidth=2, relief="groove")
        outer_frame.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew", padx=5, pady=5)
        self.root.grid_rowconfigure(row, weight=1)
        self.root.grid_columnconfigure(column, weight=1)

        canvas = Canvas(outer_frame)
        canvas.grid(row=0, column=0, sticky="nsew")

        scrollbar = Scrollbar(outer_frame, orient=VERTICAL, command=canvas.yview)
        scrollbar.grid(row=0, column=1, sticky="ns")
        canvas.configure(yscrollcommand=scrollbar.set)

        frame = Frame(canvas)
        canvas.create_window((0, 0), window=frame, anchor="nw")

        def configure_scroll_region(event):
            canvas.configure(scrollregion=canvas.bbox("all"))

        def configure_canvas_width(event):
            canvas_width = outer_frame.winfo_width()
            canvas.itemconfig("inner_frame", width=canvas_width)

        frame.bind("<Configure>", configure_scroll_region)
        canvas.bind("<Configure>", configure_canvas_width)
        canvas.itemconfig("inner_frame", width=frame.winfo_reqwidth())

        Label(frame, text=name).grid(row=0, column=0, padx=10, pady=10)
        self.sections[name] = frame

    def create_section(self, name, row, column, rowspan=1, columnspan=1):
        frame = Frame(self.root, borderwidth=2, relief="groove")
        frame.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew", padx=5, pady=5)
        Label(frame, text=name).grid(row=0, column=0, columnspan=2, padx=10, pady=10)
        self.sections[name] = frame

    def add_widget(self, section, widget_type, label_text, row, column=0, **options):
        frame = self.sections.get(section)
        if not frame:
            raise ValueError(f"Section {section} not found")

        label = ttk.Label(frame, text=label_text)
        label.grid(row=row, column=column * 2, padx=5, pady=2, sticky="w")

        widget = None
        if widget_type == "entry":
            widget = ttk.Entry(frame, **options)
        elif widget_type == "combobox":
            widget = ttk.Combobox(frame, **options)
            if label_text == "Metatype":
                self.metatype_combobox = widget
                # Bind the selection event to dynamically update the Height options
                widget.bind('<<ComboboxSelected>>',
                            lambda event: update_height_options(self.metatype_combobox, self.height_combobox,
                                                                metatype_data))
            elif label_text == "Height":
                self.height_combobox = widget
        elif widget_type == "spinner":
            widget = Spinbox(frame, **options)
        elif widget_type == "label":
            widget = Label(frame, text=label_text, **options)  # Use label_text for Label text content
        else:
            raise ValueError("Unsupported widget type")

        widget.grid(row=row, column=column * 2 + 1, padx=5, pady=2, sticky="ew")
        return widget

    def initialize_gui(self):
        self.create_scrollable_section("Personal Data", 0, 0, 1, 1)
        self.add_widget("Personal Data", "entry", "Name", 1, **{})  # Unpack an empty dictionary for clarity
        self.add_widget("Personal Data", "combobox", "Metatype", 2, **{'values': metatype_data["Metatype"]})
        self.add_widget("Personal Data", "entry", "Ethnicity", 3, **{})
        self.add_widget("Personal Data", "combobox", "Age", 4, **{'values': list(range(17, 66))})
        self.add_widget("Personal Data", "combobox", "Sex", 5, **{'values': ["Male", "Female", "Other"]})
        self.add_widget("Personal Data", "entry", "Reputation", 6, **{})
        self.add_widget("Personal Data", "combobox", "Height", 7, **{'values': []})
        self.add_widget("Personal Data", "combobox", "Weight", 8, **{'values': ["Example Weight"]})

        # Add additional sections
        self.create_scrollable_section("Core Combat Info", 0, 1, 1, 1)
        self.add_widget("Core Combat Info", "combobox", "Primary Melee Weapon", 2, **{'values': weapons["Name"]})
        self.create_scrollable_section("Attributes", 1, 0, 1, 1)
        self.create_scrollable_section("Skills", 1, 1, 1, 1)
        self.create_scrollable_section("Qualities, Positive", 2, 0, 1, 1)
        self.create_scrollable_section("Qualities, Negative", 2, 1, 1, 1)
        self.create_scrollable_section("IDs/Lifestyle/Currency", 3, 0, 1, 1)
        self.create_scrollable_section("Contacts", 3, 1, 1, 1)

        # Configure grid layout for automatic resizing
        self.root.grid_columnconfigure(0, weight=1)
        self.root.grid_columnconfigure(1, weight=1)
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_rowconfigure(2, weight=1)
        self.root.grid_rowconfigure(3, weight=1)


# Main application setup
if __name__ == "__main__":
    root = Tk()
    root.title("Character Sheet")
    root.geometry("800x600")

    # Main scrollbar for the entire window
    main_scrollbar = Scrollbar(root, orient=VERTICAL)
    main_scrollbar.pack(side="right", fill="y")

    main_canvas = Canvas(root, yscrollcommand=main_scrollbar.set)
    main_canvas.pack(side="left", fill="both", expand=True)

    main_scrollbar.config(command=main_canvas.yview)

    # Frame that will contain everything
    main_frame = Frame(main_canvas)
    main_canvas.create_window((0, 0), window=main_frame, anchor="nw")


    def configure_main_scroll_region(event):
        main_canvas.configure(scrollregion=main_canvas.bbox("all"))


    main_frame.bind("<Configure>", configure_main_scroll_region)

    gui_manager = GUIManager(main_frame, skills)

    root.mainloop()

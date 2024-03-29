import logging
from tkinter import Frame, Label, ttk, Canvas, Scrollbar, VERTICAL, HORIZONTAL, Checkbutton, Spinbox


def root_log():
    logging.debug("This is a debug message from some_function")
    try:
        # Code that might raise an exception
        pass
    except Exception as e:
        logging.error("An error occurred: %s", str(e))

class Section:
    def __init__(self, parent, name, row, column, rowspan=1, columnspan=1, scrollable=False):
        self.name = name
        self.scrollable = scrollable
        self.all_widgets = []  # Keep track of all widgets for width adjustment
        self.widgets = {}  # Add this line to store references to widgets
        if scrollable:
            self.outer_frame = Frame(parent, borderwidth=2, relief="groove")
            self.outer_frame.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew", padx=5, pady=5)
            parent.grid_rowconfigure(row, weight=1)
            parent.grid_columnconfigure(column, weight=1)

            canvas = Canvas(self.outer_frame)
            canvas.grid(row=0, column=0, sticky="nsew")
            self.outer_frame.grid_rowconfigure(0, weight=1)
            self.outer_frame.grid_columnconfigure(0, weight=1)

            v_scrollbar = Scrollbar(self.outer_frame, orient=VERTICAL, command=canvas.yview)
            v_scrollbar.grid(row=0, column=1, sticky="ns")
            h_scrollbar = Scrollbar(self.outer_frame, orient=HORIZONTAL, command=canvas.xview)
            h_scrollbar.grid(row=1, column=0, sticky="ew")
            canvas.configure(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)

            self.frame = Frame(canvas)
            canvas.create_window((0, 0), window=self.frame, anchor="nw")
            canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))
        else:
            self.frame = Frame(parent, borderwidth=2, relief="groove")
            self.frame.grid(row=row, column=column, rowspan=rowspan, columnspan=columnspan, sticky="nsew", padx=5, pady=5)

        Label(self.frame, text=name).grid(row=0, column=0, padx=10, pady=10)

    def add_widget(self, widget_type, label_text, row, column=0, **options):
        label = ttk.Label(self.frame, text=label_text)
        label.grid(row=row, column=column * 2, padx=5, pady=2, sticky="nsew")

        if widget_type == "entry":
            widget = ttk.Entry(self.frame, **options)
        elif widget_type == "combobox":
            widget = ttk.Combobox(self.frame, **options)
        elif widget_type == "spinner":
            widget = Spinbox(self.frame, **options)
        elif widget_type == "label":
            widget = Label(self.frame, text=label_text, **options)
        elif widget_type == "checkbox":
            widget = Checkbutton(self.frame, text=label_text, **options)
        else:
            raise ValueError("Unsupported widget type")
        widget.grid(row=row, column=column, sticky='ew')
        self.all_widgets.append((widget, column))  # Store widget with its column

        widget.grid(row=row, column=column * 2 + 1, padx=5, pady=2, sticky="ew")
        self.widgets[label_text] = widget  # Store the widget reference using label_text as the key
        return widget


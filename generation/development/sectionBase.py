import tkinter as tk
from tkinter import ttk


class SectionBase:
    def __init__(self, root, title, position, row, column, scrollable=False):
        self.root = root
        self.title = title
        self.position = position
        self.row = row
        self.column = column  # Add the column parameter
        self.position = position
        self.scrollable = scrollable
        self.widgets = {}
        self.all_widgets = []
        self.bindings = []
        self.initialize_section()

    def initialize_section(self):
        if self.scrollable:
            self._setup_scrollable_frame()
        else:
            self._setup_non_scrollable_frame()

        if self.title:
            self._add_title_label()

    def _add_title_label(self):
        title_label = ttk.Label(self.frame, text=self.title, font=('Arial', 12, 'bold'))
        title_label.pack(side="top", fill="x", pady=5)

    def _setup_scrollable_frame(self):
        self.container = tk.Frame(self.root)
        self.container.grid(row=self.position[0], column=self.position[1], sticky='nsew')
        self.canvas = tk.Canvas(self.container)
        self.scrollbar = ttk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.container.grid(row=self.position[0], column=self.position[1], sticky='nsew')
        self.root.grid_rowconfigure(self.position[0], weight=1)
        self.root.grid_columnconfigure(self.position[1], weight=1)
        self._bind_scroll_events()

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all"))
        )

        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.frame = self.scrollable_frame

    def _bind_scroll_events(self):
        event = "<MouseWheel>" if self.root.tk.call('tk', 'windowingsystem') != 'x11' else "<Button-4>"
        self.canvas.bind_all(event, self.on_mousewheel)
        self.bindings.append((None, event, self.on_mousewheel))

        if self.root.tk.call('tk', 'windowingsystem') == 'x11':
            self.canvas.bind_all("<Button-5>", self.on_mousewheel)
            self.bindings.append((None, "<Button-5>", self.on_mousewheel))

    def _setup_non_scrollable_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=self.position[0], column=self.position[1], sticky='nsew')
        self.root.grid_rowconfigure(self.position[0], weight=1)
        self.root.grid_columnconfigure(self.position[1], weight=1)

    def clear_section(self):
        self._clear_global_bindings()
        for widget in self.widgets.values():
            if isinstance(widget, dict):
                widget['widget'].destroy()
            else:
                widget.destroy()
        self.widgets.clear()

    def on_mousewheel(self, event):
        if self.root.tk.call('tk', 'windowingsystem') == 'win32':
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        elif self.root.tk.call('tk', 'windowingsystem') == 'x11':
            if event.num == 4:
                self.canvas.yview_scroll(-1, "units")
            elif event.num == 5:
                self.canvas.yview_scroll(1, "units")
        else:
            self.canvas.yview_scroll(int(-1 * event.delta), "units")

    def add_widget(self, widget_type, label_text, row, column=0, **options):
        label = ttk.Label(self.frame, text=label_text)
        label.grid(row=row, column=column * 2, padx=5, pady=2, sticky="nsew")

        widget = None
        if widget_type == "entry":
            widget = ttk.Entry(self.frame, **options)
        elif widget_type == "combobox":
            widget = ttk.Combobox(self.frame, **options)
        elif widget_type == "spinner":
            widget = tk.Spinbox(self.frame, **options)
        elif widget_type == "label":
            widget = ttk.Label(self.frame, **options)
        elif widget_type == "checkbox":
            var = tk.BooleanVar(self.frame)
            widget = tk.Checkbutton(self.frame, text=label_text, variable=var, **options)
            self.widgets[label_text] = {'widget': widget, 'variable': var}
        else:
            raise ValueError("Unsupported widget type")

        if widget_type != "checkbox":
            widget.grid(row=row, column=column * 2 + 1, padx=5, pady=2, sticky="ew")
            self.widgets[label_text] = widget

        self.all_widgets.append(widget)
        return widget

    def is_checkbox_checked(self, label_text):
        widget_info = self.widgets.get(label_text)
        if widget_info and isinstance(widget_info, dict) and 'variable' in widget_info:
            return widget_info['variable'].get()
        else:
            raise ValueError("Checkbox with label '{}' not found.".format(label_text))

    def set_checkbox_state(self, label_text, state: bool):
        widget_info = self.widgets.get(label_text)
        if widget_info and isinstance(widget_info, dict) and 'variable' in widget_info:
            widget_info['variable'].set(state)
        else:
            raise ValueError("Checkbox with label '{}' not found.".format(label_text))

    def _clear_global_bindings(self):
        for _, event, callback in self.bindings:
            if event:
                self.root.unbind_all(event)
            else:
                raise ValueError("Event should not be None.")

import tkinter as tk
from tkinter import ttk


class SectionBase:
    def __init__(self, root, profile_manager, title="", scrollable=False, position=(0, 0)):
        self.root = root
        self.profile_manager = profile_manager
        self.title = title
        self.scrollable = scrollable
        self.position = position
        self.widgets = {}
        self.bindings = []
        self.all_widgets = []
        self.local_bindings = []  # Track local bindings
        self.initialize_section()

    def initialize_section(self):
        if self.scrollable:
            self._setup_scrollable_frame()
        else:
            self._setup_non_scrollable_frame()

        if self.title:
            self._add_title_label()

    def _setup_scrollable_frame(self):
        self.container = tk.Frame(self.root)
        self.container.grid(row=self.position[0], column=self.position[1], sticky='nsew', padx=10, pady=10)

        # Grid configuration for the container to ensure it expands properly.
        self.container.grid_rowconfigure(1, weight=1)
        self.container.grid_columnconfigure(0, weight=1)

        # The title label is placed here, ensuring it's outside the scrollable area.
        if self.title:
            self.title_label = tk.Label(self.container, text=self.title)
            self.title_label.grid(row=0, column=0, sticky="ew", padx=5, pady=(5, 10))

        # Setup for the canvas and scrollbar as before.
        self.canvas = tk.Canvas(self.container)
        self.scrollbar = ttk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)
        self.canvas.grid(row=1, column=0, sticky="nsew")
        self.scrollbar.grid(row=1, column=1, sticky="ns")

        # Setup for the scrollable frame within the canvas as before.
        self.scrollable_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        self.scrollable_frame.bind("<Configure>", lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self._bind_scroll_events()

    def _setup_non_scrollable_frame(self):
        self.frame = tk.Frame(self.root)
        self.frame.grid(row=self.position[0], column=self.position[1], sticky='nsew', padx=10, pady=10)

        # For non-scrollable sections, the title label setup remains the same.
        if self.title:
            self._add_title_label()

    def _bind_scroll_events(self):
        if self.root.tk.call('tk', 'windowingsystem') == 'x11':
            self.canvas.bind_all("<Button-4>", self.on_mousewheel)
            self.canvas.bind_all("<Button-5>", self.on_mousewheel)
        else:
            self.canvas.bind_all("<MouseWheel>", self.on_mousewheel)

    def on_mousewheel(self, event):
        if self.root.tk.call('tk', 'windowingsystem') == 'win32' or self.root.tk.call('tk',
                                                                                      'windowingsystem') == 'darwin':
            self.canvas.yview_scroll(int(-1 * (event.delta / 120)), "units")
        elif self.root.tk.call('tk', 'windowingsystem') == 'x11':
            if event.num == 4:
                self.canvas.yview_scroll(-1, "units")
            else:  # event.num == 5
                self.canvas.yview_scroll(1, "units")

    def clear_section(self):
        # Enhanced to include all_widgets and external resources cleanup
        for widget in self.all_widgets:
            widget.destroy()
        self.widgets.clear()
        self.all_widgets.clear()
        self._clear_local_bindings()
        # Add logic here to release external resources if any

    def _clear_local_bindings(self):
        # New method to unbind local events
        for widget, event, callback in self.local_bindings:
            widget.unbind(event, callback)
        self.local_bindings.clear()

    def on_application_close(self):
        self.clear_section()
        self.root.destroy()

    def _clear_global_bindings(self):
        for _, event, callback in self.bindings:
            if event:
                self.canvas.unbind_all(event)
            # Consider if there's a need to keep track of bindings per widget for more granular unbinding
        self.bindings.clear()

    def _add_title_label(self):
        self.title_label = tk.Label(self.container if self.scrollable else self.frame, text=self.title)
        self.title_label.grid(row=0, column=0, sticky="ew", padx=self.STANDARD_PADX, pady=(self.STANDARD_PADY, 10))

    def add_widget(self, widget_type, label_text, row, column=0, **options):
        label = ttk.Label(self.scrollable_frame if self.scrollable else self.frame, text=label_text)
        label.grid(row=row, column=column * 2, padx=self.STANDARD_PADX, pady=self.STANDARD_PADY, sticky="nsew")

        # Widget creation code remains the same...
        # Ensure widget placement uses the standardized padding and margins

        if widget_type != "checkbox":
            widget.grid(row=row, column=column * 2 + 1, padx=self.STANDARD_PADX, pady=self.STANDARD_PADY, sticky="ew")
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

    def _create_scrollable_area(self):
        self.canvas = tk.Canvas(self.container)
        self.scrollbar = ttk.Scrollbar(self.container, orient="vertical", command=self.canvas.yview)
        self.canvas.configure(yscrollcommand=self.scrollbar.set)

        self.canvas.grid(row=1, column=0, sticky="nsew")
        self.scrollbar.grid(row=1, column=1, sticky="ns")

        self.scrollable_frame = ttk.Frame(self.canvas)
        self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")

        self.scrollable_frame.bind("<Configure>",
                                   lambda e: self.canvas.configure(scrollregion=self.canvas.bbox("all")))
        self._bind_scroll_events()

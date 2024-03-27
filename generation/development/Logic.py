from information import *
import json


def load_combined_attributes(self):
    pass


def priorities_combo_selection(event, category, label_references, combobox_references, priority_data,
                               personal_metatype):
    selected_priority = event.widget.get()

    if category in priority_data[selected_priority]:
        detail_value = priority_data[selected_priority][category]
        if isinstance(detail_value, int) or isinstance(detail_value, dict):
            label_text = f"{category} - {detail_value if isinstance(detail_value, int) else 'Varies'}"
        else:
            label_text = f"{category} - Varies"
    else:
        label_text = f"{category} Priority: {selected_priority} - N/A"

    if category in label_references:
        label_references[category].config(text=label_text)

    print(f"{category} selected: {selected_priority}")


def update_priorities_options(selected_priority, selected_combobox, combobox_references):
    # Gather all currently selected values excluding the trigger combobox's value
    selected_values = [cb.get() for cb, cb_val in combobox_references.items() if
                       cb != selected_combobox and cb_val.get() != '']

    # For debugging
    print(f"Selected values excluding current: {selected_values}")

    for cb in combobox_references.values():
        current_value = cb.get()
        available_options = ['A', 'B', 'C', 'D', 'E']

        if cb == selected_combobox:
            # For the triggering combobox, ensure its selected value is included in its options
            cb['values'] = available_options
        else:
            # For all other comboboxes, exclude the selected values
            cb['values'] = [option for option in available_options if option not in selected_values]

        # Correctly retain the current selection if it's still valid
        if current_value not in cb['values']:
            cb.set('')


def update_personal_metatype(priority, personal_metatype, priority_data):
    # Fetch available races for the selected priority
    available_races = list(priority_data[priority]['Races'].keys())

    # Update the personal_metatype ComboBox values
    if personal_metatype is not None:
        personal_metatype['values'] = available_races
        if available_races:
            personal_metatype.set(available_races[0])
        else:
            personal_metatype.set('')
    else:
        print("personal_metatype ComboBox is not initialized.")


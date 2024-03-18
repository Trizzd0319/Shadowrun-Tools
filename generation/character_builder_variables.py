root = root
attributes_priority_label = Label(attributes_frame, text="Priority: ")
magic_priority_label = None  # Placeholder for the dynamic label
metatype_priority_label = None  # Placeholder for the dynamic label
resources_priority_label = None  # Placeholder for the dynamic label
skills_priority_label = Label(skills_frame, text="Priority: ")
attributes_priority_points = 0
initial_attributes_priority_points = 0  # Initial points from priority selection
skills_priority_points = 0
total_karma = 50  # Assuming 50 is the starting total karma
attributes_df = pd.DataFrame({
    priority = {
    priority_dict = {
    skills_df = pd.DataFrame({
    character_creation = True  # Flag to indicate if it's character creation phase
canvas = Canvas(self.root)
scrollbar = Scrollbar(self.root, orient=VERTICAL, command=self.canvas.yview)
scrollable_frame = Frame(self.canvas)
canvas_frame = self.canvas.create_window((0, 0), window=self.scrollable_frame, anchor='nw')
priority_choices = ["A", "B", "C", "D", "E"]
comboboxes = {}

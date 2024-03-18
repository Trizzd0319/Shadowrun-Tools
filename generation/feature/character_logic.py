class CharacterLogic:
    @staticmethod
    def calculate_priority_value(priority_level, priority_dict):
        """
        Calculate the priority value based on the selected priority level.

        Args:
        - priority_level (str): The selected priority level for attributes (A, B, C, D, E).
        - priority_dict (dict): The dictionary containing priority information.

        Returns:
        - int: The priority value corresponding to the selected priority level.
        """
        attribute_priority = priority_dict['ATTRIBUTES']

        # Ensure priority_level is valid
        if priority_level in priority_dict['PRIORITY']:
            index = priority_dict['PRIORITY'].index(priority_level)
            return attribute_priority[index]
        else:
            # Handle invalid priority level gracefully, returning a default value or raising an error
            return None  # Or raise an exception, print a warning, etc.

    @staticmethod
    def increment_attribute_level(var, karma_var, current_value):
        """
        Increment the level of an attribute and deduct the cost from Karma.

        Args:
        - var (IntVar): The tkinter IntVar associated with the attribute level.
        - karma_var (IntVar): The tkinter IntVar associated with Karma.
        - current_value (int): The current value of the attribute level.

        Returns:
        - bool: True if the increment was successful, False otherwise.
        """
        next_level_cost = (current_value + 1) * 5
        if karma_var.get() >= next_level_cost and current_value < 6:
            var.set(current_value + 1)
            karma_var.set(karma_var.get() - next_level_cost)
            return True
        return False

    @staticmethod
    def decrement_attribute_level(var, karma_var, current_value):
        """
        Decrement the level of an attribute and add the cost back to Karma.

        Args:
        - var (IntVar): The tkinter IntVar associated with the attribute level.
        - karma_var (IntVar): The tkinter IntVar associated with Karma.
        - current_value (int): The current value of the attribute level.

        Returns:
        - bool: True if the decrement was successful, False otherwise.
        """
        current_level_cost = current_value * 5
        if current_value > 0:
            var.set(current_value - 1)
            karma_var.set(karma_var.get() + current_level_cost)
            return True
        return False

    @staticmethod
    def increment_skill_level(var, karma_var, current_value):
        """
        Increment the level of a skill and deduct the cost from Karma.

        Args:
        - var (IntVar): The tkinter IntVar associated with the skill level.
        - karma_var (IntVar): The tkinter IntVar associated with Karma.
        - current_value (int): The current value of the skill level.

        Returns:
        - bool: True if the increment was successful, False otherwise.
        """
        next_level_cost = (current_value + 1) * 5
        if karma_var.get() >= next_level_cost and current_value < 6:
            var.set(current_value + 1)
            karma_var.set(karma_var.get() - next_level_cost)
            return True
        return False

    @staticmethod
    def decrement_skill_level(var, karma_var, current_value):
        """
        Decrement the level of a skill and add the cost back to Karma.

        Args:
        - var (IntVar): The tkinter IntVar associated with the skill level.
        - karma_var (IntVar): The tkinter IntVar associated with Karma.
        - current_value (int): The current value of the skill level.

        Returns:
        - bool: True if the decrement was successful, False otherwise.
        """
        current_level_cost = current_value * 5
        if current_value > 0:
            var.set(current_value - 1)
            karma_var.set(karma_var.get() + current_level_cost)
            return True
        return False

    @staticmethod
    def calculate_total_karma_spent(attributes_df, skills_df):
        """
        Calculate the total karma spent on attributes and skills.

        Args:
        - attributes_df (pd.DataFrame): DataFrame containing attribute information.
        - skills_df (pd.DataFrame): DataFrame containing skill information.

        Returns:
        - int: Total karma spent.
        """
        attribute_karma = sum([row['LevelVar'].get() * 5 for _, row in attributes_df.iterrows()])
        skill_karma = sum([row['LevelVar'].get() * 5 for _, row in skills_df.iterrows()])
        return attribute_karma + skill_karma

    @staticmethod
    def calculate_remaining_karma(total_karma, initial_karma):
        """
        Calculate the remaining karma after character creation.

        Args:
        - total_karma (int): Total karma spent.
        - initial_karma (int): Initial karma before character creation.

        Returns:
        - int: Remaining karma.
        """
        return initial_karma - total_karma

    @staticmethod
    def calculate_total_resources(selected_priority, priority_dict):
        """
        Calculate the total resources based on the selected priority.

        Args:
        - selected_priority (str): The selected priority level for resources (A, B, C, D, E).
        - priority_dict (dict): The dictionary containing priority information.

        Returns:
        - int: Total resources.
        """
        resources_priority = priority_dict['RESOURCES']
        if selected_priority in priority_dict['PRIORITY']:
            index = priority_dict['PRIORITY'].index(selected_priority)
            return resources_priority[index]
        else:
            return None

    @staticmethod
    def calculate_total_essence(attributes_df, essence_var):
        """
        Calculate the total essence based on attributes.

        Args:
        - attributes_df (pd.DataFrame): DataFrame containing attribute information.
        - essence_var (IntVar): The tkinter IntVar associated with Essence.

        Returns:
        - float: Total essence.
        """
        total_essence = 6
        total_essence -= attributes_df['Body']['LevelVar'].get() / 3
        total_essence -= attributes_df['Agility']['LevelVar'].get() / 6
        total_essence -= attributes_df['Reaction']['LevelVar'].get() / 6
        total_essence -= attributes_df['Strength']['LevelVar'].get() / 3
        total_essence -= attributes_df['Willpower']['LevelVar'].get() / 3
        total_essence -= attributes_df['Logic']['LevelVar'].get() / 6
        total_essence -= attributes_df['Intuition']['LevelVar'].get() / 6
        total_essence -= attributes_df['Charisma']['LevelVar'].get() / 3
        total_essence -= attributes_df['Edge']['LevelVar'].get() / 6
        essence_var.set(total_essence)
        return total_essence

    # Add more static methods for character logic as needed

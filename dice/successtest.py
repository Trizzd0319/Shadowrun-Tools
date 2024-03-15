import random

class Dice:
    def __init__(self, rolls=1):
        self.rolls = rolls

    def roll(self):
        return sorted([random.randint(1, 6) for _ in range(self.rolls)])

class SuccessTest(Dice):
    def __init__(self, edge_stashed=1):
        super().__init__(1)  # Initialize with a placeholder value for rolls
        self.edge_stashed = edge_stashed
        self.setup_threshold_guide()
        self.threshold = 3  # Default threshold for a success

    def setup_threshold_guide(self):
        self.threshold_guide = {
            1: "\033[92mSimple task, only slightly more difficult than walking and talking.\033[0m",  # Green
            2: "\033[93mMore complex, but still in the range of normal experience.\033[0m",  # Yellow
            3: "Normal starting point for Simple tests. Complicated enough to require skill.\033[0m",  # Red
            4: "More difficult, impressive enough to accomplish.\033[0m",  # Red
            5: "Tricky, the sort of thing only accomplished by those who have worked on their skills.\033[0m",
            # Red
            6: "\033[91mElite-level accomplishment, something that few in the world could pull off.\033[0m",  # Red
            7: "\033[91mStanding out among the elite, demonstrating very rare ability.\033[0m"  # Red
        }

    def print_results_summary(self):
        colored_results = [f"\033[92m{result}\033[0m" if result >= 5 else str(result) for result in self.results]
        print("\nSorted Results (Numeric):", ', '.join(colored_results), f"(Count: {len(self.results)})")
        total_hits = sum(result >= 5 for result in self.results) + sum(result == 6 for result in self.results)
        print("Success: Yes" if total_hits >= self.threshold else "Success: No")
        print("Threshold Required Hits:", self.threshold)
        print("Total Hits:", total_hits)
        print("Number of 5s Rolled:", self.results.count(5))
        print("Total Hits Calculated for Number of 5s:", self.results.count(5))
        print("Number of 6s Rolled:", self.results.count(6))
        print("Total Hits Calculated for Number of 6s:", 2 * self.results.count(6))
        print("Number of 1s Rolled:", self.results.count(1))
        print("Glitch:", "Yes" if self.results.count(1) > len(self.results) / 2 else "No")
        print("Critical Glitch:", "Yes" if self.results.count(1) > len(self.results) / 2 and total_hits == 0 else "No")

    def roll_test(self):
        for key, description in self.threshold_guide.items():
            print(f"{key}: {description}")
        self.update_threshold_from_input()
        # Replace direct input for dice rolls with a call to validate_and_parse_dice_input
        self.results = self.validate_and_parse_dice_input()
        self.print_results_summary()
        # self.rolls = int(input("Enter the total number of dice to roll: "))
        self.edge_stashed = int(input("Enter the total number of edge that you possess: "))
        self.results = self.roll()
        self.print_results_summary()

        # Implement logic to prompt for and handle edge boost selection here...
        # For simplicity, this example does not include detailed edge boost logic.

    def apply_edge_boost(self, edge_choice):
        if edge_choice == 1:  # Example: Reroll one die
            self.reroll_one_die()
        # Placeholder: Implement the logic to apply the chosen edge boost.
        # Make sure to modify 'self.results' as needed based on the edge choice.
        pass

    def reroll_one_die(self):
        die_to_reroll = self.select_die_to_reroll()  # Method to select a die index to reroll
        original_value = self.results[die_to_reroll]
        print(f"Original Roll: {self.colorize_results(die_to_reroll, original_value, 'red')}")
        self.results[die_to_reroll] = random.randint(1, 6)  # Reroll the selected die
        new_value = self.results[die_to_reroll]
        color = 'green' if new_value >= 5 else 'red'
        print(f"New Roll:      {self.colorize_results(die_to_reroll, new_value, color)}")
        # Similar to the provided example, colorize the rerolled die
        pass  # Placeholder for brevity

    # def add_one_to_die(self):
    #     die_to_boost = self.select_die_to_boost()
    #     original_value = self.results[die_to_boost]
    #     print(f"Original Roll: {self.colorize_results(die_to_boost, original_value, 'red')}")
    #     self.results[die_to_boost] += 1
    #     print(f"New Roll:      {self.colorize_results(die_to_boost, self.results[die_to_boost], 'green')}")

    def add_one_to_die(self, roll_results, die_position):
        """Add +1 to a die roll at the specified position under specific conditions, with refined glitch
        evaluation."""
        original_value = roll_results[die_position]
        # Colorize and display the original roll for the specific die
        print(f"Original Roll: {self.colorize_results(die_position, original_value, 'red')}")
        # Check if the die is a 4 and turning it into a 5 would cause a success
        if roll_results[die_position] == 4 and self.threshold <= 5:
            roll_results[die_position] += 1
            # Colorize and display the new roll for the specific die
            print(f"New Roll:      {self.colorize_results(die_position, roll_results[die_position], 'green')}")
            return roll_results

        # For a die that's a 1, evaluate the impact of changing it on glitch scenarios
        if roll_results[die_position] == 1:
            # Determine the current number of 1s and successes
            ones_count = roll_results.count(1)
            successes_count = sum(1 for die in roll_results if die >= self.threshold)

            # Evaluate the impact of incrementing a 1 on potential glitch scenarios
            if ones_count > len(roll_results) // 2:
                # Check if incrementing this 1 would prevent a glitch or critical glitch Note: This simplifies
                # the logic by focusing on the count; detailed game mechanics might require further refinement
                if successes_count == 0 or (successes_count > 0 and ones_count - 1 <= len(roll_results) // 2):
                    roll_results[die_position] += 1

        return roll_results

    # Note: This update introduces a refined evaluation for when incrementing a 1 to a 2 is beneficial, particularly in the context of preventing or mitigating glitches and critical glitches.
    # It's important to validate this logic against the specific rules and scenarios of the game being implemented.

    # We should now consider testing this implementation to ensure it works as expected in various scenarios, including those close to glitch and critical glitch thresholds.

    def buy_automatic_hit(self):
        # Simulate adding an automatic '6' to the results and color it green
        self.results.append(6)  # Adding a hit
        print("Bought an automatic hit: \033[92m6\033[0m")

    def make_6s_explode(self):
        indices_of_6s = [i for i, result in enumerate(self.results) if result == 6]
        for i in indices_of_6s:
            # Each '6' explodes into another roll, color the original '6' green
            print(f"Exploding: {self.colorize_results(i, 6, 'green')}")
            new_roll = random.randint(1, 6)
            self.results.append(new_roll)  # Add the result of the explosion
            if new_roll >= 5:  # If the new roll is a hit, color it green
                print(f"New Hit from Explosion: \033[92m{new_roll}\033[0m")
            else:
                print(f"New Roll from Explosion: {new_roll}")

    def reroll_failed_dice(self):
        failed_dice_indices = [i for i, result in enumerate(self.results) if result < 5]
        for i in failed_dice_indices:
            print(f"Rerolling: {self.colorize_results(i, self.results[i], 'red')}")
            self.results[i] = random.randint(1, 6)
            new_color = 'green' if self.results[i] >= 5 else 'red'
            print(f"New Roll:  {self.colorize_results(i, self.results[i], new_color)}")

    def colorize_results(self, index_to_color, color):
        colors = {'red': '\033[91m', 'green': '\033[92m', 'reset': '\033[0m'}
        colored_results = [f"{colors['green']}{result}{colors['reset']}" if result >= 5 else str(result) for i, result
                           in enumerate(self.results)]
        if index_to_color is not None:
            colored_results[index_to_color] = f"{colors[color]}{self.results[index_to_color]}{colors['reset']}"
        return ', '.join(colored_results)

    def select_die_to_reroll(self):
        # Example method to select a die to reroll. This might involve user input or other logic in a full implementation.
        return 0  # Simplified example: always selects the first die

    def update_threshold_from_input(self):
        input_value = input("Enter new threshold (press Enter to keep current): ").strip()
        if input_value == "":
            # If the user presses Enter without typing anything, keep the current threshold
            print(f"Threshold remains as {self.threshold}.")
        else:
            try:
                new_threshold = int(input_value)
                self.threshold = new_threshold
                print(f"Threshold updated to {self.threshold}.")
            except ValueError:
                # Handle cases where the input cannot be converted to an integer
                print("Invalid input. Please enter a valid integer or press Enter to keep current.")

    @staticmethod
    def validate_and_parse_dice_input():
        while True:
            user_input = input("Enter dice rolls or number of dice to roll (1-6 for each dice): ").strip()
            if " " in user_input or "," in user_input:
                try:
                    dice_rolls = sorted([int(d) for d in user_input.replace(',', ' ').split()])
                except ValueError:
                    print("Invalid input. Please enter numbers only.")
                    continue

                if all(1 <= d <= 6 for d in dice_rolls):
                    return dice_rolls
                else:
                    print("Invalid input. Each dice roll must be between 1 and 6.")
            else:
                try:
                    dice_count = int(user_input)
                    if 1 <= dice_count:
                        return sorted([random.randint(1, 6) for _ in range(dice_count)])
                    else:
                        print("Invalid input. Number of dice must be positive.")
                except ValueError:
                    print("Invalid input. Please enter a valid number.")

        def main():
            dice_rolls = validate_and_parse_dice_input()
            print(f"Dice Rolls: {dice_rolls}")
            # Continue with using dice_rolls for all calculations

if __name__ == "__main__":
    test = SuccessTest(edge_stashed=3)  # Assume the user has 3 edge points available
    test.roll_test()

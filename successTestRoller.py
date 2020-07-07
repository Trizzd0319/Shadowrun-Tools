import random

class Dice:
    """Object that represents a single or multiple six-sided dice"""

    def __init__(self, rolls=1, add=0):
        """Initialize the dice object with default values"""
        self.rolls = rolls
        self.add = add
        self.results = []

    def roll(self, rerolls=0):
        """Perform the dice roll using prescribed values"""
        self.results = [random.randint(1, 6) for _ in range(self.rolls)]
        return self.results

    def set_parameters(self, rolls=None, add=None):
        """Set parameters for the dice"""
        if rolls is not None:
            self.rolls = rolls
        if add is not None:
            self.add = add

class SuccessTest(Dice):
    """Success-test style rolling for ShadowRun (six-sided with hits and misses)"""

    def __init__(self):
        """Set initial values for threshold, total_hits, success, glitch, and critical_glitch"""
        super().__init__(1, 0)  # Calling the constructor of the parent class Dice
        self.threshold = 2
        self.total_hits = 0
        self.success = False
        self.glitch = False
        self.critical_glitch = False
        self.num_5s = 0
        self.num_6s = 0
        self.edge = 3  # Default edge points
        self.threshold_guide = {
            1: "Simple task, only slightly more difficult than walking and talking. Shooting at a nearby building.",
            2: "More complex, but still in the range of normal experience. A task an average person pulls off regularly. Shooting at a nearby building while running.",
            3: "Normal starting point for Simple tests. Complicated enough to require skill. Shadowrunners are expected to be more competent than normal people, which is why game thresholds are based here. Shooting a window out of a nearby building.",
            4: "More difficult, impressive enough to accomplish. Shooting an enemy in the window of a nearby building.",
            5: "Tricky, the sort of thing only accomplished by those who have worked on their skills. Shooting an enemy in the window of a nearby building at minimum range.",
            6: "Elite-level accomplishment, something that few in the world could pull off with any degree of regularity. Shooting an enemy in the window of a building at far range.",
            7: "Standing out among the elite, demonstrating very rare ability. Shooting an enemy in the window of a building at far range while running."
        }
        self.dice_symbols = ["⚀", "⚁", "⚂", "⚃", "⚄", "⚅"]

    def roll_test(self, rerolls=0):
        """Roll the number of dice in a pool and return results"""
        self.total_hits = 0
        self.num_5s = 0
        self.num_6s = 0
        self.glitch = False  # Reset glitch variable
        self.critical_glitch = False
        results = self.roll()

        # Count occurrences of 1s
        num_ones = results.count(1)
        if num_ones > self.rolls / 2:  # If the count of 1s exceeds half the dice pool
            self.glitch = True

        # Reroll lowest die if edge points are used
        if self.edge > 0 and rerolls > 0:
            for _ in range(rerolls):
                min_value = min(results)
                min_index = results.index(min_value)
                results[min_index] = random.randint(1, 6)

        for result in results:
            if result == 5:
                self.num_5s += 1
                self.total_hits += 1
            elif result == 6:
                self.num_6s += 1
                self.total_hits += 2

        # Determine if a critical glitch has occurred
        if self.glitch and self.total_hits == 0:
            self.critical_glitch = True

        return results, self.total_hits

    def run_test(self):
        """Run the success test"""
        num_dice = int(input("Enter the number of dice to roll: "))
        self.rolls = num_dice

        manual_input = input("Do you want to input dice manually? (yes/no): ")
        if manual_input.lower() == "yes":
            while True:
                dice_input = input("Enter the dice separated by spaces or commas: ")
                dice_input = dice_input.replace(",", " ")
                try:
                    dice = [int(die) for die in dice_input.split()]
                    if any(d < 1 or d > 6 for d in dice):
                        print("Invalid input. Numbers must be between 1 and 6.")
                    elif len(dice) > num_dice:
                        print(f"Invalid input. Number of dice provided exceeds the selected number ({num_dice}).")
                    else:
                        break
                except ValueError:
                    print("Invalid input. Please enter integers separated by spaces or commas.")
                    return
            self.rolls = len(dice)
        else:
            self.rolls = num_dice

        print("Threshold Guidelines:")
        for key, value in self.threshold_guide.items():
            print(f"{key}: {value}")

        # Prompt for threshold selection
        selected_threshold = input("Select a threshold from the list (leave blank for default threshold 3): ")
        if selected_threshold.strip() == "":
            self.threshold = 3
        else:
            try:
                self.threshold = int(selected_threshold)
            except ValueError:
                print("Invalid input. Using default threshold of 3.")
                self.threshold = 3

        results, total_hits = self.roll_test()
        sorted_results = sorted(results)  # Sort the results
        unicode_result = " ".join(self.dice_symbols[result - 1] for result in sorted(results))
        numeric_result = " ".join(str(result) for result in sorted_results)
        print("\033[0mSorted Results (Unicode):", unicode_result)
        print("\033[0mSorted Results (Numeric):", numeric_result)

        # Set success based on threshold
        if total_hits >= self.threshold:
            self.success = True
            print("\033[92mSuccess: Yes")
        else:
            self.success = False
            print("\033[91mSuccess: No")

        print("\033[0mSelected Threshold:", self.threshold)
        print("\033[0mTotal Hits:", total_hits)
        print("\033[0mNumber of 5s Rolled:", self.num_5s)
        print("\033[0mTotal Hits Calculated for Number of 5s:", 1 * self.num_5s)
        print("\033[0mNumber of 6s Rolled:", self.num_6s)
        print("\033[0mTotal Hits Calculated for Number of 6s:", 2 * self.num_6s)
        print("\033[0mNumber of 1s Rolled:", results.count(1))  # Display count of 1s
        print("\033[0mGlitch:", "Yes" if self.glitch else "No")
        print("Critical Glitch:", "Yes" if self.critical_glitch else "No")

        # Prompt to use edge and specify number of edge points after showing results
        if not self.success or self.glitch or self.critical_glitch:
            print("\nEdge Chances:")
            for i in range(1, 4):
                chance = 100 * (1 - (5/6) ** (total_hits + i))
                print(f"Chance of Success with {i} edge point(s): {chance:.2f}%")
            use_edge = input("Do you want to use edge? (yes/no): ")
            if use_edge.lower() == "yes":
                edge_points = min(int(input("How many edge points do you want to use? ")), 7)
                results, total_hits = self.roll_test(rerolls=edge_points)

                # Display results after rerolls
                unicode_result = " ".join(self.dice_symbols[result - 1] for result in sorted(results))
                numeric_result = " ".join(str(result) for result in sorted_results)
                print("\033[0mSorted Results (Unicode) After Rerolls:", unicode_result)
                print("\033[0mSorted Results (Numeric) After Rerolls:", numeric_result)
                print("\033[0mTotal Hits After Rerolls:", total_hits)
                print("\033[0mNumber of 5s Rolled After Rerolls:", self.num_5s)
                print("\033[0mNumber of 6s Rolled After Rerolls:", self.num_6s)
                print("\033[0mNumber of 1s Rolled After Rerolls:", results.count(1))  # Display count of 1s
                print("\033[0mGlitch After Rerolls:", "Yes" if self.glitch else "No")
                print("Critical Glitch After Rerolls:", "Yes" if self.critical_glitch else "No")
                if total_hits >= self.threshold:
                    print("\033[92mSuccess: Yes")
                else:
                    print("\033[91mSuccess: No")
            else:
                print("No edge used. End of test.")

if __name__ == "__main__":
    test = SuccessTest()
    test.run_test()

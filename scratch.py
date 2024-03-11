import random

class Dice:
    """Object that represents a single or multiple six-sided dice"""

    def __init__(self, rolls=1, add=0):
        """Initialize the dice object with default values"""
        self.rolls = rolls
        self.add = add
        self.results = []

    def roll(self):
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
        self.threshold = 3
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

    def roll_test(self, rerolls=0, reroll_5_edge=False):
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

        # Rerolling all failed dice for 5-edge boost
        if reroll_5_edge:
            print("\nRerolling all failed dice...")
            reroll_indices = [i for i, result in enumerate(results) if result < 5]
            print("Reroll Dice:", [results[i] for i in reroll_indices])
            for i in reroll_indices:
                results[i] = random.randint(5, 6)
            print("Replacement Dice:", [results[i] for i in reroll_indices])

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

        # Calculate percentage increase towards success
        initial_success_chance = 100 * (1 - (5 / 6) ** self.total_hits)
        final_success_chance = 100 * (1 - (5 / 6) ** (self.total_hits + rerolls))
        success_increase_percent = final_success_chance - initial_success_chance

        return results, success_increase_percent

    def run_test(self):
        """Run the success test"""
        num_dice = int(input("Enter the number of dice to roll: "))
        self.rolls = num_dice
        print("Threshold Guidelines:")
        for key, value in self.threshold_guide.items():
            print(f"{key}: {value}")

        # Prompt for threshold selection
        selected_threshold = input("Select a threshold from the list (leave blank for default threshold 3): ")
        if selected_threshold == "":
            self.threshold = 3
        else:
            self.threshold = int(selected_threshold)

        results, total_hits = self.roll_test()

        sorted_results = sorted(results)  # Sort the results
        print("\nSorted Results (Numeric):", ', '.join(map(str, sorted_results)), f"(Count: {len(sorted_results)})")
        print("Success: Yes" if total_hits >= self.threshold else "Success: No")
        print("Threshold Required Hits:", self.threshold)
        print("Total Hits:", total_hits)
        print("Number of 5s Rolled:", self.num_5s)
        print("Total Hits Calculated for Number of 5s:", 1 * self.num_5s)
        print("Number of 6s Rolled:", self.num_6s)
        print("Total Hits Calculated for Number of 6s:", 2 * self.num_6s)
        print("Number of 1s Rolled:", results.count(1))  # Display count of 1s
        print("Glitch:", "Yes" if self.glitch else "No")
        print("Critical Glitch:", "Yes" if self.critical_glitch else "No")

        # Prompt to use edge and specify number of edge points after showing results
        if not self.success or self.glitch or self.critical_glitch:
            print("\nEdge Chances:")
            for i in range(1, min(self.edge + 1, 6)):  # Consider edge boost options up to available edge points
                if i == 1:
                    print(f"{i}-Edge Boost: Reroll one die")
                elif i == 2:
                    print(f"{i}-Edge Boost: +1 to a single die roll")
                elif i == 3:
                    print(f"{i}-Edge Boost: Buy one automatic hit")
                elif i == 4:
                    print(f"{i}-Edge Boost: Add Edge to your dice pool")
                else:
                    print(f"{i}-Edge Boost: Reroll all failed dice")
                chance = 100 * (1 - (5 / 6) ** (total_hits + i))
                print(f"Chance of Success with {i} edge point(s): {chance:.2f}%")
            use_edge = input("Do you want to use edge? (yes/no/edge number): ").lower()
            if use_edge == "yes":
                edge_points = min(int(input("How many edge points do you want to use? ")), 5)
                if edge_points > 0:
                    if edge_points == 1:
                        print("\nRerolling one die...")
                    elif edge_points == 2:
                        print("\nAdding +1 to a single die roll...")
                    elif edge_points == 3:
                        print("\nBuying one automatic hit...")
                    elif edge_points == 4:
                        print("\nAdding Edge to your dice pool...")
                    else:
                        print("\nRerolling all failed dice...")
                    rerolls = 0
                    reroll_5_edge = False
                    if edge_points == 1:
                        rerolls = 1
                    elif edge_points == 2:
                        rerolls = 1
                        results[results.index(min(results))] += 1
                        total_hits += 1
                    elif edge_points == 3:
                        total_hits += 1
                    elif edge_points == 4:
                        self.edge += 1
                    else:
                        reroll_5_edge = True
                    results, total_hits, success_increase_percent = self.roll_test(rerolls, reroll_5_edge)
                    print("\nAfter using edge:")
                    print("Sorted Results (Numeric):", ', '.join(map(str, sorted(results))), f"(Count: {len(sorted(results))})")
                    print("Success: Yes" if total_hits >= self.threshold else "Success: No")
                    print("Threshold Required Hits:", self.threshold)
                    print("Total Hits:", total_hits)
                    print("Number of 5s Rolled:", self.num_5s)
                    print("Total Hits Calculated for Number of 5s:", 1 * self.num_5s)
                    print("Number of 6s Rolled:", self.num_6s)
                    print("Total Hits Calculated for Number of 6s:", 2 * self.num_6s)
                    print("Number of 1s Rolled:", results.count(1))  # Display count of 1s
                    print("Glitch:", "Yes" if self.glitch else "No")
                    print("Critical Glitch:", "Yes" if self.critical_glitch else "No")
                    if self.edge > 0:
                        print("Percentage Increase towards Success:", f"{success_increase_percent:.2f}%")
            elif use_edge.isdigit():
                edge_points = min(int(use_edge), 5)
                if edge_points > 0:
                    if edge_points == 1:
                        print("\nRerolling one die...")
                    elif edge_points == 2:
                        print("\nAdding +1 to a single die roll...")
                    elif edge_points == 3:
                        print("\nBuying one automatic hit...")
                    elif edge_points == 4:
                        print("\nAdding Edge to your dice pool...")
                    else:
                        print("\nRerolling all failed dice...")
                    rerolls = 0
                    reroll_5_edge = False
                    if edge_points == 1:
                        rerolls = 1
                    elif edge_points == 2:
                        rerolls = 1
                        results[results.index(min(results))] += 1
                        total_hits += 1
                    elif edge_points == 3:
                        total_hits += 1
                    elif edge_points == 4:
                        self.edge += 1
                    else:
                        reroll_5_edge = True
                    results, total_hits, success_increase_percent = self.roll_test(rerolls, reroll_5_edge)
                    print("\nAfter using edge:")
                    print("Sorted Results (Numeric):", ', '.join(map(str, sorted(results))), f"(Count: {len(sorted(results))})")
                    print("Success: Yes" if total_hits >= self.threshold else "Success: No")
                    print("Threshold Required Hits:", self.threshold)
                    print("Total Hits:", total_hits)
                    print("Number of 5s Rolled:", self.num_5s)
                    print("Total Hits Calculated for Number of 5s:", 1 * self.num_5s)
                    print("Number of 6s Rolled:", self.num_6s)
                    print("Total Hits Calculated for Number of 6s:", 2 * self.num_6s)
                    print("Number of 1s Rolled:", results.count(1))  # Display count of 1s
                    print("Glitch:", "Yes" if self.glitch else "No")
                    print("Critical Glitch:", "Yes" if self.critical_glitch else "No")
                    if self.edge > 0:
                        print("Percentage Increase towards Success:", f"{success_increase_percent:.2f}%")

# Run the SuccessTest class
success_test = SuccessTest()
success_test.run_test()

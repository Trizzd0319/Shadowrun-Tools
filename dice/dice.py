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
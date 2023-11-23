"""
This module contain a class with DrawingMachine
that is capable to constantly draw numbers from machine capsule.
"""
import random


class DrawingMachine:
    """
    It's a machine that drawing numbers from the numbers machine.
    """

    def __init__(self):
        self.number_range = range(1, 50)

    def machine_draw(self):

        """
        The machine_draw function is a function that draws 6 random numbers from the number_range list.
        It does this by using the random.choice() method, which chooses a random element from a non-empty sequence.

        :param self: Make the function a method of the class
        :return: A list of 6 random numbers
        :doc-author: Trelent
        """
        counter = 6
        chosen_numbers = set()
        while counter != 0:
            drawed = random.choice(self.number_range)
            chosen_numbers.add(drawed)
            counter -= 1

        return list(chosen_numbers)

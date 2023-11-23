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
    The machine_draw function is a function that
    randomly chooses 6 numbers from the number_range list.
    It then appends those chosen numbers to the chosen_numbers list and returns it.

    :param self: Access the attributes and methods of the class
    :return: A list of 6 random numbers
    """
        counter = 6
        chosen_numbers = []
        while counter != 0:
            drawed = random.choice(self.number_range)
            chosen_numbers.append(drawed)
            counter -= 1

        return chosen_numbers

"""
Module that actually gather data from drawing_machine and lottery_ticket,
compares it and gives report.
"""
from math import ceil
from datetime import date
from drawing_machine import DrawingMachine
from lottery_ticket import LotteryTicket


class TotaliserCheck:
    """
    Class that making all calculations, just as you would visit
    a store where you can check your coupon at the dedicated machine.
    """

    def __init__(self, lottery_ticket: LotteryTicket, drawing_machine: DrawingMachine):
        self.lottery_ticket = lottery_ticket
        self.drawing_machine = drawing_machine

    def comparison_of_numbers(self):

        """
        The comparison_of_numbers function compares the chosen numbers with the drawed numbers.
        It returns a counter which counts how many times
        it takes to get all of the chosen numbers in order.

        :param self: Access the attributes of the class
        :return: The number of attempts it took to match the chosen_numbers with the drawed_numbers
        :doc-author: Trelent
        """
        chosen_numbers = self.lottery_ticket.what_numbers()
        chosen_numbers.sort()
        counter = 0
        while True:
            drawed_numbers = self.drawing_machine.machine_draw()
            counter += 1
            drawed_numbers.sort()
            if chosen_numbers == drawed_numbers:
                return counter

        # print(drawed_numbers)

    def raport(self):
        """
        The raport function is used to print a raport
        about the number of tries and how much money you would spent on it.
        It also shows how long it would take to win if there are 3 drawing per week.

        :param self: Represent the instance of the class
        :param counter: Count the number of tries
        :return: A string with a few variables
        :doc-author: Trelent
        """
        counter = self.comparison_of_numbers()
        today = date.today()
        today.strftime('%Y-%m-%d')
        days = ceil(counter / 3 * 7)

        report = (f"You've hit 6 at {counter:,} try\nYou would spent on it {counter * 3:,} USD\n"
                  f"If there are 3 drawings per week,\n"
                  f"you would won in about {ceil(days / 365)} years from today.\n")

        return report

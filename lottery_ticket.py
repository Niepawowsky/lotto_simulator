"""
Here player can cross his numbers on coupon
"""

class LotteryTicket:
    """
    It's a class that represents coupon customer can buy and cross his numbers
    """

    def __init__(self):
        self.numbers = []

    def what_numbers(self):

        """
        The what_numbers function asks the user to input 6 numbers from 1 to 49.
        The function checks if the number is in range
        and then appends it to a list to pass it farther.

        :param self: Refer to the instance of the class
        :return: A list of numbers
        """
        counter = 1
        possible_numbers = range(1, 50)
        while counter != 7:
            happy_numbers = int(input(f'Give me number {counter}: ') or 0)
            if happy_numbers not in possible_numbers or happy_numbers == ValueError:
                print('You should choose number from 1 to 49')
            elif happy_numbers in self.numbers:
                print('Number already chosen')
            else:
                counter += 1
                self.numbers.append(happy_numbers)
        return self.numbers

from drawing_machine import DrawingMachine
from lottery_ticket import LotteryTicket
from totaliser_check import TotaliserCheck


if __name__ == '__main__':
    lottery_ticket = LotteryTicket()
    drawing_machine = DrawingMachine()
    turn_on = TotaliserCheck(lottery_ticket, drawing_machine)
    print(turn_on.raport())



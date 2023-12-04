import re
from .day import Day
from parse import parse

class Day4(Day):
    def __init__(self, day=4):
        super().__init__(day)

    def do_part_1(self, input = None):
        print(f"[PART 1]: Running part 1...")
        if input is None:
            input = self.get_input(1)
            
        pattern = re.compile(r'Card\s+(\d+):\s+(.*)\s+\|\s+(.*)')
        l = [pattern.match(i).groups() for i in input if pattern.match(i)]
        correctGames = []
        for game, own, actual in l:
            numOwn = own.split(' ')
            numAct = actual.split(' ')
            correct = 0
            for num in numOwn:
                if num.isdigit():
                    if num in numAct:
                        if correct > 0:
                            correct *= 2
                        else:
                            correct += 1
            correctGames.append(correct) 
        print(sum(correctGames))
        return f'{sum(correctGames)}'

    def do_part_2(self, input=None):
        print(f"[PART 2]: Running part 2...")
        return None
    def do_test(self, partNumber):
        return super().do_test(partNumber)
    def get_input(self, partNumber: int):
        return super().get_input(partNumber)
    def parse_input(self, partNumber: int):
        return super().parse_input(partNumber)



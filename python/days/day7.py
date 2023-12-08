from parse import parse
from .day import Day

class Day7(Day):
    def __init__(self, day=7):
        super().__init__(day)

    def get_input(self, part_number: int):
        with open(self.inputLocation + str(part_number) + ".txt") as file:
            return file.readlines()

    def parse_input(self, data, face):
        bests = []
        for line in data:
            hand, bid = line.split()
            hand = hand.translate(str.maketrans('TJQKA', face))
            best = max(self.entropy(hand.replace('0', r)) for r in hand)
            bests.append((best, hand, int(bid)))
        return enumerate(sorted(bests), start=1)


    def entropy(self, hand):
        en = list(map(hand.count, hand))
        return sorted(en, reverse=True)

    def do_part_1(self, input_=None):
        print(f"[PART 1]: Running part 1...")
        if input_ is None:
            input_ = self.get_input(1)
        face = 'ABCDE'
        data = self.parse_input(input_, face)
        res  = 0
        for rank, (*_, bid) in data:
            res += rank * bid
            

        print(res)
        return str(res)

    def do_part_2(self, input_=None):
        print(f"[PART 2]: Running part 2...")
        if input_ is None:
            input_ = self.get_input(2)
        face = 'A0CDE'
        data = self.parse_input(input_, face)
        res  = 0
        for rank, (*_, bid) in data:
            res += rank * bid

        print(res)
        return str(res)

    def do_test(self, part_number):
        return super().do_test(part_number)

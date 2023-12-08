from parse import parse
from .day import Day

class Day7(Day):
    def __init__(self, day=7):
        super().__init__(day)
        self.cards = {"A": 14, "K": 13, "Q": 12, "J": 11}

    def get_input(self, part_number: int):
        with open(self.inputLocation + str(part_number) + ".txt") as file:
            return file.readlines()
    
    def compare_smaller_than(self, c1, c2):
        if not c1.isdigit():
            c1 = self.cards[c1]
        if not c2.isdigit():
            c2 = self.cards[c2]
        if c1  == c2:
            return None
        return c1 < c2
    
    def all_of_a_kind(self, cards):
        return list(set(cards)) == cards
        
    def n_of_a_kind(self, cards):
        for i in range(len(cards)):
            ncards = cards.pop(i)
            print(ncards)
        

    def parse_input(self, data):
        hand_bid_pairs = [d.split(' ') for d in data]
        
        return #

    def do_part_1(self, input_=None):
        print(f"[PART 1]: Running part 1...")
        if input_ is None:
            input_ = self.get_input(1)
        
        print(None)
        return str(None)

    def do_part_2(self, input_=None):
        print(f"[PART 2]: Running part 2...")
        if input_ is None:
            input_ = self.get_input(2)

        print(None)
        return str(None)

    def do_test(self, part_number):
        return super().do_test(part_number)

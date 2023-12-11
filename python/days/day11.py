import itertools
from parse import parse
from .day import Day

class Day11(Day):
    def __init__(self, day=11):
        super().__init__(day)

    def get_input(self, part_number: int):
        with open(self.inputLocation + str(part_number) + ".txt") as file:
            return file.readlines()

    def parse_input(self, data, part_number: int = 1):
        empty_rows = [i for i,row in enumerate(data) if all(space == "." for space in row)]
        empty_cols = [i for i in range(len(data[0])) if all(row[i] == "." for row in data)]
        print(empty_cols)
        print(empty_rows)
        coords = [(erow, ecol) for line, erow in zip(data, empty_rows)
              for c, ecol in zip(line, empty_cols) if c == '#']
        return coords
    
    def mnh_distance(g1, g2):
        x1,y1 = g1
        x2,y2 = g2
        return abs(x1 - x2) + abs(y1 - y2)

    def do_part_1(self, input_=None):
        print(f"[PART 1]: Running part 1...")
        if input_ is None:
            input_ = self.get_input(1)
 
        coords = self.parse_input(input_)
        print(coords)
        res = sum(self.mnh_distance(galaxy1, galaxy2) for (galaxy1, galaxy2) in itertools.combinations(coords, 2))
        print(res)
        return str(res)

    def do_part_2(self, input_=None):
        print(f"[PART 2]: Running part 2...")
        if input_ is None:
            input_ = self.get_input(2)

        print(None)
        return str(None)

    def do_test(self, part_number):
        return super().do_test(part_number)

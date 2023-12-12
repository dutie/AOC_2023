import itertools
import numpy as np
from parse import parse
from .day import Day

class Day11(Day):
    def __init__(self, day=11):
        super().__init__(day)

    def get_input(self, part_number: int):
        with open(self.inputLocation + str(part_number) + ".txt") as file:
            return file.readlines()

    def parse_input(self, data, expansion: int = 1):
        # I first forgot about accumulate.
        # empty_rows = list(map(lambda x: sum(x[1]), enumerate(map(lambda row: 1 if all(space == "." for space in row) else 0, data))))
        empty_rows = list(itertools.accumulate([1 if "#" not in row else 0 for row in data]))
        empty_cols = list(itertools.accumulate([1 if all(row[i] == "." for row in data) else 0 for i in range(len(data[0]))]))
        coords = [(erow+(empty_rows[erow]*expansion), ecol+(empty_cols[ecol]*expansion)) for erow, line in enumerate(data) for ecol, col in enumerate(line) if col == '#']
        return coords
    
    def mnh_distance(self, g1, g2):
        x1,y1 = g1
        x2,y2 = g2
        return abs(x1 - x2) + abs(y1 - y2)

    def do_part_1(self, input_=None):
        print(f"[PART 1]: Running part 1...")
        if input_ is None:
            input_ = self.get_input(1)
        coords = self.parse_input(input_)
        res = sum(self.mnh_distance(galaxy1, galaxy2) for (galaxy1, galaxy2) in itertools.combinations(coords, 2))
        print(res)
        return str(res)

    def do_part_2(self, input_=None):
        print(f"[PART 2]: Running part 2...")
        if input_ is None:
            input_ = self.get_input(2)
        coords = self.parse_input(input_, 1000000-1)
        res = sum(self.mnh_distance(galaxy1, galaxy2) for (galaxy1, galaxy2) in itertools.combinations(coords, 2))
        print(res)
        return str(res)

    def do_test(self, part_number):
        return super().do_test(part_number)

import math
from parse import parse
from .day import Day

class Day12(Day):
    def __init__(self, day=12):
        super().__init__(day)

    def get_input(self, part_number: int):
        with open(self.inputLocation + str(part_number) + ".txt") as file:
            return file.readlines()

    def grouped(self, dupId, rowId, tup):
        row, dup = tup
        if dupId >= len(dup):
            if rowId < len(row) and '#' in row[dupId:]:
                return 0
            return 1
        if rowId >= len(row):
            return 0

        res = None
        groups = dup[dupId]
        char = row[rowId]
        if char == '.':
            res = self.grouped(dupId, rowId + 1, (row, dup))
        elif char == '#':
            if '.' not in row[rowId:rowId + groups] and row[rowId + groups] != "#":
                res = self.grouped(dupId + 1, rowId + groups + 1, (row, dup))
            else:
                res = 0
        elif char == '?':
            if '.' not in row[rowId:rowId + groups] and row[rowId + groups] != "#":
                res = self.grouped(dupId + 1, rowId + groups + 1, (row, dup))
            else:
                res = self.grouped(dupId, rowId + 1, (row, dup))
        return res

    def parse_input(self, data, part_number: int = 1):
        tuples = [(row + ".", eval(dup)) for line in data for row, dup in [line.split(' ')]]
        res = sum(list(map(lambda tuple: self.grouped(0, 0, tuple), tuples)))
        return res

    def do_part_1(self, input_=None):
        print(f"[PART 1]: Running part 1...")
        if input_ is None:
            input_ = self.get_input(1)
        res = self.parse_input(input_)
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

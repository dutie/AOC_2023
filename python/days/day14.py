from functools import cache
import numpy as np
from parse import parse
from .day import Day

class Day14(Day):
    def __init__(self, day=14):
        super().__init__(day)
        self.max = 11

    def get_input(self, part_number: int):
        with open(self.inputLocation + str(part_number) + ".txt") as file:
            return file.readlines()

    def calc_total(self, ncol, j):
        row = j + 1
        cur_range = range(row-len(ncol)+1, self.max)
        return sum(map(lambda tup: tup[0] * tup[1], zip(ncol, cur_range)))

    def parse_input(self, data, part_number: int = 1):
        self.max = len(data) + 1
        total = 0
        for i, col in enumerate(list(zip(*data))):
            ncol = []
            for j, val in enumerate(col[::-1]):
                if val == "O":
                    ncol.append(1)
                elif val == "#":
                    if ncol != []:
                        total += self.calc_total(ncol, j-1)
                        ncol = []
            total += self.calc_total(ncol, j)
        return total
    
    @cache
    def move_north(self,rock_map: tuple[str]) -> tuple[str]:
        rock_map = list(rock_map)
        for y, row in enumerate(rock_map):
            for x, char in enumerate(row):
                if char != 'O':  # skip non-moving rocks
                    continue
                obstacles_y = [y for y in range(y) if rock_map[y][x] in '#O']
                new_y = max(obstacles_y, default=-1) + 1
                if new_y != y:
                    rock_map[y] = rock_map[y][:x] + '.' + rock_map[y][x+1:]
                    rock_map[new_y] = rock_map[new_y][:x]+'O'+rock_map[new_y][x+1:]
        return tuple(rock_map)


    @cache
    def turn_clockwise(self,rock_map: tuple[str]) -> tuple[str]:
        return tuple(''.join(row) for row in zip(*rock_map[::-1]))


    @cache
    def thousand_cycles(self,rock_map: tuple[str]) -> tuple[str]:
        for _ in range(4):
            rock_map = self.move_north(rock_map)
            rock_map = self.turn_clockwise(rock_map)
        return rock_map


    def calculate_load(self,rock_map: tuple[str]) -> int:
        height = len(rock_map)
        return sum(row.count('O') * (height - y) for y, row in enumerate(rock_map))

                    

    def do_part_1(self, input_=None):
        print(f"[PART 1]: Running part 1...")
        if input_ is None:
            input_ = self.get_input(1)
        data = self.parse_input(input_)
        print(data)
        return str(data)

    def do_part_2(self, input_=None):
        print(f"[PART 2]: Running part 2...")
        if input_ is None:
            input_ = self.get_input(2)
        data = [line.strip() for line in input_]
        rock_map = tuple(data)
        acc = []
        for i in range(1_000_000_000):
            rock_map = self.thousand_cycles(rock_map)
            acc.append(self.calculate_load(rock_map))
            for cs in range(2,100):
                c = acc[-cs:]
                if acc[-cs*2:-cs] == c:
                    rem = 1_000_000_000 - i - 2
                    final_load = c[rem % cs]
                    


                    print(final_load)
                    return str(final_load)

    def do_test(self, part_number):
        return super().do_test(part_number)

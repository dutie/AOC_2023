from typing import List, Tuple
from parse import parse
from .day import Day

class Day18(Day):
    def __init__(self, day=18):
        super().__init__(day)
        self.dict_parse = {"R": (1,0), "D": (0,1), "L": (-1,0), "U": (0,-1)}

    def get_input(self, part_number: int):
        with open(self.inputLocation + str(part_number) + ".txt") as file:
            return file.readlines()
        
    def print_grid(self, dr, cur, num, all_steps, grid):
        print(f"From {cur} in dir {dr} to {num}: {all_steps}")
        for row in grid:
            print(row)

    def outer(self, cur: Tuple[int], step: Tuple[str], grid: List[List[str]]):
        dr, num, col = step
        cur_dir = self.dict_parse[dr]
        all_steps = [(cur[0] + i*cur_dir[0], cur[1]+ i*cur_dir[1]) for i in range(int(num)+1)]
        for astep in all_steps:
            grid[astep[1]][astep[0]] = '#'
        print("+"*100)
        self.print_grid(dr, cur, num, all_steps, grid)
        return all_steps[-1]
        


    def parse_input(self, data, part_number: int = 1):
        data =  [line.split(' ') for line in data]
        cur = (0,0)
        grid = [['.' for _ in range(10)] for _ in range(10)]
        for step in data:
            cur = self.outer(cur, step, grid)
        
        print()
        print()
        print(grid)

    def do_part_1(self, input_=None):
        print(f"[PART 1]: Running part 1...")
        if input_ is None:
            input_ = self.get_input(1)
        data = self.parse_input(input_)
        print(data)
        return str(None)

    def do_part_2(self, input_=None):
        print(f"[PART 2]: Running part 2...")
        if input_ is None:
            input_ = self.get_input(2)

        print(None)
        return str(None)

    def do_test(self, part_number):
        return super().do_test(part_number)

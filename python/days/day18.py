from itertools import pairwise
from typing import List, Tuple
from parse import parse
from .day import Day

class Day18(Day):
    def __init__(self, day=18):
        super().__init__(day)
        self.dict_parse = {"R": (1+0j), "D": (0+1j), "L": (-1+0j), "U": (0-1j)}
    def get_input(self, part_number: int):
        with open(self.inputLocation + str(part_number) + ".txt") as file:
            return file.readlines()
    
    def surface(self, vertices) -> int:
        vertices.append(vertices[0])
        interior = abs(sum(int(a.real * b.imag - a.imag*b.real) for a,b in pairwise(vertices)) // 2)
        edge = sum(int(abs(a-b)) for a,b in pairwise(vertices))// 2
        return interior + edge + 1


    def do_part_1(self, input_=None):
        print(f"[PART 1]: Running part 1...")
        if input_ is None:
            input_ = self.get_input(1)
        # data = self.parse_input(input_)
        # print(data)
        # return str(data)
        cur = 0 + 0j
        acc = [cur]
        for line in input_:
            dr, num, _ = line.split()
            step = self.dict_parse[dr]
            cur += int(num) * step
            acc.append(cur)
        res = self.surface(acc)
        print(res)
        return str(res)
    def do_part_2(self, input_=None):
        print(f"[PART 2]: Running part 2...")
        if input_ is None:
            input_ = self.get_input(2)
        cur = 0 + 0j
        acc = [cur]
        for line in input_:
            _, _, col = line.split()
            num = int(col[2:7], 16)
            li = "RDLU"
            step = self.dict_parse[li[int(col[-2])]]
            cur += int(num) * step
            acc.append(cur)
        res = self.surface(acc)
        print(res)
        return str(res)
    def do_test(self, part_number):
        return super().do_test(part_number)
    
    def print_grid(self, grid):
        for row in grid:
            print(row)
    def outer(self, cur: Tuple[int], step: Tuple[str], grid: List[List[str]]):
        dr, num, col = step
        cur_dir = self.dict_parse[dr]
        all_steps = [(cur[0] + i*cur_dir[0], cur[1]+ i*cur_dir[1]) for i in range(int(num)+1)]
        for astep in all_steps:
            grid[astep[1]][astep[0]] = '#'
        return all_steps[-1]
    def parse_input(self, data, part_number: int = 1):
        data =  [line.split(' ') for line in data]
        cur = (0,0)
        grid = [['.' for _ in range(10)] for _ in range(10)]
        
        surface_area = 0
        fence = 0

        for step in data:
            cur = self.outer(cur, step, grid)
        self.print_grid(grid)
        return surface_area, fence
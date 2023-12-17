import numpy as np
from parse import parse
from .day import Day

class Day13(Day):
    def __init__(self, day=13):
        super().__init__(day)

    def get_input(self, part_number: int):
        with open(self.inputLocation + str(part_number) + ".txt") as file:
            return file.read().split("\n\n")
        
    def parse_input(self, data, part_number: int = 1):
        grid = data.splitlines()
        return grid 
    
    def parse_test(self, data):
        lines = []
        cur = []
        for line in data:
            if 'N' in line:
                lines.append(cur)
                cur = []
            else:
                cur.append(line)
        lines.append(cur)
        return lines
    
    def smudge(self, above, below):
        cnt = 0
        for i in range(len(above)):
            if cnt > 1:
                return False
            if above[i] != below[i]:
                cnt += 1
                above[i] = below[i]
        if cnt == 1:
            return True
        return False


    
    def find_mirror_smudge(self, grid):
        res = []
        for r in range(1, len(grid)):
            above = grid[:r][::-1]
            below = grid[r:]
            
            above = above[:len(below)]
            below = below[:len(above)]
            
            if above == below or self.smudge(above, below):
                res.append(r)
        
        return res

    def find_mirror(self, grid):
        for r in range(1, len(grid)):
            above = grid[:r][::-1]
            below = grid[r:]
            
            above = above[:len(below)]
            below = below[:len(above)]
            
            if above == below:
                return r
        
        return 0
    def do_part_1(self, input_=None):
        print(f"[PART 1]: Running part 1...")
        if input_ is None:
            input_ = self.get_input(1)
            grids = list(map(self.parse_input, input_))
        else:
            grids = self.parse_test(input_)

        total = 0
        for grid in grids:

            row = self.find_mirror(grid)
            total += row * 100

            col = self.find_mirror(list(zip(*grid)))
            total += col

        print(total)
        return str(total)

    def do_part_2(self, input_=None):
        print(f"[PART 2]: Running part 2...")
        if input_ is None:
            input_ = self.get_input(2)
            grids = list(map(self.parse_input, input_))
        else:
            grids = self.parse_test(input_)
        
        rows = []
        cols = []
        for grid in grids:

            rows.extend(self.find_mirror_smudge(grid))

            cols.extend(self.find_mirror_smudge(list(zip(*grid))))
        print(rows)
        print(cols)

        total = sum(row * 100 for row in rows) + sum(cols)
        print(total)
        return str(total)

    def do_test(self, part_number):
        return super().do_test(part_number)

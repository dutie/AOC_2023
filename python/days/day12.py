import math
from parse import parse
from .day import Day

class Day12(Day):
    def __init__(self, day=12):
        super().__init__(day)

    def get_input(self, part_number: int):
        with open(self.inputLocation + str(part_number) + ".txt") as file:
            return file.readlines()

    def grouped(self, tup):
        row, dup = tup
        dupId = 0
        tempPos = [0,0]
        charId = 0
        combs = 0
        print()
        while charId < len(row) and dupId < len(dup):
            print(f"ROW: {row} {dup}")
            spacing = " "*(5+charId)
            print(f"{spacing}^ {dupId}:{dup[dupId]}")
            char = row[charId]
            if char == "#":
                tempPos[0] += 1
            if char == "?":
                tempPos[1] += 1
            if char == "." or charId == len(row) - 1:
                if tempPos[1] > 0:
                    for remDup in range(len(dup) - dupId):
                    # combs += math.factorial(n) / (math.factorial(r)*(n-math.factorial(r)))
                        r = dup[dupId+remDup] - tempPos[0] # '#.#.??' 1
                        n = tempPos[1]
                        combs += math.comb(n+r-1, r)
                dupId += 1
                tempPos = [0,0]
            charId += 1
                    
     
        return combs
                
    def parse_input(self, data, part_number: int = 1):
        tuples = [(row, eval(dup)) for line in data for row, dup in [line.split(' ')]]
        res = list(map(self.grouped, tuples))
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

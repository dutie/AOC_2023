from math import ceil, floor, sqrt
import re
from parse import parse
from .day import Day

class Day6(Day):
    def __init__(self, day=6):
        super().__init__(day)
        
    def get_input(self, partNumber: int):
        return super().get_input(partNumber)

    def parse_input_1(self, data):
        # times, distances = (re.findall(r'\d+', line) for line in data)
        time = [int(d) for d in data[0].split(":")[1].strip().split(" ") if d.isdigit()]
        dist = [int(d) for d in data[1].split(":")[1].strip().split(" ") if d.isdigit()]
        return zip(time, dist)
    
    def parse_input_2(self, data):
        time, distance = (int(d.split(":")[1].replace(" ", "")) for d in data)
        return time, distance
    
    def citardauq(self, b, c):
        a = -1
        sroot = sqrt(b**2-4*a*c)
        x_1 = ceil(2*c / (-b - sroot))
        x_2 = floor(2*c / (-b + sroot))
        return x_1, x_2
    def quadratic(self, b, c):
        sroot = sqrt(b**2 - 4 * c)
        x_1   =(-b+sroot) / 2
        x_2   = (-b-sroot) / 2
        offset = int(x_1 == x_2 // 1 and x_1 == x_2 // 1) * 2
        res = abs(floor(x_2) - ceil(x_1) - offset + 1)
        return res

    def do_part_1(self, input_=None):
        print(f"[PART 1]: Running part 1...")
        if input_ is None:
            input_ = self.get_input(1)
        data = self.parse_input_1(input_)
        wins = 1
        for time, distance in data:
            # x_1, x_2 = self.citardauq(time,win)
            num_wins = self.quadratic(time, distance)
            wins *= num_wins

        print(wins)
        return str(wins)

    def do_part_2(self, input_=None):
        print(f"[PART 2]: Running part 2...")
        if input_ is None:
            input_ = self.get_input(2)
        time, distance = self.parse_input_2(input_)
        num_wins = self.quadratic(time, distance)
        
        
        
        print(num_wins)
        return str(num_wins)

    def do_test(self, part_number):
        return super().do_test(part_number)

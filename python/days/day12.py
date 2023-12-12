from functools import cache
import math
from parse import parse
from .day import Day

class Day12(Day):
    def __init__(self, day=12):
        super().__init__(day)

    def get_input(self, part_number: int):
        with open(self.inputLocation + str(part_number) + ".txt") as file:
            return file.readlines()
        
    def base_case(self, groups, record):
        if len(groups) == 0:
            return 1 if '#' not in record else 0
        if sum(groups) + len(groups) - 1 > len(record):
            return 0
    def body(self, groups, record): 
        if record[0] == '.':
            return self.find_groups( record[1:], groups)

        combinations = 0
        if record[0] == '?':
            combinations += self.find_groups( record[1:], groups)

        if '.' not in record[:groups[0]] and (len(record) <= groups[0] or len(record) > groups[0] and record[groups[0]] != '#'):
                combinations += self.find_groups( record[groups[0]+1:], groups[1:]   )
        return combinations
    
    @cache
    def find_groups(self, record, groups ):
        b = self.base_case(groups, record)
        if b is not None:
            return b
        
        combinations = self.body(groups, record)
        if combinations is not None:
            return combinations
    def find_groups_tabulation(self, record, groups):
        # NOT YET WORKING
        dp = [[-1] * (len(record) + 1) for _ in range(len(groups) + 1)]

        for i in range(len(groups) + 1):
            for j in range(len(record) + 1):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    char = record[j - 1]
                    nums = groups[i - 1]

                    if char == '.':
                        dp[i][j] = dp[i][j - 1]
                    elif char == '#':
                        if '?' not in record[j - nums:j]:
                            dp[i][j] = dp[i - 1][j - nums - 1]
                        else:
                            dp[i][j] = dp[i][j - 1]
                    elif char == '?':
                        if '#' not in record[j - nums:j]:
                            dp[i][j] = dp[i - 1][j - nums - 1]
                        else:
                            dp[i][j] = dp[i][j - 1] + dp[i - 1][j - nums - 1]

        return dp[len(groups)][len(record)]
    def grouped(self, dupId, charId, tuple):
        row, dup = tuple
        return self.find_groups(row, dup)
        # return self.find_groups_tabulation(row, dup)

    def parse_input(self, data, part_number: int = 1):
        tuples = [(tuple(part_number*(row + '?'))[:-1], eval((part_number*(dup+','))[:-1])) for line in data for row, dup in [line.strip().split(' ')]]
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
            input_ = self.get_input(1)
        res = self.parse_input(input_, 5)
        print(res)
        return str(res)

    def do_test(self, part_number):
        return super().do_test(part_number)

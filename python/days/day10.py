from parse import parse
from .day import Day

class Day10(Day):
    def __init__(self, day=10):
        super().__init__(day)

    def get_input(self, part_number: int):
        with open(self.inputLocation + str(part_number) + ".txt") as file:
            return file.readlines()

    def parse_input(self, data, part_number: int = 1):
        sequences = [list(map(int, line.split(' '))) for line in data if line and line != '\n']
        return sequences

    def do_part_1(self, input_=None):
        print(f"[PART 1]: Running part 1...")
        if input_ is None:
            input_ = self.get_input(1)
        data = self.parse_input(input_)
        print(res)
        return str(res)

    def do_part_2(self, input_=None):
        print(f"[PART 2]: Running part 2...")
        if input_ is None:
            input_ = self.get_input(2)
        data = self.parse_input(input_)
        print(res)
        return str(res)

    def do_test(self, part_number):
        return super().do_test(part_number)

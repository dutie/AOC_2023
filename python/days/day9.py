from parse import parse
from .day import Day

class Day9(Day):
    def __init__(self, day=9):
        super().__init__(day)

    def get_input(self, part_number: int):
        with open(self.inputLocation + str(part_number) + ".txt") as file:
            return file.readlines()

    def make_difference_sequence(self, sequence):
        # Without zip seems to be faster:
        return [sequence[i] - sequence[i - 1] for i in range(1, len(sequence))]
        # return [y - x for x, y in zip(sequence, sequence[1:])]
    
    def calc_next_val_offset(self, extrapolateList):
        # val = 0
        # extrapolateList = extrapolateList[::-1]
        # for i in range(len(extrapolateList)):
        #     val += extrapolateList[i][-1]
        # return val
        return sum(extrapolate[-1] for extrapolate in extrapolateList)
                

    def calc_extrapolation_list_and_get_offset(self, sequence):
        nSequence = sequence
        extrapolateList = []
        while True:
            if all(i == 0 for i in nSequence):
                break
            nSequence = self.make_difference_sequence(nSequence)
            extrapolateList.append(nSequence)
        return sequence[-1] + self.calc_next_val_offset(extrapolateList)
    
    def calc_extrapolation_using_recursion(self, sequence):
        diffs = self.make_difference_sequence(sequence)
        return sequence[-1] + self.calc_extrapolation_using_recursion(diffs) if sequence else 0

    def parse_input(self, data, part_number: int = 1):
        sequences = [list(map(int, line.split(' '))) for line in data if line and line != '\n']
        return sequences

    def do_part_1(self, input_=None):
        # Recursion does not seem faster.
        print(f"[PART 1]: Running part 1...")
        if input_ is None:
            input_ = self.get_input(1)
        data = self.parse_input(input_)
        repeatedSequences = list(map(self.calc_extrapolation_list_and_get_offset, data))
        res = sum(repeatedSequences)
        # res = sum(map(self.calc_extrapolation_using_recursion, data))
        print(res)
        return str(res)

    def do_part_2(self, input_=None):
        print(f"[PART 2]: Running part 2...")
        if input_ is None:
            input_ = self.get_input(2)
        data = self.parse_input(input_)
        data = [line[::-1] for line in data]
        repeatedSequences = list(map(self.calc_extrapolation_list_and_get_offset, data))
        res = sum(repeatedSequences)
        print(res)
        return str(res)

    def do_test(self, part_number):
        return super().do_test(part_number)

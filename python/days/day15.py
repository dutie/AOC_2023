from parse import parse
from .day import Day

class Day15(Day):
    def __init__(self, day=15):
        super().__init__(day)

    def get_input(self, part_number: int):
        with open(self.inputLocation + str(part_number) + ".txt") as file:
            return [step for step in file.read().split(',')]

    def parse_input(self, data, lenses: bool = False):
        tot = 0
        if lenses:
            boxes = [{} for _ in range(256)]

        for step in data:
            current_value = 0
            for idx, char in enumerate(step):
                if lenses and char in ['-', '=']:
                    action = char
                    val  = idx
                    break
                ascii_code = ord(char)
                current_value += int(ascii_code)
                current_value *= 17
                current_value %= 256
            if lenses:
                if action == "-":
                    try:
                        del boxes[current_value][step[:idx]]
                    except:
                        pass
                else:
                    boxes[current_value][step[:idx]] = int(step[idx+1:])
            tot+=current_value

        if lenses:
            tot = 0
            for i, box in enumerate(boxes):
                for j, (k,v) in enumerate(box.items()):
                    tot+= (i+1) * (j+1) * v
        return tot

    def do_part_1(self, input_=None):
        print(f"[PART 1]: Running part 1...")
        if input_ is None:
            input_ = self.get_input(1)
        else:
            input_ = [step for step in input_[0].split(',')]
        val = self.parse_input(input_)

        print(val)
        return str(val)

    def do_part_2(self, input_=None):
        print(f"[PART 2]: Running part 2...")
        if input_ is None:
            input_ = self.get_input(2)
        else:
            input_ = [step for step in input_[0].split(',')]
        val = self.parse_input(input_, True)

        print(val)
        return str(val)
    def do_test(self, part_number):
        return super().do_test(part_number)

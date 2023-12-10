from parse import parse
from .day import Day

class Day2(Day):
    def __init__(self, day=2):
        super().__init__(day)

    def do_part_1(self, input = None):
        print(f"[PART 1]: Running part 1...")
        if input is None:
            input = self.get_input(1)

        total = 0
        for l in input:
            game, rounds = parse("Game {:d}: {}", l)
            if all(
                (int(n) <= 12 if c == "red" else int(n) <= 13 if c == "green" else int(n) <= 14)
                for rs in rounds.split("; ")
                for n, c in (r.split(" ") for r in rs.split(", "))
            ):
                total += game
        print(total)
        return total

    def do_part_2(self, input=None):
        print(f"[PART 2]: Running part 2...")
        if input is None:
            input = self.get_input(2)
        pwrs = 0
        for l in input:
            game, rounds = parse("Game {:d}: {}", l)
            red, green, blue = (0, 0, 0)
            for rs in rounds.split("; "):
                for n, c in (r.split(" ") for r in rs.split(", ")):
                    if c == "red":
                        red = max(red, int(n))
                    elif c == "green":
                        green = max(green, int(n))
                    else:
                        blue = max(blue, int(n))
            pwrs += red * green * blue

        print(pwrs)
        return pwrs
    def do_test(self, partNumber):
        return super().do_test(partNumber)
    def get_input(self, partNumber: int):
        return super().get_input(partNumber)
    def parse_input(self, partNumber: int):
        return super().parse_input(partNumber)



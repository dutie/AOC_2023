from .day import Day

class Day16(Day):
    def __init__(self, day=16):
        super().__init__(day)

    def get_input(self, part_number: int):
        with open(self.inputLocation + str(part_number) + ".txt") as file:
            return file.readlines()

    def traverse_grid(self, x, y, dx, dy, mirrors, energized):
        if x < 0 or x >= len(mirrors[0]) or y < 0 or y >= len(mirrors) or (x, y, dx, dy) in energized:
            return
        if len(list(filter(lambda tup: tup[0][0] == tup[1][0] and tup[0][1] == tup[1][1]), energized)
        energized.add((x, y, dx, dy))

        match mirrors[y][x]:
            case '.':
                self.traverse_grid(x + dx, y + dy, dx, dy, mirrors, energized)
            case '-':
                if dy == 0:
                    self.traverse_grid(x + dx, y + dy, dx, dy, mirrors, energized)
                else:
                    self.traverse_grid(x, y, -1, 0, mirrors, energized)
                    self.traverse_grid(x, y, 1, 0, mirrors, energized)
            case '|':
                if dx == 0:
                    self.traverse_grid(x + dx, y + dy, dx, dy, mirrors, energized)
                else:
                    self.traverse_grid(x, y, 0, -1, mirrors, energized)
                    self.traverse_grid(x, y, 0, 1, mirrors, energized)
            case '/':
                t = dx
                dx = -dy
                dy = -t
                self.traverse_grid(x + dx, y + dy, dx, dy, mirrors, energized)
            case '\\':
                t = dx
                dx = dy
                dy = t
                self.traverse_grid(x + dx, y + dy, dx, dy, mirrors, energized)

    def get_energized_count(self, x, y, dx, dy, mirrors):
        energized = set()
        self.traverse_grid(x, y, dx, dy, mirrors, energized)
        return len({(x, y) for (x, y, _, _) in energized})

    def do_part_1(self, input_=None):
        print(f"[PART 1]: Running part 1...")
        if input_ is None:
            input_ = self.get_input(1)

        mirrors = [line.strip() for line in input_]
        result = self.get_energized_count(0, 0, 1, 0, mirrors)
        print(result)
        return str(result)

    def do_part_2(self, input_=None):
        print(f"[PART 2]: Running part 2...")
        if input_ is None:
            input_ = self.get_input(2)

        print(None)
        return str(None)
    
    def do_test(self, part_number):
        return super().do_test(part_number)

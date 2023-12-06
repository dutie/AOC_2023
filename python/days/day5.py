from parse import parse
from .day import Day

class Day5(Day):
    def __init__(self, day=5):
        super().__init__(day)

    def get_input(self, part_number: int):
        with open(self.inputLocation + str(part_number) + ".txt") as file:
            return file.readlines()

    def get_seeds(self, data, part_number):
        seeds = [int(seed) for seed in data[0].strip().split(": ")[1].split(" ")]
        if part_number == 2:
            updated_seeds = []
            start = 0
            for i, seed in enumerate(seeds):
                if i % 2 == 0:
                    start = seed
                else:
                    updated_seeds.extend(list(range(start, start + seed)))
            seeds = updated_seeds
        return seeds

    def parse_input(self, data, part_number: int = 1):
        seeds = self.get_seeds(data, part_number)
        mappings = []

        for line in data[1:]:
            line = line.strip()
            if line.endswith(":"):
                mappings.append([])
            elif len(line) > 0:
                mappings[-1].append([int(value) for value in line.split(" ")])
        
        return seeds, mappings

    def apply_mappings(self, position, type_mappings):
        for mapping in type_mappings:
            if mapping[1] <= position < mapping[1] + mapping[2]:
                position = position - mapping[1] + mapping[0]
                break
        return position

    def do_part_1(self, input_=None):
        print(f"[PART 1]: Running part 1...")
        if input_ is None:
            input_ = self.get_input(1)

        seeds, mappings = self.parse_input(input_)
        [mapping.sort(key=lambda x: x[1]) for mapping in mappings]

        result = 2**32
        for position in seeds:
            for type_mappings in mappings:
                position = self.apply_mappings(position, type_mappings)
            result = min(position, result)

        print(result)
        return str(result)

    def do_part_2(self, input_=None):
        print(f"[PART 2]: Running part 2...")
        if input_ is None:
            input_ = self.get_input(2)

        seeds, mappings = self.parse_input(input_)
        result = 2**64

        for start, offset in zip(seeds[::2], seeds[1::2]):
            ranges = [(start, start + offset - 1)]
            for type_mappings in mappings:
                new_ranges = []
                for low, high in ranges:
                    found = False
                    for md, ms, mo in type_mappings:
                        if low >= ms and high < ms + mo:
                            new_ranges.append((low - ms + md, high - ms + md))
                            found = True
                            break
                        elif low < ms and high >= ms and high < ms + mo:
                            ranges.append((low, ms - 1))
                            new_ranges.append((md, md + high - ms))
                            found = True
                            break
                        elif low < ms + mo and high >= ms + mo and low >= ms:
                            ranges.append((ms + mo, high))
                            new_ranges.append((md + low - ms, md + mo - 1))
                            found = True
                            break
                        elif low < ms and high >= ms + mo:
                            ranges.append((low, ms - 1))
                            new_ranges.append((md, md + mo - 1))
                            ranges.append((ms + mo, high))
                            found = True
                            break
                    if not found:
                        new_ranges.append((low, high))
                ranges = new_ranges.copy()

            result = min(result, min(ranges)[0])

        print(result)
        return str(result)

    def do_test(self, part_number):
        return super().do_test(part_number)

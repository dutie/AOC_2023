import math
import re
from parse import parse
from .day import Day

class Day8(Day):
    def __init__(self, day=8):
        super().__init__(day)

    def get_input(self, part_number: int):
        with open(self.inputLocation + str(part_number) + ".txt") as file:
            return file.read().strip()

    def parse_line(self, line, node_neighbor_pairs):
        source, left, right = re.findall(r"[0-9A-Z]+", line)
        node_neighbor_pairs[source] = (left, right)
        return node_neighbor_pairs

    def parse_input(self, data, part_number: int = 1):
        instructions, lines = data.split("\n\n")
        node_neighbor_pairs = {}
        for line in lines.splitlines():
            node_neighbor_pairs = self.parse_line(line, node_neighbor_pairs)
        return instructions, node_neighbor_pairs

    def loop(self, instructions):
        instructions = [instruction == "R" for instruction in instructions]
        while True:
            yield from instructions
            
    def do_part(self,node, instructions, nnp, end="ZZZ"):
        step_count = 0
        for instruction in self.loop(instructions):
            if node == end or (end != "ZZZ" and node.endswith(end)):
                break
            step_count += 1
            node = nnp[node][instruction]
        return step_count

    def do_part_1(self, input_=None):
        print(f"[PART 1]: Running part 1...")
        if input_ is None:
            input_ = self.get_input(1)
        instructions, nnp = self.parse_input(input_)
        node = "AAA"
        step_count = self.do_part(node, instructions, nnp)
        
        print(step_count)
        return str(step_count)

    def do_part_2(self, input_=None):
        print(f"[PART 2]: Running part 2...")
        if input_ is None:
            input_ = self.get_input(2)
        instructions, nnp = self.parse_input(input_)
        step_counts = []
        for node in filter(lambda x: x[-1] == 'A', nnp):
            step_counts.append(self.do_part(node, instructions, nnp, "Z"))
        lcm = math.lcm(*step_counts)
        print(lcm)
        return str(lcm)

    def do_test(self, part_number):
        return super().do_test(part_number)

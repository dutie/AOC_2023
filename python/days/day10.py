from typing import List, Set, Tuple
from parse import parse
from .day import Day

class Day10(Day):
    def __init__(self, day=10):
        super().__init__(day)
        self.dict_coor = {
            "-": [(0,1), (0,-1)],
            "|": [(1,0), (-1,0)],
            "L": [(0, 1), (-1, 0)],
            "F": [(0, 1), (1, 0)],
            "7": [(0, -1), (1, 0)],
            "J": [(0, -1), (-1, 0)]
        }
        self.neighbors_coor = [(0,-1), (0,1), (-1,0), (1,0)]
    def get_input(self, part_number: int):
        with open(self.inputLocation + str(part_number) + ".txt") as file:
            return file.readlines()

    def parse_input(self, data, part_number: int = 1):
        start_pos = [(i, start_line.find("S")) for i, start_line in enumerate(data) if start_line.find("S") > -1][0]
        return data, start_pos
    
    def in_bounds(self, coor, field):
        max_x = len(field[0])
        max_y = len(field)
        val   = field[coor[0]][coor[1]]
        return 0 <= coor[0] < max_y and 0 <= coor[1] < max_x and val in self.dict_coor.keys() 
   
    def traverse_and_count_bfs(self, start: Tuple[int], field: List[List[str]], visited: Set[Tuple[int]]) -> int:
        q = list(filter(lambda n: self.in_bounds(n ,field) and n != start,[(n[0]+start[0], n[1]+start[1]) for n in self.neighbors_coor]))
        visited.add(start)

        while q:
            current = q.pop(0)
            (y, x) = current
            char = field[y][x]

            for dy, dx in self.dict_coor[char]:
                neighbor = (y + dy, x + dx)

                if neighbor not in visited and self.in_bounds(neighbor, field):
                    visited.add(neighbor)
                    q.append(neighbor)

        return len(visited) // 2
    
    def fence(self, field, visited):
        cnt = 0
        fen = " "
        for y in range(len(field)):
            out = True
            for x in range(len(field[y])):
                if (y, x) in visited:
                    if field[y][x] == "F":
                        fen = "7"
                    elif field[y][x] == "L":
                        fen = "J"
                    elif field[y][x] == "-":
                        continue
                    else:
                        if field[y][x] != fen:
                            out = not out
                        fen = " "
                elif not out:
                    cnt += 1
        return cnt
        

    def do_part_1(self, input_=None):
        print(f"[PART 1]: Running part 1...")
        if input_ is None:
            input_ = self.get_input(1)
        data, start_pos = self.parse_input(input_)
        visited = set()
        visited.clear()
        visited.add(start_pos)
        res = self.traverse_and_count_bfs(start_pos, data, visited)
        print(res)
        return str(res)

    def do_part_2(self, input_=None):
        print(f"[PART 2]: Running part 2...")
        if input_ is None:
            input_ = self.get_input(2)
        data, start_pos = self.parse_input(input_)
        visited = set()
        visited.clear()
        visited.add(start_pos)
        _ = self.traverse_and_count_bfs(start_pos, data, visited)
        res = self.fence(data, visited)
        print(res)
        return str(res)

    def do_test(self, part_number):
        return super().do_test(part_number)

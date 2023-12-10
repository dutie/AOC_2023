from typing import List, Tuple

from .day import Day

class Day3(Day):
    def __init__(self, day=3):
        super().__init__(day)

    def neighbors(self, input_matrix: List[List[str]]) -> List[int]:
        numbers = []
        
        for row, row_values in enumerate(input_matrix):
            col = 0
            while col < len(row_values):
                if row_values[col].isdigit():
                    number, n_col = self.extract_number((row, col), input_matrix)
                    if self.check_neighbors((row, col), (row, n_col), input_matrix):
                        numbers.append(number)
                    col = n_col
                col += 1

        return numbers

    def extract_number(self, coordinates: Tuple[int, int], matrix: List[List[str]]) -> Tuple[int, int]:
        number = ""
        row, col = coordinates
        while col < len(matrix[row]) and matrix[row][col].isdigit():
            number += matrix[row][col]
            col += 1
        return int(number), col - 1

    def check_neighbors(self, cor_cur, cor_cur_end, matrix):
        row, col = cor_cur
        end_row, end_col = cor_cur_end
        number_coor = set((row, c) for c in range(col, end_col + 1))

        for r in range(row - 1, end_row + 2):
            for c in range(col - 1, end_col + 2):
                if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and (r, c) != (row, col) and (r, c) not in number_coor:
                    if matrix[r][c] != '.':
                        return True

        return False

    def do_part_1(self, input=None):
        print(f"[PART 1]: Running part 1...")
        if input is None:
            input = self.get_input(1)
        result = sum(self.neighbors(input))
        print(f"[PART 1]: {result}")
        return result

    def get_number(self, coordinates: Tuple[int, int], rowList: List[str]):
        row, col = coordinates
        maxCol = col
        # number = f""
        while maxCol < len(rowList) and rowList[maxCol].isdigit():
            # number += rowList[maxCol]
            maxCol += 1
        minCol = col-1
        # number = number[::-1]
        while minCol >= 0 and rowList[minCol].isdigit():
            # number += rowList[minCol]
            minCol -= 1
            col = minCol
        return (minCol+1, maxCol-1)
        # return number[::-1]

    def make_number(self, start, end, rowList):
        number_chars = []
        for c in range(start, end+1):
            number_chars.append(rowList[c])
        number_str = ''.join(number_chars)
        return int(number_str)

    def check_special_neighbors(self, coordinates: Tuple[int, int], matrix: List[List[str]]):
        row, col = coordinates
        neighboring_numbers = []
        visited = set()

        for r in range(row - 1, row + 2):
            for c in range(col - 1, col + 2):
                if 0 <= r < len(matrix) and 0 <= c < len(matrix[0]) and (r, c) != coordinates and matrix[r][c].isdigit() and (r, c) not in visited:
                    start_col, end_col = self.get_number((r, c), matrix[r])
                    visited.update((r, colu) for colu in range(start_col, end_col+1))
                    neighboring_numbers.append(self.make_number(start_col, end_col, matrix[r]))

        return neighboring_numbers
    def special(self, matrix):
        results = []
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if not(matrix[row][col] == '.' or matrix[row][col].isdigit()):
                    gears = self.check_special_neighbors((row, col), matrix)
                    if len(gears) == 2:
                        results.append(int(gears[0]) * int(gears[1]))
        return results


    def do_part_2(self, input=None):
        print(f"[PART 2]: Running part 2...")
        if input is None:
            input = self.get_input(2)
        result = sum(self.special(input))
        print(f"[PART 2]: {result}")
        return result

    def do_test(self, partNumber):
        return super().do_test(partNumber)
    
    def get_input(self, partNumber):
        return super().do_part_2(input)
    
    def do_test(self, partNumber):
        return super().do_test(partNumber)
    
    def get_input(self, partNumber: int):
        return super().get_input(partNumber)
    def parse_input(self, partNumber: int):
        return super().parse_input(partNumber)

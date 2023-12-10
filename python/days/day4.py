import re
from .day import Day
from parse import parse

class Day4(Day):
    def __init__(self, day=4):
        super().__init__(day)

    def parse_input(self, data):
        pattern = re.compile(r'Card\s+(\d+):\s+(.*)\s+\|\s+(.*)')
        cards = [pattern.match(i).groups() for i in data if pattern.match(i)]
        print(cards)
        # print(cards)
        # cards = [[re.split(r'\s+', part.strip()) for part in row.split(': ')[1].split(' | ')] for row in data]
        # print(cards)
        return cards

    def do_part_1(self, input = None):
        print(f"[PART 1]: Running part 1...")
        if input is None:
            input = self.get_input(1)
        input = self.parse_input(input)
        correctGames = []
        for game, own, actual in input:
            numOwn = own.split(' ')
            numAct = actual.split(' ')
            correct = 0
            for num in numOwn:
                if num.isdigit():
                    if num in numAct:
                        if correct > 0:
                            correct *= 2
                        else:
                            correct += 1
            correctGames.append(correct) 
        print(sum(correctGames))
        return f'{sum(correctGames)}'

    def do_part_2(self, input=None):
        print(f"[PART 2]: Running part 2...")
        if input is None:
            input = self.get_input(2)
        parsedData = self.parse_input(input)
        number_of_cards = [1 for _ in range(len(parsedData))]
        for card_number, (_, own, actual) in enumerate(parsedData):
            card = [own, actual]
            won = 0
            for number in card[0]:
                if number in card[1]:
                    won += 1 
            for i in range(won):
                number_of_cards[card_number + (i + 1)] += (1 * number_of_cards[card_number])
        result = sum(number_of_cards)
        print(f"[PART 2]: {result}")
        return result
    def do_test(self, partNumber):
        return super().do_test(partNumber)
    def get_input(self, partNumber: int):
        return super().get_input(partNumber)
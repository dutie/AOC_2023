from abc import ABC, abstractmethod
import time

class Day(ABC):
    def __init__(self, day):
        self.inputLocation = "inputs/day" + str(day) + "_"
        self.testLocation  = "tests/day" + str(day) + "_"

    @abstractmethod
    def parse_input(self, partNumber: int):
        raise NotImplementedError

    @abstractmethod
    def get_input(self, partNumber: int):
        with open(self.inputLocation + str(partNumber) + ".txt") as f:
            return f.read().splitlines()

    @abstractmethod
    def do_part_1(self, input = None):
        print(f"[PART 1]: Running part 1...")
        raise NotImplementedError
    @abstractmethod
    def do_test(self, partNumber):
        print(f"[TESTING]: Testing part {partNumber}...")
        inputs, outputs = self.get_test(partNumber)
        print(inputs, outputs)
        allPassed = True
        for idIO, (input, output) in enumerate(zip(inputs, outputs)):
            if partNumber == 1:
                result = self.do_part_1(input)
            elif partNumber == 2:
                result = self.do_part_2(input)
            outcomeText = f"Test {idIO} passed." if output == result else f"Test {idIO} failed."
            print(outcomeText)
            print(f"Expected: {output}.")
            print(f"Actual: {result}.")
            if not output == result:
                allPassed = False
        return allPassed
            
    @abstractmethod
    def do_part_2(self, input = None):
        print(f"[PART 2]: Running part 2...")
        raise NotImplementedError
    

    def get_test(self, partNumber: int):
        with open(self.testLocation + str(partNumber) + ".txt") as f:
            inputs = []
            input = []
            outcomes = []
            lines = [line for line in f.read().splitlines()]
            flagIn = True
            for line in lines:
                if line == "OUTPUTS:":
                    flagIn = False
                    continue
                print(line)
                if flagIn:
                    if line == "":
                        inputs.append(input)
                        input = []
                    else:
                        input.append(line)
                else:
                    outcomes.append(line)   
        return inputs, outcomes
        
    def run(self):

        startTime = time.time()
        self.do_part_1()
        delta = time.time() - startTime
        print(f"[PART 1]: {delta*1000} ms")
        startTime = time.time()
        self.do_part_2()
        delta = time.time() - startTime
        print(f"[PART 2]: {delta*1000} ms")

from parse import parse
from .day import Day

class Day19(Day):
    def __init__(self, day=19):
        super().__init__(day)

    def get_input(self, part_number: int):
        with open(self.inputLocation + str(part_number) + ".txt") as file:
            return file.readlines()

    def parse_workflow(self, workflow, letter, input):
        val_dict = {val[:1]:val[2:] for val in input.split(',')}
        
        return eval(lambda: workflow, val_dict[letter])
        
        
        

    def parse_input(self, data, part_number: int = 1):
        workflows, ratings = data
        workflow_dict = {}
        start_key = ''
        for workflow in workflows:
            data_list = workflow.split('{')
            workflow_key, workflow_content = data_list[0], [action.split(':') for action in data_list[1][:-1].split(',')]
            if start_key == '':
                start_key = workflow_key
            workflow_dict[workflow_key] = workflow_content
        workflow = workflow_dict[start_key]
        while len(ratings) > 0:
            rating = ratings.pop()
            print(workflow)
            for work in workflow:
                if len(work) == 1:
                    workflow_dict[work[0]]
                else:
                    if work[0][0] in 'xmas':
                        print("N")
                        res = self.parse_workflow(work[1:], work[0], rating)
                        print(res)
        return workflow_dict

    def do_part_1(self, input_=None):
        print(f"[PART 1]: Running part 1...")
        if input_ is None:
            input_ = self.get_input(1)
        else:
            index_of_split = input_.index('ratings')
            workflows, ratings = input_[:index_of_split], input_[index_of_split+1:]
        print(workflows, ratings)
        res = self.parse_input((workflows, ratings))
        print(res)
        return str(None)

    def do_part_2(self, input_=None):
        print(f"[PART 2]: Running part 2...")
        if input_ is None:
            input_ = self.get_input(2)

        print(None)
        return str(None)

    def do_test(self, part_number):
        return super().do_test(part_number)

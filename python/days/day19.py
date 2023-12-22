import ast
from parse import parse
from .day import Day

class Day19(Day):
    def __init__(self, day=19):
        super().__init__(day)

    def get_input(self, part_number: int):
        with open(self.inputLocation + str(part_number) + ".txt") as file:
            return file.read().split('\n')
        

    def parse_work(self, cur_id, workflow, letter, input):
        work = workflow[cur_id]

        parsed_expr = ast.parse(work, mode='eval')

        variables = {letter: input[letter]}

        result = eval(compile(parsed_expr, filename='<string>', mode='eval'), variables)
        # print("START AT: ", workflow)
        # print(f"{work} in {letter}: {input[letter]}{work} is {result}.")
        if result:
            n_cur_id = cur_id+1
            return n_cur_id
        else:
            n_cur_id = cur_id+2
            return n_cur_id


    def parse_workflows(self, workflows):
        workflow_dict = {}

        for workflow in workflows:
            tokens = workflow.split('{')
            key = tokens[0].strip()
            nested_values = []

            for token in tokens[1].rstrip('}').split(','):
                values = [item.strip() for item in token.split(':')]
                if len(values) == 1:
                    nested_values.append(values[0])
                else:
                    nested_values.extend(values)

            workflow_dict[key] = nested_values

        return workflow_dict
    def parse_ratings(self, ratings):
        rating_dict_list = []
        for rating in ratings:
            rating_dict = {}
            for s_rating in rating.split(','):
                key, val = s_rating.replace('{', '').replace('}', '').split('=')
                rating_dict[key] = int(val)
            rating_dict_list.append(rating_dict)
        return rating_dict_list

    def do_workflow(self, rating, workflow, workflow_dict):
        if workflow[0] in workflow_dict.keys() or workflow[0] in "AR":
            if workflow[0] in "AR":
                if workflow[0] == "A":
                    return True
                else:
                    return False
            else:
                return self.do_workflow(rating, workflow_dict[workflow[0]], workflow_dict)
        else:
            cur_id = 0
            while cur_id < len(workflow):
                work = workflow[cur_id]
                cur_id = self.parse_work(cur_id, workflow, work[0][0], rating)
                n_workflow = workflow[cur_id:]
                return self.do_workflow(rating, n_workflow , workflow_dict)


    def parse_input(self, data, part_number: int = 1):
        workflows, ratings = data
        workflow_dict = self.parse_workflows(workflows)
        workflow = workflow_dict["in"]
        ratings = self.parse_ratings(ratings)
        accepted_list = []
        for rating in ratings:
            is_accepted = self.do_workflow(rating, workflow, workflow_dict)
            if is_accepted:
                accepted_list.append(rating)
            # for work in workflow:
            #     if len(work) == 1:
            #         workflow_dict[work[0]]
            #     else:
            #         if work[0][0] in 'xmas':
            #             res = self.parse_workflow(work, work[0][0], rating)
        total = 0
        for accepted in accepted_list:
            total += sum(accepted.values())
        return total

    def do_part_1(self, input_=None):
        print(f"[PART 1]: Running part 1...")
        if input_ is None:
            input_ = self.get_input(1)
            idx = input_.index('')
            workflows, ratings = input_[:idx], input_[idx+1:]
        else:
            index_of_split = input_.index('ratings')
            workflows, ratings = input_[:index_of_split], input_[index_of_split+1:]
        res = self.parse_input((workflows, ratings))
        print(res)
        return str(res)

    def do_part_2(self, input_=None):
        print(f"[PART 2]: Running part 2...")
        if input_ is None:
            input_ = self.get_input(1)
            idx = input_.index('')
            workflows, ratings = input_[:idx], input_[idx+1:]
        else:
            index_of_split = input_.index('ratings')
            workflows, ratings = input_[:index_of_split], input_[index_of_split+1:]
        res = self.parse_input((workflows, ratings))
        print(res)
        return str(res)

    def do_test(self, part_number):
        return super().do_test(part_number)
    

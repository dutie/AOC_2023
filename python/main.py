import importlib
from days.day import Day


def parse_args(): 
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-d", "--day", type=int, required=True, help="Day of Advent")
    parser.add_argument("-p", "--part", type=int, required=True,  help="Part 1 or 2")
    parser.add_argument("-t", "--test", type=int, help="Run test")
    return parser.parse_args()

def main():
    args = parse_args()
    day = args.day
    part = args.part
    doTest = args.test # if 1 run only test, if 0 run only normal code, if not there run both

    day_module_name = f'days.day{day}'
    day_module = importlib.import_module(day_module_name)

    # Create an instance of the correct Day class (e.g., Day1)
    day_class_name = f'Day{day}'
    day_class: Day = getattr(day_module, day_class_name)()

    # Run the specified part

    if doTest is not None:
        if doTest == 1:
            day_class.do_test(part)
        else:
            if part == 1:
                day_class.do_part_1()
            elif part == 2:
                day_class.do_part_2()
    else:
        day_class.run()
if __name__ == "__main__":
    main()
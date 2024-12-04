import re
from input_loader import load_input, load_test_intput


def filter_expressions(input_data: str):
    return re.findall(re.compile(r"mul\(\d+,\d+\)"), input_data)

def filter_expressions_with_do(input_data: str):
    return re.findall(re.compile(r"mul\(\d+,\d+\)|do\(\)|don't\(\)"), input_data)

def calculate_expressions(expressions: list[str]):

    result = 0
    for expression in expressions:
        numbers = re.findall(r"\d+", expression)
        result += (int(numbers[0]) * int(numbers[1]))

    return result

def calculate_expressions_with_do_mode(expressions: list[str]):

    result = 0
    do_mode = True
    do_not_mode_count = 0
    for expression in expressions:

        if expression == "don't()":
            do_not_mode_count += 1
            do_mode = False
            continue

        if expression == "do()":
            do_mode = True
            continue

        if do_mode is False:
            continue

        numbers = re.findall(r"\d+", expression)
        result += (int(numbers[0]) * int(numbers[1]))
        do_mode = True

    print(do_not_mode_count)

    return result

def run(input_data: str):
    expressions = filter_expressions(input_data)
    return calculate_expressions(expressions)

def run_with_do_mode(input_data: str):
    expressions = filter_expressions_with_do(input_data)
    return calculate_expressions_with_do_mode(expressions)

test_data_part_1_result = run(load_test_intput()[0])
assert test_data_part_1_result == 161

# part_1
data_part_1_result = sum([run(x) for x in load_input()]) # 174336360
# part_2
data_part_2_result = run_with_do_mode(''.join(load_input())) # 88802350
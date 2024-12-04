import re
from input_loader import load_input, load_test_intput


def filter_expressions(input_data: str):
    return re.findall(re.compile(r"mul\(\d+,\d+\)"), input_data)

def calculate_expressions(expressions: list[str]):

    result = 0
    for expression in expressions:
        numbers = re.findall(r"\d+", expression)
        result += (int(numbers[0]) * int(numbers[1]))

    return result


def run(input_data: str):
    expressions = filter_expressions(input_data)
    return calculate_expressions(expressions)

test_data_part_1_result = run(load_test_intput()[0])
assert test_data_part_1_result == 161

# part_1
data_part_1_result = sum([run(x) for x in load_input()]) # 174336360

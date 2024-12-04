from shlex import split

from input_loader import load_test_intput, load_input

data = load_test_intput()

def parse_input(input_data: list):
    """
    One time only for input data
    """
    lists = {
        'left': [],
        'right': []
    }

    for input_element in input_data:
        element = input_element.split()
        lists['left'].append(int(element[0]))
        lists['right'].append(int(element[1]))

    return lists

def calculate(numbers: dict[str, list[int]]):

    left_list = sorted(numbers['left'])
    right_list = sorted(numbers['right'])

    result = 0

    for left, right in zip(left_list, right_list):
        result += abs(left - right)

    return result


# exercise input
input_data = load_input()
parsed_data = parse_input(input_data)
exercise_data = calculate(parsed_data)
print(exercise_data) # 1603498 correct result
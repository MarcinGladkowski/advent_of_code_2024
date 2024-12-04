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

def similarity(numbers: dict[str, list[int]]) -> int:

    result = 0
    for key, value in zip(numbers['left'], numbers['right']):
        element_count = numbers['right'].count(key)
        if element_count < 1:
            continue

        result += element_count * key

    return result


# exercise input
input_data = load_input()
parsed_data = parse_input(input_data)
part_1 = calculate(parsed_data)
print(part_1) # 1603498 correct result

part_2_result = similarity(parsed_data)
print(part_2_result)
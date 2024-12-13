from input_loader import load_test_intput, load_input
from main import calculate

def parse_input(data: list[str]) -> list:
    result = []

    for line in data:
        elements = line.split(':')

        result.append([
            int(elements[0]),
            list(map(lambda x: int(x), elements[1].strip().split(' ')))
        ])

    return result

# test_data = parse_input(load_test_intput())
#
# assert calculate(test_data) == 3749
#
# print(calculate(parse_input(load_input())))

combinations = [
    ('*', '*', '*', '*', '*', '*', '*', '*'),
    ('*', '*', '*', '*', '*', '*', '*', '*'),
    ('*', '*', '*', '*', '*', '*', '*', '*')
]

print(list(set(combinations)))


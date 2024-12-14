import itertools

def determine_operators_combinations(operators: list, combinations_len) -> set[str]:
    """
        Works for two elements
    """
    return set(list(itertools.product(operators, repeat=combinations_len)))


def load_combinations(number: int) -> list[str]:
    with open(f'{number}_length_combinations.txt', 'r') as f:
        return f.read().splitlines()

def determine_combination(result: int, numbers: [int], operators: list) -> [int]:
    """
    add operations (+)
    multiply operations (*)

    :param result:
    :param numbers:
    :return: int > 0 ok, = 0 not determined
    """
    combinations = determine_operators_combinations(operators, len(numbers)-1)
    # load combinations from file
    #combinations = load_combinations(len(numbers))

    for combination in combinations:
        if result == execute_combination(combination, numbers):
            return result

    return 0


def execute_combination(combination: str, numbers: list[int]) -> int:
    result = 0
    combination = ''.join(combination).replace('||', '|')
    for index, number in enumerate(numbers):
        if index == 0:
            result += number
            continue
        if combination[index - 1] == '*':
            result *= number
        if combination[index - 1] == '+':
            result += number
        if combination[index - 1] == '|':
            result = int(str(result) + str(number))

    return result


def calculate(data: list, operators: list) -> int:
    result = 0
    for data in data:
        result += determine_combination(data[0], data[1], operators)
        #print(f"Determine combination for: {data[0]} | result: {result}")

    return result
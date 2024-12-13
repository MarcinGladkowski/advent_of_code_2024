import itertools


def determine_operators_combinations(operators: list, combinations_len) -> set[str]:
    """
        Works for two elements
    """
    combinations = []
    for number in range(combinations_len + 1):
        base_combination = operators[0] * combinations_len
        combinations.append(base_combination.replace(operators[0], operators[1], number))

    for number in range(combinations_len + 1):
        base_combination = operators[1] * combinations_len
        combinations.append(base_combination.replace(operators[1], operators[0], number))

    result = set(combinations)
    for combination in combinations:
        combined = list(itertools.permutations(combination, combinations_len))
        for permuted in combined:
            result.add(''.join(permuted))

    return result

def determine_combination(result: int, numbers: [int]) -> [int]:
    """
    add operations (+)
    multiply operations (*)

    :param result:
    :param numbers:
    :return: int > 0 ok, = 0 not determined
    """
    combinations = determine_operators_combinations(['*', '+'], len(numbers))

    for combination in combinations:
        if result == execute_combination(combination, numbers):
            return result

    return 0


def execute_combination(combination: str, numbers: list[int]) -> int:
    result = 0
    for index, number in enumerate(numbers):
        if index == 0:
            result += number
            continue
        if combination[index - 1] == '*':
            result *= number
        if combination[index - 1] == '+':
            result += number

    return result


def calculate(data: list) -> int:
    return sum([determine_combination(data[0], data[1]) for data in data])
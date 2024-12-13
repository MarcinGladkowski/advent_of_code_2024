import itertools
from functools import cache

# @cache
def determine_operators_combinations(operators: list, combinations_len) -> set[str]:
    """
        Works for two elements

        Should work as iterator, generating 2**12 is memory consumption
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
        combined = set((itertools.permutations(combination, combinations_len)))
        print(len)
        for permuted in combined:
            result.add(''.join(permuted))

    return result


def load_combinations(number: int) -> list[str]:
    with open(f'{number}_length_combinations.txt', 'r') as f:
        return f.read().splitlines()

def determine_combination(result: int, numbers: [int]) -> [int]:
    """
    add operations (+)
    multiply operations (*)

    :param result:
    :param numbers:
    :return: int > 0 ok, = 0 not determined
    """
    #combinations = determine_operators_combinations(['*', '+'], len(numbers)-1)
    # load combinations from file
    combinations = load_combinations(len(numbers))

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
    result = 0
    for data in data:
        result += determine_combination(data[0], data[1])
        #print(f"Determine combination for: {data[0]} | result: {result}")

    return result
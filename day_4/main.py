import re

from input_loader import load_test_intput, load_input


def find_vertical(data_set: list[list[str]]) -> int:
    """
        With up and down
        Rewrite column into rows
        :return: count of found XMAS
    """
    new_data_set = [[] for _ in range(len(data_set))]

    for row in data_set:
        for index, letter in enumerate(row):
            new_data_set[index].append(letter)

    return sum([find_horizontal(''.join(row)) for row in new_data_set])

def find_horizontal(data_row: str) -> int:
    """
        With written backwards
        :return: count of found XMAS
    """
    return len(re.findall(r"XMAS", data_row)) + len(re.findall(r"SAMX", data_row))

def find_diagonal(data_set: list[list[str]]) -> int:
    """
        With written backwards
        :return: count of found XMAS

        * There are only 4 options for 4x4 block
        * Another idea is to create strings on diagonals
    """
    return sum([find_horizontal(''.join(row)) for row in parse_diagonals_from_left(data_set)])

def parse_diagonals_from_left(data: list[list[str]]) -> list[list[str]]:
    new_set = []
    for index, row in enumerate(data):
        new_set.insert(index, [])
        for idx in range(len(row) - index):
            new_set[index].append(data[idx][idx+index])

    index_offset = len(new_set)
    for index, row in enumerate(data):
        set_index = index_offset + index
        new_set.insert(set_index, [])
        for idx in range(len(row) - index - 1):
            new_set[set_index].append(data[idx+index+1][idx])

    return new_set

def reverse_rows(data: list[list[str]]) -> list[list[str]]:
    return [list(reversed(row)) for row in data]

def process_xmas(data: list[list[str]]) -> int:
    horizontal_count = sum([find_horizontal(''.join(row)) for row in data])
    print(f"Horizontal count: {horizontal_count}")

    vertical_count = find_vertical(data)
    print(f"Vertical count: {vertical_count}")

    diagonals_from_left = find_diagonal(data)
    print(f"Diagonals left count: {diagonals_from_left}")

    diagonals_from_right = find_diagonal(reverse_rows(data))
    print(f"Diagonals right count: {diagonals_from_right}")


    return horizontal_count + vertical_count + diagonals_from_left + diagonals_from_right

assert 18 == process_xmas(load_test_intput())
assert 2549 == process_xmas(load_input())
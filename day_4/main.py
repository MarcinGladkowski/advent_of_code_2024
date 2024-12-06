import re


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
    return len(re.findall(r"XMAS|SAMX", data_row))

def find_diagonal(data_set: list[list[str]]) -> int:
    """
        With written backwards
        :return: count of found XMAS

        There are only 4 options
    """
    diagonals_count = 0

    """from top left to bottom right"""
    if data_set[0][0] == 'X' and data_set[1][1] == 'M' and data_set[2][2] == 'A' and data_set[3][3] == 'S':
        diagonals_count += 1

    """from top right to bottom left"""
    if data_set[0][3] == 'X' and data_set[1][2] == 'M' and data_set[2][1] == 'A' and data_set[3][0] == 'S':
        diagonals_count += 1

    """from bottom left to top right"""
    if data_set[3][0] == 'X' and data_set[2][1] == 'M' and data_set[1][2] == 'A' and data_set[0][3] == 'S':
        diagonals_count += 1

    """from bottom right to top left"""
    if data_set[3][3] == 'X' and data_set[2][2] == 'M' and data_set[1][1] == 'A' and data_set[0][0] == 'S':
        diagonals_count += 1

    return diagonals_count


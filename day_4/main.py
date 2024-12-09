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

def sanitize_x_mass(xmas_set: list[list[str]]) -> str:
    xmas_set[0][1] = '.'
    xmas_set[1][0] = '.'
    xmas_set[1][2] = '.'
    xmas_set[2][1] = '.'

    return ''.join([''.join(row) for row in xmas_set])


def count_xmas(parsed_data: str) -> bool:
    xmas_matrix = [
        'M.S.A.M.S',
        'S.M.A.S.M',
        'M.M.A.S.S',
        'S.S.A.M.M',
    ]

    return parsed_data in xmas_matrix


class XmasIterator:

    def __init__(self, board: list[list[str]]) -> None:
        self.board = board
        self.horizontal_len = len(board[0])
        self.vertical_len = len(board)
        self.row_start = 0
        self.row_end = 3
        self.vertical_cursor = 0

    def __iter__(self):
        return self

    def __next__(self) -> list:
        """
        Each step returning a 3x3 box

        :return:
        """
        if self.row_end > self.horizontal_len and self.vertical_cursor + 3 >= self.vertical_len:
            raise StopIteration

        if self.row_end > self.horizontal_len:
            """move down"""
            self.row_start = 0
            self.row_end = 3
            self.vertical_cursor += 1

        data =  [
            self.board[self.vertical_cursor][self.row_start:self.row_end],
            self.board[self.vertical_cursor + 1][self.row_start:self.row_end],
            self.board[self.vertical_cursor + 2][self.row_start:self.row_end]
        ]

        self.row_start += 1
        self.row_end += 1

        return data


def proces_xmas_count(data: list[list[str]]) -> int:

    iterator = XmasIterator(data)
    count = 0
    while True:

        try:
            data = next(iterator)
            result = count_xmas(sanitize_x_mass(data))

            if result:
                count += 1
        except StopIteration:
            return count


assert 18 == process_xmas(load_test_intput())
assert 2549 == process_xmas(load_input())
assert 9 == proces_xmas_count([[el for el in row] for row in load_test_intput()])
assert 2003 == proces_xmas_count([[el for el in row] for row in load_input()])


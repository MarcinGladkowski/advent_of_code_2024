from day_4.main import find_horizontal, find_diagonal, find_vertical, process_xmas, parse_diagonals_from_left, \
    reverse_rows


def test_find_xmas_vertical():
    """Write correct and backwards"""
    assert find_horizontal('custom_text') == 0
    assert find_horizontal('MMSAMXXMASMXMAS') == 3
    assert find_horizontal('SAMX') == 1
    assert find_horizontal('XMAS') == 1
    assert find_horizontal('MAMXMASAMX') == 2

def test_find_horizontal():
    """Write down"""
    test_input = [
        ['X', '.', '.', '.'],
        ['M', 'M', 'X', '.'],
        ['A', '.', 'A', '.'],
        ['S', 'S', '.', 'S'],
    ]

    assert find_vertical(test_input) == 1

    test_input = [
        ['X', 'X', '.', '.'],
        ['M', 'M', 'X', '.'],
        ['A', 'A', 'A', '.'],
        ['S', 'S', '.', 'S'],
    ]

    assert find_vertical(test_input) == 2

    test_input = [
        ['X', 'S', '.', '.'],
        ['M', 'A', 'X', '.'],
        ['A', 'M', 'A', '.'],
        ['S', 'X', '.', 'S'],
    ]

    assert find_vertical(test_input) == 2

def test_find_diagonal_from_top_left_to_right_bottom():
    test_input = [
        ['X', '.', '.', '.'],
        ['A', 'M', 'X', '.'],
        ['.', '.', 'A', '.'],
        ['A', 'S', '.', 'S'],
    ]

    assert find_diagonal(test_input) == 1

def test_find_diagonal_from_top_right_to_left_bottom():
    test_input = [
        ['.', '.', '.', 'X'],
        ['A', 'M', 'M', '.'],
        ['.', 'A', 'A', '.'],
        ['S', 'S', '.', 'S'],
    ]

    assert find_diagonal(reverse_rows(test_input)) == 1

def test_count_xmas():
    test_input = [
        ['M', 'M', 'M', 'S', 'X', 'X', 'M', 'A', 'S', 'M'], # hor: 1
        ['M', 'S', 'A', 'M', 'X', 'M', 'S', 'M', 'S', 'A'], # hor: 1
        ['A', 'M', 'X', 'S', 'X', 'M', 'A', 'A', 'M', 'M'],
        ['M', 'S', 'A', 'M', 'A', 'S', 'M', 'S', 'M', 'X'],
        ['X', 'M', 'A', 'S', 'A', 'M', 'X', 'A', 'M', 'M'], # hor 2
        ['X', 'X', 'A', 'M', 'M', 'X', 'X', 'A', 'M', 'A'],
        ['S', 'M', 'S', 'M', 'S', 'A', 'S', 'X', 'S', 'S'],
        ['S', 'A', 'X', 'A', 'M', 'A', 'S', 'A', 'A', 'A'],
        ['M', 'A', 'M', 'M', 'M', 'X', 'M', 'M', 'M', 'M'],
        ['M', 'X', 'M', 'X', 'A', 'X', 'M', 'A', 'S', 'X'] # hor 1
    ] # ver: 3

    assert process_xmas(test_input) == 18

def test_parse_diagonals():

    test_input = [
        ['S', '.', '.', 'S'],
        ['A', 'A', 'A', '.'],
        ['.', 'M', 'M', '.'],
        ['X', 'S', '.', 'X'],
    ]

    assert parse_diagonals_from_left(test_input) == [
        ['S', 'A', 'M', 'X'],
        ['.', 'A', '.'],
        ['.', '.'],
        ['S'],
        ['A', 'M', '.'],
        ['.', 'S'],
        ['X'],
        []
    ]

def test_reverse_for_left_parsing():

    test_input = [
        ['S', '.', '.', 'S'],
        ['A', 'A', 'A', '.'],
        ['.', 'M', 'M', '.'],
        ['X', 'S', '.', 'X'],
    ]

    assert reverse_rows(test_input) == [
        ['S', '.', '.', 'S'],
        ['.', 'A', 'A', 'A'],
        ['.', 'M', 'M', '.'],
        ['X', '.', 'S', 'X'],
    ]
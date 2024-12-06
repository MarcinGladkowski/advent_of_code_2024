from day_4.main import find_horizontal, find_diagonal, find_vertical


def test_find_xmas_vertical():
    """Write correct and backwards"""
    assert find_horizontal('custom_text') == 0
    assert find_horizontal('MMSAMXXMASMXMAS') == 3
    assert find_horizontal('SAMX') == 1

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

def test_find_diagonal():
    test_input = [
        ['X', '.', '.', '.'],
        ['A', 'M', 'X', '.'],
        ['.', '.', 'A', '.'],
        ['A', 'S', '.', 'S'],
    ]

    assert find_diagonal(test_input) == 1

    test_input = [
        ['.', '.', '.', 'X'],
        ['A', 'M', 'M', '.'],
        ['.', 'A', 'A', '.'],
        ['S', 'S', '.', 'S'],
    ]

    assert find_diagonal(test_input) == 1

    test_input = [
        ['S', '.', '.', 'S'],
        ['A', 'A', 'A', '.'],
        ['.', 'M', '.', '.'],
        ['X', 'S', '.', 'X'],
    ]

    assert find_diagonal(test_input) == 1

    test_input = [
        ['S', '.', '.', 'S'],
        ['A', 'A', 'A', '.'],
        ['.', '.', 'M', '.'],
        ['X', 'S', '.', 'X'],
    ]

    assert find_diagonal(test_input) == 1

    test_input = [
        ['S', '.', '.', 'S'],
        ['A', 'A', 'A', '.'],
        ['.', 'M', 'M', '.'],
        ['X', 'S', '.', 'X'],
    ]

    assert find_diagonal(test_input) == 2


from pprint import pprint

from day_8.main import combinations, AntennasPair, AntennaPoint, find_antenna_points, detect_nodes, write_nodes_on_area


def test_calculate_antinodes_for_pair_diagonal_from_left_top_to_right_bottom():
    """
        Expect two nodes at
        (0, 0), (6, 3)
    """
    test_map = [
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", "a", ".", "."],
        [".", ".", ".", "."],
        [".", ".", "a", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."],
    ]

    pair = AntennasPair(
        AntennaPoint(2, 1, 'a'),
        AntennaPoint(4, 2, 'a')
    )

    assert pair.calculate_antinodes() == [(0,0), (6, 3)]

def test_calculate_antinodes_for_pair_diagonal_from_left_right_to_left_bottom():
    """
        Expect two nodes at
        (0, 0), (6, 3)
    """
    test_map = [
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", ".", "a", "."],
        [".", ".", ".", "."],
        [".", "a", ".", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."],
    ]

    pair = AntennasPair(
        AntennaPoint(2, 2, 'a'),
        AntennaPoint(4, 1, 'a')
    )

    assert pair.calculate_antinodes() == [(0, 3), (6,0)]


def test_calculate_anti_nodes_horizontally():
    test_map = [
        ['.', '.', 'a', '.', 'a', '.', '.'],
    ]

    pair = AntennasPair(
        AntennaPoint(0, 2, 'a'),
        AntennaPoint(0, 4, 'a')
    )

    assert pair.calculate_antinodes() == [(0, 0), (0, 6)]

def test_calculate_anti_nodes_vertically():
    """
        Expect two nodes at
        (0, 0), (6, 3)
    """
    test_map = [
        ["."],
        ["."],
        ["a"],
        ["."],
        ["a"],
        ["."],
        ["."],
    ]

    pair = AntennasPair(
        AntennaPoint(2, 0, 'a'),
        AntennaPoint(4, 0, 'a')
    )

    assert pair.calculate_antinodes() == [(0, 0), (6,0)]


def test_should_return_points_for_4_same_antennas():

    test_map = [
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", "a", "a", "."],
        [".", ".", ".", "."],
        [".", "a", "a", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."],
    ]

    assert len(find_antenna_points(test_map)['a']) == 4

def test_should_return_combinations_for_frequency():

    test_map = [
        [".", ".", ".", "."],
        [".", ".", ".", "."],
        [".", "a", "a", "."],
        [".", ".", ".", "."],
        [".", "a", "a", "."],
        [".", ".", ".", "."],
        [".", ".", ".", "."],
    ]

    assert len(combinations(test_map)['a']) == 6


def test_should_return_anti_nodes_to_put_on_map():

    test_map = [
        [".", ".", "a", "."],
        [".", ".", ".", "."],
        [".", "a", ".", "."],
        [".", ".", ".", "."],
        ["b", ".", "a", "."],
        [".", ".", ".", "."],
        [".", "b", ".", "."],
    ]

    assert len(combinations(test_map)['a']) == 3
    assert len(combinations(test_map)['b']) == 1

def test_found_anti_nodes_for_3_antennas():
    """
    it's possible to set only 4 anti nodes
    """
    test_map = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', 'a', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', 'a', '.'],
        ['.', '.', '.', '.', '.', 'a', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    ]

    nodes = detect_nodes(test_map)

    pprint(write_nodes_on_area(test_map, nodes))

    assert len(detect_nodes(test_map)) == 4

def test_found_anti_nodes_for_test_data():
    test_map = [
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '0', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '0', '.', '.', '.', '.'],
        ['.', '.', '.', '0', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', 'A', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', 'A', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', 'A', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.', '.', '.', '.', '.', '.']
    ]
    nodes = detect_nodes(test_map)

    pprint(write_nodes_on_area(test_map, nodes))

    assert len(nodes) == 14
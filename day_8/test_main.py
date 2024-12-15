from day_8.main import detect_nodes, AntennasPair, AntennaPoint


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

    assert pair.calculate_antinodes() == [(6,0), (0, 3)]


# def test_create_two_nodes():
#     """
#         Expect two nodes at
#         (0, 0), (6, 3)
#     """
#     test_map = [
#         [".", ".", ".", "."],
#         [".", ".", ".", "."],
#         [".", "a", ".", "."],
#         [".", ".", ".", "."],
#         [".", ".", "a", "."],
#         [".", ".", ".", "."],
#         [".", ".", ".", "."],
#     ]
#
#     assert detect_nodes(test_map) == [(0, 0), (6, 3)]

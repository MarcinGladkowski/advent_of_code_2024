from daty_10.main import PathIterator, Point


def test_find_next_element_for_two_paths():
    test_input = [
        [2, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9],
        [0, 1, 0],
        [2, 2, 2],
        [2, 3, 2],
        [2, 4, 2],
        [2, 5, 2],
        [2, 6, 2],
        [2, 7, 2],
        [2, 8, 2],
        [2, 9, 2]
    ]

    """9 moves for each point from root"""
    iterator = PathIterator(Point(1, 0), test_input)
    steps = 0
    result = []
    while steps <= 9:
        result = next(iterator)
        steps += 1



    print(result)

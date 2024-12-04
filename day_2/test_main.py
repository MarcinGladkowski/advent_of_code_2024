from day_2.main import is_decreasing, is_increasing, max_differ, analyze_reports


def test_is_decreasing():
    assert is_decreasing([3, 2, 1])
    assert is_decreasing([1, 2, 3]) == False
    assert is_decreasing([1, 1, 1]) == False


def test_is_increasing():
    assert is_increasing([1, 2, 3])
    assert is_increasing([1, 1, 1]) == False
    assert is_increasing([3, 2, 1]) == False


def test_max_difference():
    assert max_differ([1, 2, 3])
    assert max_differ([1, 0, 10]) == False


def test_analyze_reports():
    reports = [
        [7, 6, 4, 2, 1],
        [1, 2, 7, 8, 9],
        [9, 7, 6, 2, 1],
        [1, 3, 2, 4, 5],
        [8, 6, 4, 4, 1],
        [1, 3, 6, 7, 9]
    ]

    assert analyze_reports(reports) == 2

from day_9.main import decode, rearrange


def test_decode():
    assert decode('12345') == [0, None, None, 1, 1, 1, None, None, None, None, 2, 2, 2, 2, 2]


def test_rearrange():
    assert rearrange(
        [0, None, None, 1, 1, 1, None, None, None, None, 2, 2, 2, 2, 2]
    ) == [0, 1, 1, 1, 2, 2, 2, 2, 2, None, None, None, None, None, None]


def test_calculate_checksum_on_basic():
    assert sum([index * int(element) for index, element in enumerate('0099811188827773336446555566')]) == 1928

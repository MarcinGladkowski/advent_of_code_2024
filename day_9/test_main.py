from day_9.main import decode, rearrange, is_free_space_on_right_side


def test_decode():
    assert decode('12345') == [0, None, None, 1, 1, 1, None, None, None, None, 2, 2, 2, 2, 2]

def test_rearrange():
    assert rearrange(
        [0, None, None, 1, 1, 1, None, None, None, None, 2, 2, 2, 2, 2]
    ) == [0, 2, 2, 1, 1, 1, 2, 2, 2]

    assert rearrange(
        [0,0, None, None, None, 1,1,1, None, None, None, 2, None, None, None, 3,3,3, None, 4,4, None, 5,5,5,5, None, 6,6,6,6, None,
         7,7,7, None, 8,8,8,8,9,9]
    ) == [0, 0, 9, 9, 8, 1, 1, 1, 8, 8, 8, 2, 7, 7, 7, 3, 3, 3, 6, 4, 4, 6, 5, 5, 5, 5, 6, 6]

def test_is_finished_rearrange():
    assert is_free_space_on_right_side([0, 2, 2, 1, 1, 1, None, None, None, None, 2, 2, 2, 2, 2]) == False
    assert is_free_space_on_right_side([0, 2, 2, 1, 1, 1, None, None, None, None])

def test_calculate_checksum_on_basic():
    assert sum([index * int(element) for index, element in enumerate('0099811188827773336446555566')]) == 1928

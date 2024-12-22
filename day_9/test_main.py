from day_9.main import decode, rearrange, is_free_space_on_right_side, calculate_hash, decode_to_blocks, is_free_slot, \
    Block, rearrange_blocks, join_blocks


def test_decode():
    assert decode('12345') == [0, None, None, 1, 1, 1, None, None, None, None, 2, 2, 2, 2, 2]


def test_rearrange():
    assert rearrange(
        [0, None, None, 1, 1, 1, None, None, None, None, 2, 2, 2, 2, 2]
    ) == [0, 2, 2, 1, 1, 1, 2, 2, 2]

    assert rearrange(
        [0, 0, None, None, None, 1, 1, 1, None, None, None, 2, None, None, None, 3, 3, 3, None, 4, 4, None, 5, 5, 5, 5,
         None, 6, 6, 6, 6, None,
         7, 7, 7, None, 8, 8, 8, 8, 9, 9]
    ) == [0, 0, 9, 9, 8, 1, 1, 1, 8, 8, 8, 2, 7, 7, 7, 3, 3, 3, 6, 4, 4, 6, 5, 5, 5, 5, 6, 6]


def test_is_finished_rearrange():
    assert is_free_space_on_right_side([0, 2, 2, 1, 1, 1, None, None, None, None, 2, 2, 2, 2, 2]) == False
    assert is_free_space_on_right_side([0, 2, 2, 1, 1, 1, None, None, None, None])


def test_calculate_checksum_on_basic():
    assert sum([index * int(element) for index, element in enumerate('0099811188827773336446555566')]) == 1928
    """Replaces none with zeros"""
    assert calculate_hash(
        [0, 0, 9, 9, 2, 1, 1, 1, 7, 7, 7, 0, 4, 4, 0, 3, 3, 3, 0, 0, 0, 0, 5, 5, 5, 5, 0, 6, 6, 6, 6, 0, 0, 0, 0, 0, 8,
         8, 8, 8, 0, 0]
    ) == 2858


def test_decode_to_groups():
    assert decode_to_blocks('2333133121414131402') == [
        [0, 0], [None, None, None], [1, 1, 1], [None, None, None], [2], [None, None, None], [3, 3, 3], [None], [4, 4],
        [None], [5, 5, 5, 5], [None], [6, 6, 6, 6], [None], [7, 7, 7], [None], [8, 8, 8, 8], [9, 9]
    ]

def test_is_free_slot():
    assert is_free_slot([None, None, None])
    assert is_free_slot([0, 0, 0]) == False


def test_decode_to_blocks():
    """
        00...111
    """
    result = decode_to_blocks('233')

    assert len(result) == 3
    assert Block(5, 7, 1) == result[2]
    assert Block(2, 4, None) == result[1]
    assert Block(0, 1, 0) == result[0]


def test_decode_and_encode():
    blocks = decode_to_blocks('233')
    assert join_blocks(blocks) == '00...111'


def test_rearrange_blocks_for_split_contains():
    blocks = decode_to_blocks('2321')
    assert len(blocks) == 4
    rearrange_blocks(blocks)




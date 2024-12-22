import re

from day_9.main import decode, rearrange, is_free_space_on_right_side, calculate_hash, decode_to_groups, \
    rearrange_groups, is_free_slot, rearrange_with_regular_expression


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
    assert decode_to_groups('2333133121414131402') == [
        [0, 0], [None, None, None], [1, 1, 1], [None, None, None], [2], [None, None, None], [3, 3, 3], [None], [4, 4],
        [None], [5, 5, 5, 5], [None], [6, 6, 6, 6], [None], [7, 7, 7], [None], [8, 8, 8, 8], [9, 9]
    ]

def test_is_free_slot():
    assert is_free_slot([None, None, None])
    assert is_free_slot([0, 0, 0]) == False

def test_move_block_and_fill_block_to_the_end():
    assert (rearrange_groups([[0, 0], [None, None, None], [1, 1, 1], [9, 9]]) == [[0, 0], [9, 9], [None], [1, 1, 1], [None, None]])

def test_move_block_from_end():
    assert rearrange_groups([[None, None],[9,9]]) == [[9,9],[None, None]]

def test_move_shorter_block_and_split_it_up():
    assert (rearrange_groups([[0, 0], [None], [1, 1, 1], [2], [7, 7, 7]]) == [[0, 0], [2], [1, 1, 1], [None], [7, 7, 7]])

def test_rearrange_with_groups_for_test_case():
    assert rearrange_groups(
        [
            [0, 0], [None, None, None], [1, 1, 1], [None, None, None], [2], [None, None, None], [3, 3, 3], [None],
            [4, 4],
            [None], [5, 5, 5, 5], [None], [6, 6, 6, 6], [None], [7, 7, 7], [None], [8, 8, 8, 8], [9, 9]
        ]
    ) == [
               [0, 0], [9, 9], [2], [1, 1, 1], [7, 7, 7], [None], [4, 4], [None], [3, 3, 3], [None, None, None, None],
               [5, 5, 5, 5], [None], [6, 6, 6, 6], [None, None, None, None, None], [8, 8, 8, 8], [None, None]
           ]

def test_solution_on_regular_expression():

    result = rearrange_with_regular_expression(
        [
            [0, 0], [None, None, None], [1, 1, 1], [None, None, None], [2], [None, None, None], [3, 3, 3], [None],
            [4, 4],
            [None], [5, 5, 5, 5], [None], [6, 6, 6, 6], [None], [7, 7, 7], [None], [8, 8, 8, 8], [9, 9]
        ],
        '00...111...2...333.44.5555.6666.777.888899'
    )

    assert True

def test_move_block_from_end_with_re():

    #print('..99'[2:4])
    assert rearrange_with_regular_expression(
        [[None, None],[9,9]],
        '..99'
    ) == '99..'
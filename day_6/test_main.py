import pytest

from day_6.main import GuardWalker, Cursor


def test_found_initial_position():
    test_input = [
        ['.','.','.'],
        ['.','^','.'],
        ['.','.','.'],
    ]
    assert Cursor(1,1) == GuardWalker(test_input).initial_position()

def test_move_up():
    walker = next(GuardWalker([
        ['.','.','.'],
        ['.','^','.'],
        ['.','.','.'],
    ]))
    assert walker.cursor == Cursor(0, 1)
    assert walker.steps == 1

def test_move_down():
    walker = next(GuardWalker([
        ['.','.','.'],
        ['.','v','.'],
        ['.','.','.'],
    ]))
    assert walker.cursor == Cursor(2, 1)
    assert walker.steps == 1

def test_move_left():
    walker = next(GuardWalker([
        ['.','.','.'],
        ['.','<','.'],
        ['.','.','.'],
    ]))
    assert walker.cursor == Cursor(1, 0)
    assert walker.steps == 1

def test_move_right():
    walker = next(GuardWalker([
        ['.','.','.'],
        ['.','>','.'],
        ['.','.','.'],
    ]))
    assert walker.cursor == Cursor(1, 2)
    assert walker.steps == 1

def test_turn_while_goes_up():
    walker = next(GuardWalker([
        ['.','#','.'],
        ['.','^','.'],
        ['.','.','.'],
    ]))
    assert walker.cursor == Cursor(1, 2)
    assert walker.steps == 1

def test_turn_while_goes_down():
    walker = next(GuardWalker([
        ['.','.','.'],
        ['.','v','.'],
        ['.','#','.'],
    ]))
    assert walker.cursor == Cursor(1, 0)
    assert walker.steps == 1

def test_turn_while_goes_left():
    walker = next(GuardWalker([
        ['.','.','.'],
        ['#','<','.'],
        ['.','.','.'],
    ]))
    assert walker.cursor == Cursor(0, 1)
    assert walker.steps == 1

def test_turn_while_goes_right():
    walker = next(GuardWalker([
        ['.','.','.'],
        ['.','>','#'],
        ['.','.','.'],
    ]))
    assert walker.cursor == Cursor(2, 1)
    assert walker.steps == 1

def test_finish_when_goes_out_of_map():
    with pytest.raises(StopIteration):
        next(GuardWalker([['^'],]))
        next(GuardWalker([['>'],]))
        next(GuardWalker([['<'],]))
        next(GuardWalker([['v'],]))
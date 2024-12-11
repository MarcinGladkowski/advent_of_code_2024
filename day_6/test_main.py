from day_6.main import GuardWalker


def test_found_initial_position():
    test_input = [
        ['.','.','.'],
        ['.','^','.'],
        ['.','.','.'],
    ]
    assert [1,1] == GuardWalker(test_input).initial_position()

def test_move_up():
    walker = next(GuardWalker([
        ['.','.','.'],
        ['.','^','.'],
        ['.','.','.'],
    ]))
    assert walker.cursor == [0, 1]
    assert walker.steps == 1

def test_move_down():
    walker = next(GuardWalker([
        ['.','.','.'],
        ['.','v','.'],
        ['.','.','.'],
    ]))
    assert walker.cursor == [2, 1]
    assert walker.steps == 1

def test_move_left():
    walker = next(GuardWalker([
        ['.','.','.'],
        ['.','<','.'],
        ['.','.','.'],
    ]))
    assert walker.cursor == [1, 0]
    assert walker.steps == 1

def test_move_right():
    walker = next(GuardWalker([
        ['.','.','.'],
        ['.','>','.'],
        ['.','.','.'],
    ]))
    assert walker.cursor == [1, 2]
    assert walker.steps == 1

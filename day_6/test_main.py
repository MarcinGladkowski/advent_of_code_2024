from day_6.main import GuardWalker


def test_found_initial_position():

    test_input = [
        ['.','.','.'],
        ['.','^','.'],
        ['.','.','.'],
    ]

    assert (1,1) == GuardWalker(test_input).initial_position()


def test_move_up():
    test_input = [
        ['.','.','.'],
        ['.','^','.'],
        ['.','.','.'],
    ]

    assert True

def test_move_down():
    pass

def test_move_left():
    pass

def test_move_right():
    pass

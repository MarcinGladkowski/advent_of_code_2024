from day_1.main import parse_input, calculate, similarity
from input_loader import load_test_intput

def test_parse_data():
    data = {
        'left': [3, 4, 2, 1, 3, 3],
        'right': [4, 3, 5, 3, 9, 3]
    }

    assert parse_input(load_test_intput()) == data

def test_calculate():
    data = {
        'left': [3, 4, 2, 1, 3, 3],
        'right': [4, 3, 5, 3, 9, 3]
    }

    assert calculate(data) == 11

def test_similarity():
    data = {
        'left': [3, 4, 2, 1, 3, 3],
        'right': [4, 3, 5, 3, 9, 3]
    }

    assert similarity(data) == 31



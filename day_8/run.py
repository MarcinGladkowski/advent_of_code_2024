from pprint import pprint

from day_8.main import detect_nodes
from input_loader import load_input, load_test_intput

test_data = [[i for i in x] for x in load_test_intput()]

assert len(detect_nodes(test_data)) == 14

data = [[i for i in x] for x in load_input()]

assert 379 == len(detect_nodes(data))
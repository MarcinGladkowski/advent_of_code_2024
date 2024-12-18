from pprint import pprint

from day_8.main import detect_nodes, write_nodes_on_area
from input_loader import load_input, load_test_intput

test_data = [[i for i in x] for x in load_test_intput()]

assert len(detect_nodes(test_data)) == 14
data = [[i for i in x] for x in load_input()]
assert 379 == len(detect_nodes(data))

### PART II
nodes = detect_nodes(test_data, True)
assert 34 == len(detect_nodes(test_data, True))
assert 1339 == len(detect_nodes(data, True))



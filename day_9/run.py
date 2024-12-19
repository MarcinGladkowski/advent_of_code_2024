from day_9.main import run
from input_loader import load_test_intput, load_input

test_data = load_test_intput()

assert run(test_data[0]) == 1928

data = load_input()

"""Takes few minutes"""
assert run(data[0]) == 6346871685398
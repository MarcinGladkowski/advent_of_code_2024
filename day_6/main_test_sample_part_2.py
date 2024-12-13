from day_6.main import GuardWalker
from input_loader import load_test_intput, load_input

# data = [[i for i in x] for x in load_test_intput()]
# assert 6 == GuardWalker(data).find_loops()

task_data = [[i for i in x] for x in load_input()]

# 2383 too high
print(GuardWalker(task_data).find_loops())


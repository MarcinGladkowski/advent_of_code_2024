from day_6.main import GuardWalker
from input_loader import load_test_intput, load_input

data = [[i for i in x] for x in load_test_intput()]

assert 41 == GuardWalker(data).run()

task_data = [[i for i in x] for x in load_input()]

assert 5453 ==  GuardWalker(task_data).run()
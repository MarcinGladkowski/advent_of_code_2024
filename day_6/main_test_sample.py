from os import write

from day_6.main import GuardWalker
from input_loader import load_test_intput, load_input

data = [[i for i in x] for x in load_test_intput()]

assert 41 == GuardWalker(data).run()

task_data = [[i for i in x] for x in load_input()]

assert 5453 ==  GuardWalker(task_data).run()
# def write_to_file(task_data, cursors: list):
#     f = open("map.txt", "a")
#     for cursor in cursors:
#         task_data[cursor.y][cursor.x] = '@'
#
#     for row in task_data:
#         f.write(''.join(row) + '\n')
#
#     f.close()
#
# write_to_file(task_data, result[1])
from day_9.main import run_for_full_moved, generate, decode
from input_loader import load_test_intput, load_input

# test_data = load_test_intput()
#
# assert run_for_full_moved(test_data[0]) == 2858

data = load_input()

#Wrong - too low: 116624657569
#Wrong - too low: 230632628781

output = generate(data[0])
# with open('rearranged_input.txt', 'w+') as file:
#     file.write(output)
#     file.flush()
#     file.close()

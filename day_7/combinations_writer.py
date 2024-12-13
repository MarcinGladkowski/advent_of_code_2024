from day_7.main import determine_operators_combinations

# 4096 combinations written to file - few minutes
for i in range(2, 11):
    combinations = determine_operators_combinations(['*', '+'], i)
    with open(f'{i}_length_combinations.txt', 'w+') as f:
        f.write(''.join([''.join(combination)+'\n' for combination in combinations]))
        f.close()



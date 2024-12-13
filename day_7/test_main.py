from day_7.main import calculate, determine_combination, determine_operators_combinations, execute_combination


def test_determine_operators_combination_for_3_operators():
    """
    Permutations with repeats 2**3 = 8
        +++
        ++*
        +**
        ***
        *++
        **+
        +*+
        *+*
    """
    assert len(determine_operators_combinations(['*', '+'], 3)) == 8

def test_execute_combination():
    assert execute_combination('+*+', [11,6,16,20]) == 292

def test_determine_by_multiply():
    assert 190 == determine_combination(190, [10, 19])
    assert 9688755 == determine_combination(9688755, [13,87,278,4,98,5,62,87])

def test_generate_result_for_set():
    test_data = [
        [190, [10, 19]],
        [3267, [81, 40, 27]],
        [83, [17, 5]],
        [156, [15, 6]],
        [7290, [6, 8, 6, 15]],
        [161011, [16, 10, 13]],
        [192, [17, 8, 14]],
        [21037, [9, 7, 18, 13]],
        [292, [11, 6, 16, 20]],
    ]

    assert calculate(test_data) == 3749

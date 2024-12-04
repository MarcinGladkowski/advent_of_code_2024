from day_3.main import filter_expressions, calculate_expressions, filter_expressions_with_do, \
    calculate_expressions_with_do_mode


def test_filter_expressions():
    assert filter_expressions(
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    ) == ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]

    assert filter_expressions("sdfsdmul(897,336)dsfsd") == ["mul(897,336)"]

def test_calculate():
    assert calculate_expressions(["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]) == 161

def test_filter_expressions_with_do():
    assert filter_expressions_with_do(
        "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
    ) == ["mul(2,4)", "don't()", "mul(5,5)", "mul(11,8)", "do()", "mul(8,5)"]

def test_calculate_with_do_mode():
    assert calculate_expressions_with_do_mode(
        ["mul(2,4)", "don't()", "mul(5,5)", "mul(11,8)", "do()", "mul(8,5)"]
    ) == 48
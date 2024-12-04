from day_3.main import filter_expressions, calculate_expressions


def test_filter_expressions():
    assert filter_expressions(
        "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    ) == ["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]

    assert filter_expressions("sdfsdmul(897,336)dsfsd") == ["mul(897,336)"]

def test_calculate():
    assert calculate_expressions(["mul(2,4)", "mul(5,5)", "mul(11,8)", "mul(8,5)"]) == 161
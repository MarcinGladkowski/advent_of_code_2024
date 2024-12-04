from input_loader import load_test_intput, load_input


def parse_input(data_input: list[str]):
    return [list(map(lambda x: int(x), x.split())) for x in data_input]

def save_report(report: list[int]) -> bool:
    return max_differ(report) and (is_increasing(report) or is_decreasing(report))


def analyze_reports(reports: list[list[int]]) -> int:
    return sum([1 if save_report(report) else 0 for report in reports])

def is_decreasing(numbers: list[int]) -> bool:
    for index, number in enumerate(numbers):
        if index == 0:
            continue
        if number >= numbers[index - 1]:
            return False

    return True

def is_increasing(numbers: list[int]) -> bool:
    for index, number in enumerate(numbers):
        if index == 0:
            continue
        if number <= numbers[index - 1]:
            return False

    return True

def max_differ(numbers: list[int], max_step: int = 3) -> bool:
    for index, number in enumerate(numbers):
        if index == 0:
            continue
        diff = abs(number - numbers[index - 1])

        if diff > max_step:
            return False

    return True


data = analyze_reports(parse_input(load_test_intput()))
print(data)

part_1 = analyze_reports(parse_input(load_input()))
print(part_1)

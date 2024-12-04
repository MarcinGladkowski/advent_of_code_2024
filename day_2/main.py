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

def analyze_reports_with_level_tolerance(reports: list[list[int]]) -> int:
    save_reports_count = analyze_reports(reports)
    """
        Test bad reports on permutations
    """
    for report in reports:
        if save_report(report) is False:
            permutations_result = analyze_reports(
                create_permutations(report)
            )

            if permutations_result > 0:
                save_reports_count += 1

    return save_reports_count

def create_permutations(report: list[int]) -> list[list[int]]:
    permutations = []
    for index in range(len(report)):
        new_report = report.copy()
        new_report.pop(index)
        permutations.append(new_report)

    return permutations

data = analyze_reports(parse_input(load_test_intput()))
print(data)

part_1 = analyze_reports(parse_input(load_input()))
print(part_1)

part_2 = analyze_reports_with_level_tolerance(parse_input(load_input()))
print(part_2)


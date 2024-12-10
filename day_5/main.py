from input_loader import load_input, load_test_intput


class Rule:

    def __init__(self, first, second):
       self.first = first
       self.second = second

    @classmethod
    def from_str(cls, data: str):
        first, second = data.split("|")
        return cls(int(first), int(second))

    def support_page(self, page: int):
        return self.first == page

    def numbers(self) -> set[int]:
        return {self.first, self.second}

    def __str__(self):
        return f"{self.first} | {self.second}"

    def __repr__(self):
        return f"{self.__class__.__name__}({self.first}, {self.second})"

class PagesUpdate:

    def __init__(self, pages: list[int]):
        self.pages = pages

    @classmethod
    def from_str(cls, data: str):
        filtered = list(filter(lambda x: len(x) > 0, data.split(",")))
        pages = list(map(lambda x: int(x), filtered))
        return cls(pages)

    def get_pages(self) -> set[int]:
        return set(self.pages)

    def is_rule_correct(self, rule: Rule) -> bool:
        return self.pages.index(rule.first) < self.pages.index(rule.second)

    def result(self) -> int:
        return self.pages[int(len(self.pages) / 2)]

    def __eq__(self, other) -> bool:
        return self.pages == other.pages

class Rules:

    def __init__(self):
        self.rules: list[Rule] = []

    def add_rule(self, rule: Rule):
        self.rules.append(rule)

    @classmethod
    def from_rules_str(cls, data: list[str]) -> "Rules":
        rules = cls()

        for rule in data:
            rules.add_rule(
                Rule.from_str(rule)
            )
        return rules

    def find_rules(self, page: PagesUpdate) -> set[Rule]:
        matching_rules = set()
        for rule in self.rules:
            intersection = rule.numbers() & page.get_pages()
            if len(intersection) == 2:
                matching_rules.add(rule)

        return matching_rules

    def count_by_first_occurence(self):
        count_map = {}
        for rule in self.rules:
            if count_map.get(rule.first) is None:
                count_map[rule.first] = 1
                continue

            count_map[rule.first] += 1

        return count_map


def page_update_correct(pages: PagesUpdate, rules: Rules) -> bool:
    rules_to_test = rules.find_rules(pages)

    for rule in rules_to_test:
        if pages.is_rule_correct(rule) is False:
            return False

    return True

def fix_page_update(pages: PagesUpdate, rules: Rules):
    """
        Count by the first number - it's an index in reverse order
    """
    rules_to_test = rules.find_rules(pages)

    rules_to_count = Rules()
    for rule in rules_to_test:
        rules_to_count.add_rule(rule)

    indexes = rules_to_count.count_by_first_occurence()

    result = [None for _ in range(len(indexes.values()))]
    for key, value in indexes.items():
        result.insert(value, key)

    result.reverse()
    result = list(filter(lambda x: x is not None, result))

    """Set last missing element"""
    missing_element = set(pages.pages).difference(set(result))
    result.append(missing_element.pop())
    return PagesUpdate.from_str(','.join(map(lambda x: str(x), result)))

def parse_data_to_rules_and_updates(data: list[str]):
    data_rules = Rules.from_rules_str(data[0:data.index('')])
    pages_updates = data[data.index(''):len(data)]
    return data_rules, pages_updates


def calculate(data: tuple[Rules, list[str]]) -> int:
    result = 0
    rules = data[0]

    for update in data[1]:
        page_update = PagesUpdate.from_str(update)
        if page_update.pages == []:
            continue

        if page_update_correct(page_update, rules):
            result += page_update.result()

    return result

def calculate_fixed(data: tuple[Rules, list[str]]) -> int:
    result = 0
    rules = data[0]

    for update in data[1]:
        page_update = PagesUpdate.from_str(update)
        if page_update.pages == []:
            continue

        if page_update_correct(page_update, rules) is False:
            fixed = fix_page_update(page_update, rules)
            result += fixed.result()

    return result


"""Part 1"""
assert 143 == calculate(parse_data_to_rules_and_updates(load_test_intput()))
assert 5166 == calculate(parse_data_to_rules_and_updates(load_input()))

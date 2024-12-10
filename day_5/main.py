from typing import Any


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
        pages = list(map(lambda x: int(x), data.split(",")))
        return cls(pages)

    def get_pages(self) -> set[int]:
        return set(self.pages)

    def is_rule_correct(self, rule: Rule) -> bool:
        return self.pages.index(rule.first) < self.pages.index(rule.second)

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

def page_update_correct(pages: PagesUpdate, rules: Rules) -> bool:
    rules_to_test = rules.find_rules(pages)

    for rule in rules_to_test:
        if pages.is_rule_correct(rule) is False:
            return False

    return True
from day_5.main import Rule, PagesUpdate, Rules

raw_test_rules = [
    '47|53',
    '97|13',
    '97|61',
    '97|47',
    '75|29',
    '61|13',
    '75|53',
    '29|13',
    '97|29',
    '53|29',
    '61|53',
    '97|53',
    '61|29',
    '47|13',
    '75|47',
    '97|75',
    '47|61',
    '75|61',
    '47|29',
    '75|13',
    '53|13',
]

test_rules = Rules.from_rules_str(raw_test_rules)

def test_parse_rules():
    assert isinstance(Rule.from_str("47|53"), Rule)

def test_find_related_rules():
    assert isinstance(PagesUpdate.from_str('75,47,61,53,29'), PagesUpdate)

def test_find_rules_to_check():
    """
    75 =  75|47, 75|61, 75|53, and 75|29. = 4
    47 = (75|47) 47|61, 47|53,  47|29. = 3
    61 = (75|61  47|61) (61|53  61|29). = 2
    53 = (53|29). = 1
    29 = []
    find by fist number and rest set
    """

    assert len(test_rules.find_rules(PagesUpdate.from_str('75,47,61,53,29'))) == 10
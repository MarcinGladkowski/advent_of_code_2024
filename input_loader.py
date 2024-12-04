
def load_test_intput():
    return load("test_input.txt")

def load_input():
    return load("input.txt")

def load(filename: str):
    with open(filename) as f:
        return [line.strip() for line in f]
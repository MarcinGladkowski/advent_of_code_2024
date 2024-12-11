from enum import Enum


class Move(Enum):
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'

class GuardWalker:

    def __init__(self, lab_map: list[list[str]]) -> None:
        self.lab_map = lab_map
        self.cursor = self.initial_position()

    def initial_position(self):
        for row_index, row in enumerate(self.lab_map):
            for col_index, col in enumerate(row):
                if col in Move:
                    return row_index, col_index

        raise RuntimeError('initial position of Guard not found')

    def __next__(self):
        pass

    def step(self):
        pass
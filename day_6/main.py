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
        self.steps = 0

    def initial_position(self):
        for row_index, row in enumerate(self.lab_map):
            for col_index, col in enumerate(row):
                if col in Move:
                    return [row_index, col_index]

        raise RuntimeError('initial position of Guard not found')

    def __next__(self) -> "GuardWalker":

        direction = self.lab_map[self.cursor[0]][self.cursor[1]]

        if Move.UP.value == direction:
            self.cursor[0] -= 1
            self.steps += 1
            return self

        if Move.DOWN.value == direction:
            self.cursor[0] += 1
            self.steps += 1
            return self

        if Move.LEFT.value == direction:
            self.cursor[1] -= 1
            self.steps += 1
            return self

        if Move.RIGHT.value == direction:
            self.cursor[1] += 1
            self.steps += 1
            return self

        return self
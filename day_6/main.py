from enum import Enum


class Move(Enum):
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'

obstacle = '#'


class Cursor:

    def __init__(self, y: int, x: int, direction: str = Move.UP.value):
        self.y = y
        self.x = x
        self.direction = direction

    def up(self):
        return Cursor(self.y - 1, self.x, Move.UP.value)

    def down(self):
        return Cursor(self.y + 1, self.x, Move.DOWN.value)

    def right(self):
        return Cursor(self.y, self.x + 1, Move.RIGHT.value)

    def left(self):
        return Cursor(self.y, self.x - 1, Move.LEFT.value)

    def __eq__(self, other):
        return self.y == other.y and self.x == other.x

class GuardWalker:

    def __init__(self, lab_map: list[list[str]]) -> None:
        self.lab_map = lab_map
        self.cursor: Cursor = self.initial_position()
        self.steps = 0

    def initial_position(self):
        for row_index, row in enumerate(self.lab_map):
            for col_index, col in enumerate(row):
                if col in Move:
                    return Cursor(row_index, col_index, self.lab_map[row_index][col_index])

        raise RuntimeError('initial position of Guard not found')

    def __next__(self) -> "GuardWalker":

        position = self.position(self.cursor)

        try:
            if Move.UP.value == position and self.is_allowed(self.cursor.up()):
                self.cursor = self.cursor.right()
                self.steps += 1
                return self

            if Move.DOWN.value == position and self.is_allowed(self.cursor.down()):
                self.cursor = self.cursor.left()
                self.steps += 1
                return self

            if Move.LEFT.value == position and self.is_allowed(self.cursor.left()):
                self.cursor = self.cursor.up()
                self.steps += 1
                return self

            if Move.RIGHT.value == position and self.is_allowed(self.cursor.right()):
                self.cursor = self.cursor.down()
                self.steps += 1
                return self

            if Move.UP.value == position:
                self.cursor = self.cursor.up()

            if Move.DOWN.value == position:
                self.cursor = self.cursor.down()

            if Move.LEFT.value == position:
                self.cursor = self.cursor.left()

            if Move.RIGHT.value == position:
                self.cursor = self.cursor.right()

            self.steps += 1
            return self
        except RuntimeError:
            raise StopIteration

    def position(self, cursor: Cursor) -> str:
        return self.lab_map[cursor.y][cursor.x]

    def is_allowed(self, cursor: Cursor) -> bool:
        try:
            return self.lab_map[cursor.y][cursor.x] == obstacle
        except IndexError:
            raise RuntimeError('out of map!')
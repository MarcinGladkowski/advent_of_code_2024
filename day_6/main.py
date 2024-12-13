from copy import deepcopy
from enum import Enum
from pprint import pprint


class Move(Enum):
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'

obstacle = '#'


class LoopDetectedError(RuntimeError):
    pass

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

    def __str__(self):
        return f'({self.y}, {self.x})'

    def __hash__(self):
        return hash(str(self))

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

        cursor_direction = self.cursor.direction

        try:
            if Move.UP.value == cursor_direction and self.is_obstacle(self.cursor.up()):
                self.cursor = self.cursor.right()
                self.steps += 1
                return self

            if Move.DOWN.value == cursor_direction and self.is_obstacle(self.cursor.down()):
                self.cursor = self.cursor.left()
                self.steps += 1
                return self

            if Move.LEFT.value == cursor_direction and self.is_obstacle(self.cursor.left()):
                self.cursor = self.cursor.up()
                self.steps += 1
                return self

            if Move.RIGHT.value == cursor_direction and self.is_obstacle(self.cursor.right()):
                self.cursor = self.cursor.down()
                self.steps += 1
                return self

            if Move.UP.value == cursor_direction:
                self.cursor = self.cursor.up()

            if Move.DOWN.value == cursor_direction:
                self.cursor = self.cursor.down()

            if Move.LEFT.value == cursor_direction:
                self.cursor = self.cursor.left()

            if Move.RIGHT.value == cursor_direction:
                self.cursor = self.cursor.right()

            self.steps += 1
            return self
        except RuntimeError:
            raise StopIteration

    def position(self, cursor: Cursor) -> str:
        return self.lab_map[cursor.y][cursor.x]

    def is_obstacle(self, cursor: Cursor) -> bool:
        try:
            return self.lab_map[cursor.y][cursor.x] == obstacle
        except IndexError:
            raise RuntimeError('out of map!')

    def run(self) -> int:
        walker = self
        visited = [self.initial_position()]
        while True:
            try:
                walker = next(walker)
                visited.append(walker.cursor)
            except StopIteration:
                # eliminate duplicates
                return len(set(visited))




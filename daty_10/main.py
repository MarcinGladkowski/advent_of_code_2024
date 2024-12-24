class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

class PathIterator:
    def __init__(self, start: Point, data_map: list):
        self.cursor = start
        self.data_map = data_map

    def __iter__(self):
        return self

    def __next__(self):
        """4 directions, UP, DOWN, LEFT, RIGHT"""
        expected_next_value = self.current_point_value() + 1

        to_move = []

        down = self.point_down()
        if self.value_by_point(down) == expected_next_value:
            to_move.append(
                PathIterator(down, self.data_map)
            )

        up = self.point_up()
        if self.value_by_point(up) == expected_next_value:
            to_move.append(
                PathIterator(up, self.data_map)
            )

        left = self.point_left()
        if self.value_by_point(left) == expected_next_value:
            to_move.append(
                PathIterator(left, self.data_map)
            )

        right = self.point_right()
        if self.value_by_point(right) == expected_next_value:
            to_move.append(
                PathIterator(right, self.data_map)
            )

        """Can run multiple paths (iterators)"""
        return to_move

    def current_point_value(self):
        return self.data_map[self.cursor.y][self.cursor.x]

    def value_by_point(self, point: Point):
        return self.data_map[point.y][point.x]

    def point_down(self):
        try:
            self.data_map[self.cursor.y + 1][self.cursor.x]
            return Point(self.cursor.y + 1, self.cursor.x)
        except IndexError:
            return None

    def point_up(self):
        try:
            self.data_map[self.cursor.y - 1][self.cursor.x]
            return Point(self.cursor.y - 1, self.cursor.x)
        except IndexError:
            return None

    def point_left(self):
        try:
            self.data_map[self.cursor.y][self.cursor.x - 1]
            return Point(self.cursor.y - 1, self.cursor.x - 1)
        except IndexError:
            return None

    def point_right(self):
        try:
            self.data_map[self.cursor.y][self.cursor.x + 1]
            return Point(self.cursor.y - 1, self.cursor.x + 1)
        except IndexError:
            return None

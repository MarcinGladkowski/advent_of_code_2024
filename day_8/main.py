import itertools


class AntennaPoint:
    def __init__(self, y: int, x: int, frequency: str, area: list):
        self.y = y
        self.x = x
        self.frequency = frequency
        self.area = area

    def __str__(self):
        return f"{self.y}:{self.x}"

    def __repr__(self):
        return f"{self.y}:{self.x}"

    def as_tuple(self) -> tuple:
        return self.y, self.x

    def to_bottom_right(self, y: int = 0, x: int = 0) -> "AntennaPoint":
        return AntennaPoint(self.y + y, self.x + x, self.frequency, self.area)

    def to_top_left(self, y: int = 0, x: int = 0) -> "AntennaPoint":
        return AntennaPoint(self.y - y, self.x - x, self.frequency, self.area)

    def to_top_right(self, y: int = 0, x: int = 0) -> "AntennaPoint":
        return AntennaPoint(self.y - y, self.x + x, self.frequency, self.area)

    def to_bottom_left(self, y: int = 0, x: int = 0) -> "AntennaPoint":
        return AntennaPoint(self.y + y, self.x - x, self.frequency, self.area)

    def to_left(self, y: int = 0, x: int = 0) -> "AntennaPoint":
        return AntennaPoint(self.y, self.x - x, self.frequency, self.area)

    def to_right(self, y: int = 0, x: int = 0) -> "AntennaPoint":
        return AntennaPoint(self.y, self.x + x, self.frequency, self.area)

    def to_up(self, y: int = 0, x: int = 0) -> "AntennaPoint":
        return AntennaPoint(self.y - y, self.x, self.frequency, self.area)

    def to_down(self, y: int = 0, x: int = 0) -> "AntennaPoint":
        return AntennaPoint(self.y + y, self.x, self.frequency, self.area)

class AntennasPair:
    def __init__(self, first_antenna: AntennaPoint, second_antenna: AntennaPoint = None):
        self.first_antenna = first_antenna
        self.second_antenna = second_antenna

    def is_same_frequency(self, antenna_point: AntennaPoint):
        return antenna_point.frequency == self.first_antenna.frequency

    def set_second_point(self, antenna_point: AntennaPoint):
        self.second_antenna = antenna_point

    @classmethod
    def from_tuple(cls, pair: tuple[AntennaPoint, AntennaPoint]):
        return cls(pair[0], pair[1])

    def calculate_antinodes(self, iteration: bool = False) -> list[tuple[int, int]]:
        """
            Based on two points we can find out expected positions for anti nodes

            We can define 4 main positions:
            a -> a (fully horizontal)
            a -> a (fully vertical)
            a -> a (diagonal from left top to right bottom)
            a -> a (diagonal from right top to left bottom)
        """
        nodes_strategies = [
            LeftToRightAntiNodes,
            RightToLeftAntiNodes,
            HorizontallyAntiNodes,
            VerticallyAntiNodes,
        ]

        if iteration:
            for node_strategy in nodes_strategies:
                if node_strategy.is_applicable(self):
                    return node_strategy.calculate_anti_nodes_iteration(self)

        for node_strategy in nodes_strategies:
            if node_strategy.is_applicable(self):
                return node_strategy.calculate_anti_nodes(self)

        raise RuntimeError("Any calculation found")


class LeftToRightAntiNodes:

    @staticmethod
    def is_applicable(antenna_pair: AntennasPair) -> bool:
        return antenna_pair.second_antenna.y > antenna_pair.first_antenna.y and antenna_pair.first_antenna.x < antenna_pair.second_antenna.x

    @staticmethod
    def calculate_anti_nodes(antennas_pair: AntennasPair) -> list[tuple[int, int]]:
        vertical_distance = antennas_pair.second_antenna.y - antennas_pair.first_antenna.y
        horizontal_distance = antennas_pair.second_antenna.x - antennas_pair.first_antenna.x
        return [
            (antennas_pair.first_antenna.y - vertical_distance, antennas_pair.first_antenna.x - horizontal_distance),
            (antennas_pair.second_antenna.y + vertical_distance, antennas_pair.second_antenna.x + horizontal_distance)
        ]

    @staticmethod
    def calculate_anti_nodes_iteration(antennas_pair: AntennasPair):
        vertical_distance = antennas_pair.second_antenna.y - antennas_pair.first_antenna.y
        horizontal_distance = antennas_pair.second_antenna.x - antennas_pair.first_antenna.x

        nodes = []

        next_iterator = StepIterator(
            antennas_pair.second_antenna,
            vertical_distance,
            horizontal_distance,
        )

        nodes.extend(next_iterator.to_bottom_right())

        previous_iterator = StepIterator(
            antennas_pair.first_antenna,
            vertical_distance,
            horizontal_distance,
        )

        nodes.extend(previous_iterator.to_top_left())

        return [node.as_tuple() for node in nodes]

class RightToLeftAntiNodes:

    @staticmethod
    def is_applicable(antenna_pair: AntennasPair) -> bool:
        return antenna_pair.second_antenna.y > antenna_pair.first_antenna.y and antenna_pair.first_antenna.x > antenna_pair.second_antenna.x

    @staticmethod
    def calculate_anti_nodes(antennas_pair: AntennasPair) -> list[tuple[int, int]]:
        vertical_distance = antennas_pair.second_antenna.y - antennas_pair.first_antenna.y
        horizontal_distance = antennas_pair.first_antenna.x - antennas_pair.second_antenna.x

        return [
            (antennas_pair.first_antenna.y - vertical_distance, antennas_pair.first_antenna.x + horizontal_distance),
            (antennas_pair.second_antenna.y + vertical_distance, antennas_pair.second_antenna.x - horizontal_distance)
        ]

    @staticmethod
    def calculate_anti_nodes_iteration(antennas_pair: AntennasPair):
        vertical_distance = antennas_pair.second_antenna.y - antennas_pair.first_antenna.y
        horizontal_distance = antennas_pair.first_antenna.x - antennas_pair.second_antenna.x

        nodes = []

        next_iterator = StepIterator(
            antennas_pair.second_antenna,
            vertical_distance,
            horizontal_distance,
        )

        nodes.extend(next_iterator.to_bottom_left())

        previous_iterator = StepIterator(
            antennas_pair.first_antenna,
            vertical_distance,
            horizontal_distance,
        )

        nodes.extend(previous_iterator.to_top_right())

        return [node.as_tuple() for node in nodes]


class HorizontallyAntiNodes:

    @staticmethod
    def is_applicable(antenna_pair: AntennasPair) -> bool:
        return antenna_pair.second_antenna.y == antenna_pair.first_antenna.y

    @staticmethod
    def calculate_anti_nodes(antennas_pair: AntennasPair) -> list[tuple[int, int]]:
        horizontal_distance = antennas_pair.second_antenna.x - antennas_pair.first_antenna.x

        return [
            (0, antennas_pair.first_antenna.x - horizontal_distance),
            (0, antennas_pair.second_antenna.x + horizontal_distance)
        ]

    @staticmethod
    def calculate_anti_nodes_iteration(antennas_pair: AntennasPair):
        horizontal_distance = antennas_pair.second_antenna.x - antennas_pair.first_antenna.x

        nodes = []

        next_iterator = StepIterator(
            antennas_pair.first_antenna,
            0,
            horizontal_distance,
        )

        nodes.extend(next_iterator.to_left())

        previous_iterator = StepIterator(
            antennas_pair.second_antenna,
            0,
            horizontal_distance,
        )

        nodes.extend(previous_iterator.to_right())

        return [node.as_tuple() for node in nodes]


class VerticallyAntiNodes:

    @staticmethod
    def is_applicable(antenna_pair: AntennasPair) -> bool:
        return antenna_pair.second_antenna.x == antenna_pair.first_antenna.x

    @staticmethod
    def calculate_anti_nodes(antennas_pair: AntennasPair) -> list[tuple[int, int]]:
        vertical_distance = antennas_pair.second_antenna.y - antennas_pair.first_antenna.y

        return [
            (antennas_pair.first_antenna.y - vertical_distance, 0),
            (antennas_pair.second_antenna.y + vertical_distance, 0)
        ]

    @staticmethod
    def calculate_anti_nodes_iteration(antennas_pair: AntennasPair):
        vertical_distance = antennas_pair.second_antenna.y - antennas_pair.first_antenna.y

        nodes = []

        next_iterator = StepIterator(
            antennas_pair.first_antenna,
            vertical_distance,
            0,
        )

        nodes.extend(next_iterator.to_up())

        previous_iterator = StepIterator(
            antennas_pair.second_antenna,
            vertical_distance,
            0,
        )

        nodes.extend(previous_iterator.to_down())

        return [node.as_tuple() for node in nodes]


def find_antenna_points(area: list[list[str]]) -> dict:
    """
    Map all antennas to points and then make combinations by frequency e.g `a`

    :param area:
    :return:
    """
    antenna_points = {}
    for y_index, row in enumerate(area):
        for x_index, value in enumerate(row):
            frequency = area[y_index][x_index]

            if frequency == '.':
                continue

            antenna_point = AntennaPoint(int(y_index), int(x_index), frequency, area)

            if antenna_points.get(frequency, None) is None:
                antenna_points[frequency] = [antenna_point]
                continue

            antenna_points[frequency].append(antenna_point)

    return antenna_points


def combinations(area: list) -> dict[str, set[AntennasPair]]:
    """
    # combinations = itertools.combinations([
    #     AntennaPoint(0, 1, 'a'),
    #     AntennaPoint(0, 2, 'a'),
    #     AntennaPoint(0, 3, 'a'),
    #     AntennaPoint(0, 4, 'a')
    # ], 2)
    :return:
    """
    antennas_points = find_antenna_points(area)

    frequency_combinations = {}

    for key, value in antennas_points.items():
        frequency_combinations[key] = {AntennasPair.from_tuple(combination) for combination in
                                       list(itertools.combinations(value, 2))}

    return frequency_combinations


def detect_nodes(area: list[list[str]], iteration_mode=False) -> list:
    """
       Nodes are created only for two antennas with the same letter [a-z][A-Z][0-9]] on the same line
       diagonal, vertical, horizontal ?
    """
    nodes = []
    for frequency, antenna_pairs in combinations(area).items():
        for pair in antenna_pairs:
            nodes_candidates = pair.calculate_antinodes(iteration_mode)
            for candidate in nodes_candidates:

                if candidate[0] < 0 or candidate[1] < 0:
                    continue

                try:
                    """not append while IndexError"""
                    area[candidate[0]][candidate[1]]
                    nodes.append(candidate)
                except IndexError:
                    continue

    return list(set(nodes))


def write_nodes_on_area(area: list, nodes: list) -> list[str]:
    for node in nodes:
        area[node[0]][node[1]] = '#'
    return area


class StepIterator:

    def __init__(
            self,
            antenna_point: AntennaPoint,
            vertical_step: int = 0,
            horizontal_step: int = 0
    ) -> None:
        self.antenna_point = antenna_point
        self.horizontal_step = horizontal_step
        self.vertical_step = vertical_step

    def to_bottom_right(self):
        nodes = []

        area = self.antenna_point.area
        cursor = self.antenna_point

        while True:
            last_second_node = cursor.to_bottom_right(
                self.vertical_step,
                self.horizontal_step
            )

            cursor = last_second_node

            if cursor.y >= len(area) or cursor.x >= len(area[0]):
                return nodes

            nodes.append(last_second_node)

    def to_top_left(self):
        nodes = []

        cursor = self.antenna_point

        while True:
            last_second_node = cursor.to_top_left(
                self.vertical_step,
                self.horizontal_step
            )

            cursor = last_second_node

            if cursor.y < 0 or cursor.x < 0:
                return nodes

            nodes.append(last_second_node)

    def to_top_right(self):
        nodes = []

        area = self.antenna_point.area
        cursor = self.antenna_point

        while True:
            last_second_node = cursor.to_top_right(
                self.vertical_step,
                self.horizontal_step
            )

            cursor = last_second_node

            if cursor.y >= len(area) or cursor.x >= len(area[0]):
                return nodes

            nodes.append(last_second_node)

    def to_bottom_left(self):
        nodes = []

        cursor = self.antenna_point

        while True:
            last_second_node = cursor.to_bottom_left(
                self.vertical_step,
                self.horizontal_step
            )

            cursor = last_second_node

            if cursor.y < 0 or cursor.x < 0:
                return nodes

            nodes.append(last_second_node)

    def to_left(self):
        nodes = []

        cursor = self.antenna_point

        while True:
            last_second_node = cursor.to_left(
                self.vertical_step,
                self.horizontal_step
            )

            cursor = last_second_node

            if cursor.y < 0 or cursor.x < 0:
                return nodes

            nodes.append(last_second_node)

    def to_right(self):
        nodes = []

        area = self.antenna_point.area
        cursor = self.antenna_point

        while True:
            last_second_node = cursor.to_right(
                self.vertical_step,
                self.horizontal_step
            )

            cursor = last_second_node

            if cursor.y >= len(area) or cursor.x >= len(area[0]):
                return nodes

            nodes.append(last_second_node)

    def to_up(self):
        nodes = []

        cursor = self.antenna_point

        while True:
            last_second_node = cursor.to_up(
                self.vertical_step,
                self.horizontal_step
            )

            cursor = last_second_node

            if cursor.y < 0 or cursor.x < 0:
                return nodes

            nodes.append(last_second_node)

    def to_down(self):
        nodes = []

        area = self.antenna_point.area
        cursor = self.antenna_point

        while True:
            last_second_node = cursor.to_down(
                self.vertical_step,
                self.horizontal_step
            )

            cursor = last_second_node

            if cursor.y >= len(area) or cursor.x >= len(area[0]):
                return nodes

            nodes.append(last_second_node)
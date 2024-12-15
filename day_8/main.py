class AntennaPoint:
    def __init__(self, y: int, x: int, frequency: str):
        self.y = y
        self.x = x
        self.frequency = frequency

class AntennasPair:
    def __init__(self, first_antenna: AntennaPoint, second_antenna: AntennaPoint = None):
        self.first_antenna = first_antenna
        self.second_antenna = second_antenna

    def is_same_frequency(self, antenna_point: AntennaPoint):
        return antenna_point.frequency == self.first_antenna.frequency

    def set_second_point(self, antenna_point: AntennaPoint):
        self.second_antenna = antenna_point

    def calculate_antinodes(self) -> list[tuple[int]]:
        """
            Based on two points we can find out expected positions for anti nodes
        """
        vertical_distance = self.second_antenna.y - self.first_antenna.y
        horizontal_distance = self.second_antenna.x - self.first_antenna.x

        top_left_node = (
            self.first_antenna.y - vertical_distance,
            self.first_antenna.x - horizontal_distance,
        )

        right_bottom_node = (
            self.second_antenna.y + vertical_distance,
            self.second_antenna.x + horizontal_distance,
        )

        return [top_left_node, right_bottom_node]

def detect_nodes(area: list[list[str]]):
    """
       Nodes are created only for two antennas with the same letter [a-z][A-Z][0-9]] on the same line
       diagonal, vertical, horizontal ?
    """

    pass
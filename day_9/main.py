import re


def decode(raw_input: str):
    decoded = []

    for index, element in enumerate(raw_input):
        if index % 2 != 0:
            decoded.extend([None for _ in range((int(element)))])
            continue

        decoded.extend([int(index / 2) for _ in range((int(element)))])

    return decoded


def rearrange(disk_map: list[int | None]) -> list[int]:
    """
    Rearranges the disk map
    """
    for index, element in enumerate(disk_map):

        if is_free_space_on_right_side(disk_map):
            return list(filter(lambda x: x is not None, disk_map))

        if element is None:
            disk_map[index] = get_from_right(disk_map)
            disk_map.insert(len(disk_map), None)

    return disk_map


def is_allowed_to_apply(disk_element: list[None | int], candidate: list[int]) -> bool:
    return len(disk_element) >= len(candidate)


def create_free_slot(number_of_elements: int) -> list[None]:
    return [None for _ in range(number_of_elements)]


def is_free_space_on_right_side(disk_map: list[int]) -> bool:
    """When all free spaces on right side we are finished operation of rearrange"""
    return len(list(filter(lambda x: x is not None, disk_map))) - 1 < disk_map.index(None)


def get_from_right(disk_map: list[int]) -> int:
    while True:
        last_element = disk_map.pop()

        if last_element is not None:
            return last_element


def calculate_hash(disk_map: list[int]) -> int:
    return sum([index * int(element) for index, element in enumerate(disk_map)])


def run(data_input: str) -> int:
    decoded = decode(data_input)
    rearranged = rearrange(decoded)

    return calculate_hash(rearranged)


def number_count(disk_map: list[int|None], number: str|int) -> int:
    return len(list(filter(lambda x: x == int(number), disk_map)))

def none_spots(disk_map: list[int|None]) -> list:
    raw_map = ''.join(['.' if el is None else str(el) for el in disk_map])

    return re.findall(r'\.+', raw_map)


def full_blocks_rearrange(disk_map: list[int | None]) -> list[int]:
    """
        Rearranges the disk map for part II
    """
    for index, element in enumerate(disk_map):
        if element is not None:
            # get number of elements for number
            # we can search elements and remove by number e.g. 13, 13, 13
            number_len = number_count(disk_map, element)
            # None sports
            print(none_spots(disk_map))


    return disk_map

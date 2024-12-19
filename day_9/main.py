from copy import deepcopy

def decode(raw_input: str):
    decoded = []

    for index, element in enumerate(raw_input):
        if index % 2 != 0:
            decoded.extend([None for _ in range((int(element)))])
            continue

        decoded.extend([int(index / 2) for _ in range((int(element)))])

    return decoded


def decode_to_groups(raw_input: str):

    decoded = []

    for index, element in enumerate(raw_input):
        if index % 2 != 0:

            if int(element) == 0:
                continue

            decoded.append([None for _ in range((int(element)))])
            continue

        decoded.append([int(index / 2) for _ in range((int(element)))])

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

def rearrange_groups(disk_map: list[list[int|None]]) -> list[list[int]]:
    """
        Remember to split if group is smaller than space

        Not enumerate by disk_map but from end not None groups
    """
    reverse_group_iterator = list(filter(lambda x: None not in x, deepcopy(disk_map)))
    reverse_group_iterator.reverse()

    for index, element in enumerate(reverse_group_iterator):
        print(element)

    return []


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

































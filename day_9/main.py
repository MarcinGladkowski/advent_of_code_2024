import re
from copy import deepcopy
from pprint import pprint


def decode(raw_input: str):
    decoded = []

    for index, element in enumerate(raw_input):
        if index % 2 != 0:
            decoded.extend([None for _ in range((int(element)))])
            continue

        decoded.extend([int(index / 2) for _ in range((int(element)))])

    return decoded

class Block:

    def __init__(self, index_from: int, index_to: int, element: int|None):
        self.index_from = index_from
        self.index_to = index_to
        self.element = element

    def __repr__(self):
        return f'{self.index_from}-{self.index_to}: {self.element}'

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


def is_free_slot(disk_element: list[None|int]) -> bool:
    return all(list(map(lambda x: x is None, disk_element)))

def is_allowed_to_apply(disk_element: list[None|int], candidate: list[int]) -> bool:
    return len(disk_element) >= len(candidate)

def rearrange_groups(disk_map: list[list[int|None]]) -> list[list[int]]:
    """
        Remember to split if group is smaller than space
        Not enumerate by disk_map but from end not None groups

        Required to be split None free blocks when new block is shorter than free space
        (manage count of elements in memory block)
    """
    reverse_group_iterator = list(deepcopy(disk_map))
    reverse_group_iterator.reverse()

    for index, candidate_to_allocate in enumerate(reverse_group_iterator):

        if index == (len(reverse_group_iterator) - 1):
            return disk_map

        if is_free_slot(candidate_to_allocate):
            continue

        for disk_index, disk_element in enumerate(disk_map):
            if is_free_slot(disk_element) and is_allowed_to_apply(disk_element, candidate_to_allocate):
                deallocate_used_element(candidate_to_allocate, disk_map, len(disk_map)-index-1)
                disk_allocate_space(candidate_to_allocate, disk_map, disk_index)
                break

    return disk_map


def deallocate_on_raw(disk_map_raw: str, replace_from: int, replace_to: int):
    replaced = []
    for index, element in enumerate(disk_map_raw):
        if replace_from < index <= replace_to:
            replaced.append('.')
            continue
        replaced.append(element)

    return ''.join(replaced)


def rearrange_with_regular_expression(disk_map: list[list[int|None]], raw_disk_map: str) -> str:

    reverse_group_iterator = list(deepcopy(disk_map))
    reverse_group_iterator.reverse()

    for index, candidate_to_allocate in enumerate(reverse_group_iterator):

        if index == (len(reverse_group_iterator) - 1):
            return raw_disk_map

        min_block_len = len(candidate_to_allocate)
        pattern = re.compile(fr'\.{{{min_block_len}}}')

        match = re.search(pattern, raw_disk_map)

        if match:
            disk_element_to_move = ''.join([str(number) for number in candidate_to_allocate])
            raw_disk_map = re.sub(pattern, disk_element_to_move, raw_disk_map)
            raw_disk_map = deallocate_on_raw(raw_disk_map, )

    return raw_disk_map

def disk_allocate_space(disk_element: list[int], disk_map: list, disk_index: int) -> None:
    """
    Can allocate partially
    e.g. 2 from 3 elements
    """
    if len(disk_element) == len(disk_map[disk_index]):
        disk_map[disk_index] = disk_element
        return None

    rest_of_disk_map = len(disk_map[disk_index]) - len(disk_element)
    free_to_allocate = [None for _ in range(rest_of_disk_map)]
    disk_map.insert(disk_index, free_to_allocate)
    disk_map.insert(disk_index, disk_element)
    disk_map.pop(disk_index+2)

def deallocate_used_element(disk_element: list[int], disk_map: list, disk_index: int) -> None:
    """
        When move element we need to move there None** block
    """
    disk_map[disk_index] = create_free_slot(len(disk_element))

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

































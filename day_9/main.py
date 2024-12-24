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


def number_block_length(disk_map: str, number: str) -> int:
    """
        length for number block to move
    """
    return len(re.findall(fr'{number}', disk_map))

def free_blocks_for_length(raw_map: str, number: int) -> list:
    """
        Check if exist free space for moving block length
    """
    return re.findall(fr'\.{{{number}}}', raw_map)

def is_free_block_to_allocate(raw_map: str, number: int, element: str|None = None) -> bool:
    """
    Check allocating only on free space on right side

    Split raw map by index
    """
    index = len(raw_map) if element is None else raw_map.index(element)
    numbers_count = number_block_length(raw_map, element)
    raw_map = raw_map[:index]

    for block in free_blocks_for_length(raw_map, numbers_count):

        if len(block) == 0 or numbers_count == 0:
            continue

        if len(block) >= numbers_count:
            return True

    return False

def full_blocks_rearrange(disk_map: str, decoded_disk: list[int|None]) -> str:
    """
        Rearranges the disk map for part II
        Add support for numbers > 9, 122,122,122 ...
    """
    for index, element in enumerate(reversed(decoded_disk)):

        if element == 0 or element is None:
            continue

        raw_element = str(element)

        element_count = number_block_length(disk_map, raw_element)

        if element is not None and is_free_block_to_allocate(disk_map, element_count, raw_element):
            # skip rest elements
            # get number of elements for number
            # we can search elements and remove by number e.g. 13, 13, 13
            # None sports for specific number
            # replace with none|dots
            disk_map = re.sub(
                fr'[{{{element}}}]+',
                '.'*element_count,
                disk_map,
                1
            )

            # put in spaces
            disk_map = re.sub(
                fr'\.{{{element_count}}}',
                raw_element*element_count,
                disk_map,
                1
            )

            # needs to rebuild decoded string and list ?

    return disk_map


def calculate_on_raw(raw: str):
    return sum([index * int(element) for index, element in enumerate(raw)])


def generate(data_input: str) -> str:
    decoded = decode(data_input)
    raw = ''.join([str(n) if n is not None else '.' for n in decoded])
    return full_blocks_rearrange(raw, decoded)

def run_for_full_moved(data_input: str) -> int:
    return calculate_hash([int(x) if x != '.' else 0 for x in generate(data_input)])































from configparser import NoOptionError


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

    def __str__(self):
        return str(self.element if self.element is not None else '.') * ((self.index_to - self.index_from) + 1)

    def __eq__(self, other):
        return (self.index_from == other.index_from
                and self.index_to == other.index_to
                and self.element == other.element)

    def is_empty(self) -> bool:
        return self.element is None

    def slots_reserved(self) -> int:
        return (self.index_to - self.index_from) + 1

    def to_allocate(self, to_set: "Block"):
        return self.slots_reserved() >= to_set.slots_reserved()

    def allocate(self, to_set: "Block"):
        if self.slots_reserved() == to_set.slots_reserved():
            """Allocated space is the same"""
            return Block(self.index_from, self.index_to, to_set.element), None
        """Needed None blocks for rest space"""
        free_spaces = self.slots_reserved() - to_set.slots_reserved()
        Block(self.index_to, self.index_to + free_spaces, None)

        return (
            Block(self.index_from, self.index_to - free_spaces, to_set.element),
            Block(self.index_to, self.index_to + free_spaces, None)
        )

    def reset_block(self):
        return Block(self.index_from, self.index_to, None)

def decode_to_blocks(raw_input: str):

    decoded = []
    cursor = 0
    for index, element in enumerate(raw_input):

        if index == 0:
            decoded.append(Block(cursor, cursor + int(element) - 1, index))
            cursor += int(element)
            continue

        if index % 2 != 0:
            decoded.append(Block(cursor, cursor + int(element) - 1, None))
            cursor += int(element)
            continue

        decoded.append(Block(cursor, cursor + int(element) - 1, index - 1))
        cursor += int(element)

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


"""Rearrange for part 2"""
def join_blocks(blocks: list[Block]) -> str:
    return ''.join([str(block) for block in blocks])

def rearrange_blocks(blocks: list[Block]) -> list[Block]:

    for index in reversed(range(len(blocks))):
        block_to_allocate = blocks[index]

        if index == 0:
            continue

        if block_to_allocate.is_empty():
            continue

        for block_index, block in enumerate(blocks):
            if block.is_empty() and block.to_allocate(block_to_allocate):

                print(f"\n [DEBUG] Applied block {block_to_allocate} into {block} \n")

                to_allocate = block.allocate(block_to_allocate)
                blocks[block_index] = to_allocate[0] # replace object
                blocks[index] = block_to_allocate.reset_block() # reset block

                if to_allocate[1]:
                    blocks.insert(block_index, to_allocate[1])

                # @TODO Merge None blocks next to None blocks
                break

    return blocks






























def decode(raw_input: str):

    decoded = []

    for index, element in enumerate(raw_input):
        if index == 0:
            decoded.append(index)
            continue
        if index % 2 != 0:
            decoded.extend([None for _ in range((int(element)))])
            continue

        decoded.extend([int(index / 2) for _ in range((int(element)))])

    return decoded

def rearrange(disk_map: list[int|None]) -> list[int|None]:
    """
    Rearranges the disk map
    """
    sorted(disk_map, key=lambda x: (x is None, x))
def rotate_left(dial_at: int, distance: int, min: int, max: int) -> int:
    """Towards smaller numbers."""
    dial_at = dial_at - distance
    dial_at = dial_at % max

    return dial_at


def rotate_right(dial_at: int, distance: int, min: int, max: int) -> int:
    """Towards bigger numbers."""
    dial_at = dial_at + distance
    dial_at = dial_at % max

    return dial_at


def rotate_dial_and_count_zeros(rotations: list[str], dial_start: int) -> int:
    print(f"The dial starts by pointing at {dial_start}.")

    zero_counter = 0
    dial_at = dial_start
    min = 0
    max = 100

    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])

        if direction == "L":
            dial_at = rotate_left(dial_at, distance, min, max)
        elif direction == "R":
            dial_at = rotate_right(dial_at, distance, min, max)
        else:
            raise NotImplementedError

        print(f"The dial is rotated {rotation} to point at {dial_at}.")

        # Or should this be before rotating?
        if dial_at == 0:
            zero_counter += 1

    return zero_counter

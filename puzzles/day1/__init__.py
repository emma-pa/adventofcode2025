def rotate_left(dial_at: int, distance: int, max: int) -> int:
    """Towards smaller numbers."""
    dial_at = dial_at - distance
    dial_at = dial_at % max

    return dial_at


def rotate_right(dial_at: int, distance: int, max: int) -> int:
    """Towards bigger numbers."""
    dial_at = dial_at + distance
    dial_at = dial_at % max

    return dial_at


def rotate_left_and_count_zero(
    dial_at: int, distance: int, max: int
) -> tuple[int, int]:
    count_zeros = (dial_at - distance) // max
    count_zeros = abs(
        count_zeros
    )  # Modulo of negative numbers give negative numbers but we just want to count the nof times 0 is crossed so it has to be positive

    # Starting from 0 doesn't mean crossing 0, so remove 1 in that case
    if dial_at == 0:
        count_zeros -= 1

    dial_at = rotate_left(dial_at, distance, max)
    return dial_at, count_zeros


def rotate_right_and_count_zero(
    dial_at: int, distance: int, max: int
) -> tuple[int, int]:
    # Reaching 0 is not like crossing 0, so count zero should be 0, not 1
    if dial_at + distance == max:
        count_zeros = 0
    else:
        count_zeros = (dial_at + distance) // max

    dial_at = rotate_right(dial_at, distance, max)

    # Reaching 0 is not like crossing 0, so count zero should be 0, not 1
    if dial_at == 0 and count_zeros != 0:
        count_zeros -= 1

    return dial_at, count_zeros


def rotate_dial_and_count_zeros(rotations: list[str], dial_start: int) -> int:
    print(f"The dial starts by pointing at {dial_start}.")

    zero_counter = 0
    dial_at = dial_start
    max = 100

    for rotation in rotations:
        direction = rotation[0]
        distance = int(rotation[1:])

        if direction == "L":
            dial_at = rotate_left(dial_at, distance, max)
        elif direction == "R":
            dial_at = rotate_right(dial_at, distance, max)
        else:
            raise NotImplementedError

        print(f"The dial is rotated {rotation} to point at {dial_at}.")

        # Or should this be before rotating?
        if dial_at == 0:
            zero_counter += 1

    return zero_counter


def rotate_dial_and_count_zeros_on_all_click(
    rotations: list[str], dial_start: int
) -> int:
    print(f"The dial starts by pointing at {dial_start}.")

    zero_counter = 0
    dial_at = dial_start
    max = 100

    for rotation in rotations:
        count_zeros = 0
        direction = rotation[0]
        distance = int(rotation[1:])

        if direction == "L":
            dial_at, count_zeros = rotate_left_and_count_zero(
                dial_at, distance, max
            )
        elif direction == "R":
            dial_at, count_zeros = rotate_right_and_count_zero(
                dial_at, distance, max
            )
        else:
            raise NotImplementedError

        log_msg = f"The dial is rotated {rotation} to point at {dial_at}."
        if count_zeros:
            log_msg += f" During this rotation, it points at 0 {count_zeros} times."
        print(log_msg)

        if dial_at == 0:
            zero_counter += 1

        zero_counter += count_zeros
        print(f"{zero_counter=}")

    return zero_counter

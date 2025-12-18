def is_id_invalid(id: str, nof_repetition: int = 2) -> bool:
    """If a sequence of digits that repeats itself nof_repetition times can be identified, then the id is invalid."""
    is_len_id_divisible_by_repetition = len(id) % nof_repetition == 0
    if not is_len_id_divisible_by_repetition:
        # In that case no pattern can be repeated enough time to match repetions
        return False

    len_sequence = (
        len(id) // nof_repetition
    )  # Since we made sure that the lenght of the id is divisible by the number of repetition this should have no remain
    # print(f"{len_sequence=}")
    sequences = []
    index_start = 0
    for _ in range(nof_repetition):
        index_end = index_start + len_sequence
        sequence = id[index_start:index_end]
        sequences.append(sequence)
        index_start = index_end

    assert len(sequences) == nof_repetition, (
        "Less sequence than required repetition of the sequence!"
    )

    # print(f"{sequences=}")
    # Doesn't work with nof_repetition 1
    sequence_prev = sequences[0]
    # print(f"{sequence_prev=}")
    for sequence in sequences[1:]:
        # print(f"{sequence=}")
        if sequence_prev != sequence:
            return False

    return True


def add_up_invalid_ids(ids: list[int], nof_repetition: int = 2) -> tuple[int, int]:
    total = 0
    nof_invalid_ids = 0
    for id in ids:
        if is_id_invalid(str(id), nof_repetition):
            total += id
            nof_invalid_ids += 1
            print(f"Id {id} is invalid.")

    return total, nof_invalid_ids


def add_up_invalid_ids_any_repetition(ids: list[int]) -> tuple[int, int]:
    total = 0
    nof_invalid_ids = 0
    for id in ids:
        str_id = str(id)
        max_nof_repetition = len(str_id)
        nof_repetition = 2
        is_invalid = False
        while nof_repetition <= max_nof_repetition and not is_invalid:
            is_invalid = is_id_invalid(str_id, nof_repetition)
            if is_invalid:
                total += id
                nof_invalid_ids += 1
                print(f"Id {id} is invalid.")
            nof_repetition += 1

    return total, nof_invalid_ids


def parse_ranges(ranges: list[tuple[int, int]]) -> int:
    total_in_all_ranges = 0
    total_nof_invalid_ids = 0
    for start, end in ranges:
        print(f"Parsing range ({start}, {end}).")
        ids_in_range = list(range(start, end + 1))
        total, nof_invalid_ids = add_up_invalid_ids(ids_in_range)
        total_nof_invalid_ids += nof_invalid_ids
        total_in_all_ranges += total

    print(f"Nof invalid ids {total_nof_invalid_ids}")
    return total_in_all_ranges


def parse_ranges_any_repetition(ranges: list[tuple[int, int]]) -> int:
    """Looks for any possible amount of repetitions of a pattern, not just 2 repetitions."""
    total_in_all_ranges = 0
    total_nof_invalid_ids = 0
    for start, end in ranges:
        print(f"Parsing range ({start}, {end}).")
        ids_in_range = list(range(start, end + 1))
        total, nof_invalid_ids = add_up_invalid_ids_any_repetition(ids_in_range)
        total_nof_invalid_ids += nof_invalid_ids
        total_in_all_ranges += total

    print(f"Nof invalid ids {total_nof_invalid_ids}")
    return total_in_all_ranges

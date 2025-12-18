from puzzles.day2 import parse_ranges, parse_ranges_any_repetition


def main():
    with open("puzzles/day2/ids.txt", "r") as file:
        ranges_str = file.read().split(",")

    ranges: list[tuple[int, int]] = []
    for range in ranges_str:
        start, end = range.split("-")
        ranges.append((int(start), int(end)))

    # total = parse_ranges(ranges)
    # print(f"Total invalid ids sum-up {total}")

    total = parse_ranges_any_repetition(ranges)
    print(f"Total invalid ids sum-up according to new rule (any amount of rep): {total}")


if __name__ == "__main__":
    main()
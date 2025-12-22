from puzzles.day4 import count_accessible_rolls, parse_shelves, remove_rolls, resolve_grid


def main():
    with open("puzzles/day4/shelves.txt", "r") as file:
        shelves = file.read().splitlines()

    grid = parse_shelves(shelves)
    # resolved_grid = resolve_grid(grid)
    # accessible_rolls = count_accessible_rolls(resolved_grid)
    # print(f"Nof accessible rolls: {accessible_rolls}")
    total_removed_rolls = remove_rolls(grid)
    print(f"Total removed rolls: {total_removed_rolls}")

if __name__ == "__main__":
    main()
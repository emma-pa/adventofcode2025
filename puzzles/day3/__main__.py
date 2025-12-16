from puzzles.day3 import compute_total_joltage


def main(nof_batteries=2):
    with open("puzzles/day3/banks.txt", "r") as file:
        banks = file.read().splitlines()

    total_joltage = compute_total_joltage(banks, nof_batteries)

    print(f"Total joltage: {total_joltage}")


if __name__ == "__main__":
    main()

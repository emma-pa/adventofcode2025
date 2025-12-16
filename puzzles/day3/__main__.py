from puzzles.day3 import compute_total_joltage

NOF_BATTERIES = 12

def main():
    with open("puzzles/day3/banks.txt", "r") as file:
        banks = file.read().splitlines()

    total_joltage = compute_total_joltage(banks, NOF_BATTERIES)

    print(f"Total joltage: {total_joltage}")


if __name__ == "__main__":
    main()

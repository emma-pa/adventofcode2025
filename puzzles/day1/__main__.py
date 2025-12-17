from puzzles.day1 import rotate_dial_and_count_zeros

DIAL_START = 50

def main():
    with open("puzzles/day1/rotations.txt", "r") as file:
        rotations = file.read().splitlines()

    print(len(rotations))

    count_zeros = rotate_dial_and_count_zeros(rotations, DIAL_START)

    print(f"Total zeros {count_zeros}")


if __name__ == "__main__":
    main()
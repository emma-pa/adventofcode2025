import unittest

from puzzles.day1 import (
    rotate_dial_and_count_zeros,
    rotate_dial_and_count_zeros_on_all_click,
    rotate_left,
    rotate_left_and_count_zero,
    rotate_right_and_count_zero,
)


test_rotations = [
    "L68",
    "L30",
    "R48",
    "L5",
    "R60",
    "L55",
    "L1",
    "L99",
    "R14",
    "L82",
]
max = 100
dial_start = 50


class TestDay1Part1(unittest.TestCase):
    def test_rotate_dial_and_count_zeros(self):
        count_zeros = rotate_dial_and_count_zeros(test_rotations, dial_start)
        assert count_zeros == 3

    def test_rotate_left(self):
        dial_at = 0
        distance = 876
        rotated_dial_at = rotate_left(dial_at, distance, max)
        assert rotated_dial_at == 24


class TestDay1Part2(unittest.TestCase):
    def test_rotate_right_and_count_zero_1000(self):
        dial_at = 50
        distance = 1000
        dial_at, count_zeros = rotate_right_and_count_zero(dial_at, distance, max)

        assert dial_at == 50
        assert count_zeros == 10

    def test_rotate_right_and_count_zero(self):
        dial_at = 98
        distance = 102
        dial_at, count_zeros = rotate_right_and_count_zero(dial_at, distance, max)

        assert dial_at == 0
        assert count_zeros == 1

    def test_rotate_right_and_count_zero_small(self):
        dial_at = 97
        distance = 13
        dial_at, count_zeros = rotate_right_and_count_zero(dial_at, distance, max)

        assert dial_at == 10
        assert count_zeros == 1

    def test_rotate_right_and_count_zero_to_100(self):
        dial_at = 52
        distance = 48
        dial_at, count_zeros = rotate_right_and_count_zero(dial_at, distance, max)

        assert dial_at == 0
        assert count_zeros == 0

    def test_rotate_left_and_count_zero(self):
        dial_at = 50
        distance = 1000
        dial_at, count_zeros = rotate_left_and_count_zero(dial_at, distance, max)

        assert dial_at == 50
        assert count_zeros == 10

    def test_rotate_left_and_count_zero_small(self):
        dial_at = 7
        distance = 13
        dial_at, count_zeros = rotate_left_and_count_zero(dial_at, distance, max)

        assert dial_at == 94
        assert count_zeros == 1

    def test_rotate_left_and_count_zero_to_100(self):
        dial_at = 50
        distance = 50
        dial_at, count_zeros = rotate_left_and_count_zero(dial_at, distance, max)

        assert dial_at == 0
        assert count_zeros == 0

    def test_rotate_dial_and_count_zeros_on_all_click(self):
        dial_start = 1
        test_rotations = ["L50", "R101"]
        count_zeros = rotate_dial_and_count_zeros_on_all_click(
            test_rotations, dial_start
        )
        print(f"Count zeros: {count_zeros}")
        assert count_zeros == 2

    def test_left_101(self):
        dial_at = 99
        distance = 100
        dial_at, count_zeros = rotate_left_and_count_zero(dial_at, distance, max)

        assert dial_at == 99
        assert count_zeros == 1

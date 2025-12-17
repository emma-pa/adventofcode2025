import unittest

from puzzles.day1 import rotate_dial_and_count_zeros, rotate_left


class TestDay1Part1(unittest.TestCase):
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
    min = 0
    max = 100
    count_zero = 0
    dial_start = 50

    def test_rotate_dial_and_count_zeros(self):
        count_zeros = rotate_dial_and_count_zeros(self.test_rotations, self.dial_start)
        assert count_zeros == 3

    def test_rotate_left(self):
        dial_at = 0
        distance = 876
        rotated_dial_at = rotate_left(dial_at, distance, self.min, self.max)
        assert rotated_dial_at == 24 # ??

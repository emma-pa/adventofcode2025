import unittest
from puzzles.day3 import compute_total_joltage, find_joltage


class TestDay3Part1(unittest.TestCase):
    test_banks = ["987654321111111", "811111111111119", "818181911112111"]
    expected_joltage = [98, 89, 92]
    nof_batteries = 2
    expected_total_joltage = sum(expected_joltage)

    def test_find_joltage(self):
        for i, bank in enumerate(self.test_banks):
            joltage_in_bank = find_joltage(bank, self.nof_batteries)

            assert joltage_in_bank == self.expected_joltage[i]

    def test_comput_total_joltage(self):
        total_joltage = compute_total_joltage(self.test_banks, self.nof_batteries)
        assert total_joltage == self.expected_total_joltage



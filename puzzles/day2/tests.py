import unittest

from puzzles.day2 import add_up_invalid_ids, add_up_invalid_ids_any_repetition, is_id_invalid, parse_ranges, parse_ranges_any_repetition


class TestDay2Part1(unittest.TestCase):
    def test_is_id_invalid(self):
        id = "1188511885"
        assert is_id_invalid(id)

    def test_add_up_invalid_ids(self):
        ids = list(range(1188511880, 1188511891))
        add_up_ids, nof_invalid_ids = add_up_invalid_ids(ids)
        assert add_up_ids == 1188511885 # Only one invalid id in this range
        assert nof_invalid_ids == 1

    def test_parse_ranges(self):
        ranges = [(11,22), (1188511880, 1188511890)]
        parsed_ranges = parse_ranges(ranges)
        assert parsed_ranges == 33 + 1188511885

class TestDay2Part2(unittest.TestCase):
    def test_parse_ranges_any_repetition(self):
        ranges = [(11,22), (1188511880, 1188511890), (2121212118, 2121212124), (824824821, 824824828)]
        parsed_ranges = parse_ranges_any_repetition(ranges)
        assert parsed_ranges == 33 + 1188511885 + 2121212121 + 824824824

    def test_is_id_invalid_7_rep(self):
        id = "1111111"
        assert is_id_invalid(id, 7)

    def test_add_up_invalid_ids_any_repetition_5_rep(self):
        ids = list(range(2121212118, 2121212125))
        add_up_ids, nof_invalid_ids = add_up_invalid_ids_any_repetition(ids)
        assert add_up_ids == 2121212121

    def test_add_up_invalid_ids_any_repetition_3_rep(self):
        ids = list(range(824824821, 824824829))
        add_up_ids, nof_invalid_ids = add_up_invalid_ids_any_repetition(ids)
        assert add_up_ids == 824824824
        assert nof_invalid_ids == 1
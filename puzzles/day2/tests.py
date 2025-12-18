import unittest

from puzzles.day2 import add_up_invalid_ids, is_id_invalid, parse_ranges


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
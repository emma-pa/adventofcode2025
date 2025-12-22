import unittest

from puzzles.day4 import (
    count_accessible_rolls,
    parse_shelves,
    remove_rolls,
    remove_rolls_from_grid,
    resolve_grid,
)
import numpy as np


test_shelves = [
    "..@@.@@@@.",
    "@@@.@.@.@@",
    "@@@@@.@.@@",
    "@.@@@@..@.",
    "@@.@@@@.@@",
    ".@@@@@@@.@",
    ".@.@.@.@@@",
    "@.@@@.@@@@",
    ".@@@@@@@@.",
    "@.@.@@@.@.",
]
test_parsed_grid = np.array(
    [
        [0, 0, 1, 1, 0, 1, 1, 1, 1, 0],
        [1, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 0, 1, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 0],
        [1, 1, 0, 1, 1, 1, 1, 0, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [1, 0, 1, 1, 1, 0, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [1, 0, 1, 0, 1, 1, 1, 0, 1, 0],
    ]
)
test_resolved_grid = np.array(
    [
        [0, 0, 1, 1, 0, 1, 1, 0, 1, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 1, 0, 0, 0, 0, 0, 1, 0],
    ]
)
test_next_state_grid = np.array(
    [
        [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 1, 1, 0, 1, 0, 1, 0, 1, 1],
        [1, 1, 1, 1, 1, 0, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 0, 0, 1, 0],
        [0, 1, 0, 1, 1, 1, 1, 0, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
        [0, 1, 0, 1, 0, 1, 0, 1, 1, 1],
        [0, 0, 1, 1, 1, 0, 1, 1, 1, 1],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
    ]
)


class TestDay4Part1(unittest.TestCase):
    def test_parse_grid(self):
        grid = parse_shelves(test_shelves)
        assert grid.shape == (len(test_shelves), len(test_shelves[0]))
        assert np.array_equal(grid, test_parsed_grid)

    def test_resolve_grid(self):
        resolved_grid = resolve_grid(test_parsed_grid)
        assert np.array_equal(resolved_grid, test_resolved_grid)

    def test_count_accessible_rolls(self):
        assert count_accessible_rolls(test_resolved_grid) == 13


class TestDay4Part2(unittest.TestCase):
    def test_remove_rolls_from_grid(self):
        new_state_grid = remove_rolls_from_grid(test_parsed_grid, test_resolved_grid)
        assert np.array_equal(new_state_grid, test_next_state_grid)

    def test_remove_rolls(self):
        total_removed_rolls = remove_rolls(test_parsed_grid)
        assert total_removed_rolls == 43
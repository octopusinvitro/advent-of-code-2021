# flake8: noqa: E241
from unittest import TestCase

from aoc.d15.map import Map


class TestMap(TestCase):
    def setUp(self):
        self.original = [
            [1, 1, 6],
            [1, 3, 8],
            [2, 1, 3]
        ]
        self.map = Map(self.original, factor=5, maximum_value=9)

    def test_keeps_the_original(self):
        self.assertEqual(self.map.original, self.original)

    def test_starts_replicating_the_original_factor_times(self):
        expected = [
            [1, 1, 6,   1, 1, 6,   1, 1, 6,   1, 1, 6,   1, 1, 6],
            [1, 3, 8,   1, 3, 8,   1, 3, 8,   1, 3, 8,   1, 3, 8],
            [2, 1, 3,   2, 1, 3,   2, 1, 3,   2, 1, 3,   2, 1, 3],

            [1, 1, 6,   1, 1, 6,   1, 1, 6,   1, 1, 6,   1, 1, 6],
            [1, 3, 8,   1, 3, 8,   1, 3, 8,   1, 3, 8,   1, 3, 8],
            [2, 1, 3,   2, 1, 3,   2, 1, 3,   2, 1, 3,   2, 1, 3],

            [1, 1, 6,   1, 1, 6,   1, 1, 6,   1, 1, 6,   1, 1, 6],
            [1, 3, 8,   1, 3, 8,   1, 3, 8,   1, 3, 8,   1, 3, 8],
            [2, 1, 3,   2, 1, 3,   2, 1, 3,   2, 1, 3,   2, 1, 3],

            [1, 1, 6,   1, 1, 6,   1, 1, 6,   1, 1, 6,   1, 1, 6],
            [1, 3, 8,   1, 3, 8,   1, 3, 8,   1, 3, 8,   1, 3, 8],
            [2, 1, 3,   2, 1, 3,   2, 1, 3,   2, 1, 3,   2, 1, 3],

            [1, 1, 6,   1, 1, 6,   1, 1, 6,   1, 1, 6,   1, 1, 6],
            [1, 3, 8,   1, 3, 8,   1, 3, 8,   1, 3, 8,   1, 3, 8],
            [2, 1, 3,   2, 1, 3,   2, 1, 3,   2, 1, 3,   2, 1, 3]
        ]
        self.assertEqual(self.map.map, expected)

    def test_increments_original_one_unit_horizontally_and_vertically(self):
        expected = [
            [1, 1, 6,   2, 2, 7,   3, 3, 8,   4, 4, 9,   5, 5, 1],
            [1, 3, 8,   2, 4, 9,   3, 5, 1,   4, 6, 2,   5, 7, 3],
            [2, 1, 3,   3, 2, 4,   4, 3, 5,   5, 4, 6,   6, 5, 7],

            [2, 2, 7,   3, 3, 8,   4, 4, 9,   5, 5, 1,   6, 6, 2],
            [2, 4, 9,   3, 5, 1,   4, 6, 2,   5, 7, 3,   6, 8, 4],
            [3, 2, 4,   4, 3, 5,   5, 4, 6,   6, 5, 7,   7, 6, 8],

            [3, 3, 8,   4, 4, 9,   5, 5, 1,   6, 6, 2,   7, 7, 3],
            [3, 5, 1,   4, 6, 2,   5, 7, 3,   6, 8, 4,   7, 9, 5],
            [4, 3, 5,   5, 4, 6,   6, 5, 7,   7, 6, 8,   8, 7, 9],

            [4, 4, 9,   5, 5, 1,   6, 6, 2,   7, 7, 3,   8, 8, 4],
            [4, 6, 2,   5, 7, 3,   6, 8, 4,   7, 9, 5,   8, 1, 6],
            [5, 4, 6,   6, 5, 7,   7, 6, 8,   8, 7, 9,   9, 8, 1],

            [5, 5, 1,   6, 6, 2,   7, 7, 3,   8, 8, 4,   9, 9, 5],
            [5, 7, 3,   6, 8, 4,   7, 9, 5,   8, 1, 6,   9, 2, 7],
            [6, 5, 7,   7, 6, 8,   8, 7, 9,   9, 8, 1,   1, 9, 2]
        ]

        self.assertEqual(self.map.full_map(), expected)

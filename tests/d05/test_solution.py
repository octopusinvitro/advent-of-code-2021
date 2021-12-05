from unittest import TestCase
from unittest.mock import Mock

from ..common import fixture_path

from aoc.file_parser import FileParser
from aoc.d05.solution import Solution


class TestSolution(TestCase):
    def setUp(self):
        path = fixture_path('d05', 'valid_input')
        lines = FileParser(['', path], Mock()).lines()
        self.solution = Solution(lines)

    def test_counts_intersections_between_non_diagonals(self):
        self.assertEqual(self.solution.part1(), 5)

    def test_counts_intersections_including_diagonals(self):
        self.assertEqual(self.solution.part2(), 12)

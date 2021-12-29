from unittest import TestCase
from unittest.mock import Mock

from ..common import fixture_path

from aoc.file_parser import FileParser
from aoc.d01.solution import Solution


class TestSolution(TestCase):
    def setUp(self):
        path = fixture_path('d01', 'valid_input')
        depths = FileParser(path, Mock()).lines()
        self.solution = Solution(depths)

    def test_counts_larger_than_previous_in_groups_of_two(self):
        self.assertEqual(self.solution.part1(), 7)

    def test_counts_larger_than_previous_in_groups_of_three(self):
        self.assertEqual(self.solution.part2(), 5)

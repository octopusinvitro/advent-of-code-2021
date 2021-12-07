from unittest import TestCase
from unittest.mock import Mock

from ..common import fixture_path

from aoc.file_parser import FileParser
from aoc.d06.solution import Solution


class TestSolution(TestCase):
    def setUp(self):
        path = fixture_path('d06', 'valid_input')
        lines = FileParser(['', path], Mock()).lines()
        self.solution = Solution(lines)

    def test_80days(self):
        self.assertEqual(self.solution.part1(), 5934)

    def test_256days(self):
        self.assertEqual(self.solution.part2(), 26984457539)

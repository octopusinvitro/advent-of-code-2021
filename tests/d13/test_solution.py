from unittest import TestCase
from unittest.mock import Mock

from ..common import fixture_path

from aoc.file_parser import FileParser
from aoc.d13.solution import Solution


class TestSolution(TestCase):
    def setUp(self):
        path = fixture_path('d13', 'valid_input')
        lines = FileParser(['', path], Mock()).lines()
        self.solution = Solution(lines)

    def test_part1(self):
        self.assertEqual(self.solution.part1(), 17)

    def test_part2(self):
        self.assertEqual(self.solution.part2(), 16)

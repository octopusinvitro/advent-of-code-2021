from unittest import TestCase
from unittest.mock import Mock

from ..common import fixture_path

from aoc.file_parser import FileParser
from aoc.d02.solution import Solution


class TestSolution(TestCase):
    def setUp(self):
        path = fixture_path('d02', 'valid_input')
        directions = FileParser(path, Mock()).lines()
        self.solution = Solution(directions)

    def test_part1(self):
        self.assertEqual(self.solution.part1(), 150)

    def test_part2(self):
        self.assertEqual(self.solution.part2(), 900)

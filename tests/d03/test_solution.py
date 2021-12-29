from unittest import TestCase
from unittest.mock import Mock

from ..common import fixture_path

from aoc.file_parser import FileParser
from aoc.d03.solution import Solution


class TestSolution(TestCase):
    def setUp(self):
        path = fixture_path('d03', 'valid_input')
        report = FileParser(path, Mock()).lines()
        self.solution = Solution(report)

    def test_calculates_power(self):
        self.assertEqual(self.solution.part1(), 198)

    def test_calculates_life_support(self):
        self.assertEqual(self.solution.part2(), 230)

from unittest import TestCase
from unittest.mock import Mock

from ..common import fixture_path, data_path

from aoc.file_parser import FileParser
from aoc.d07.solution import Solution


class TestSolution(TestCase):
    def setUp(self):
        path = fixture_path('d07', 'valid_input')
        lines = FileParser(['', path], Mock()).lines()
        self.solution = Solution(lines)

    def test_part1(self):
        self.assertEqual(self.solution.part1(), 37)

    def test_part2(self):
        self.assertNotEqual(self.solution.part2(), 168)
        self.assertEqual(self.solution.part2_differences(), 168)

    def test_part2_with_input_data(self):
        path = data_path('d07')
        lines = FileParser(['', path], Mock()).lines()
        solution = Solution(lines)

        self.assertEqual(solution.part2(), 98231647)
        self.assertEqual(solution.part2_differences(), 98231647)

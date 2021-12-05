from unittest import TestCase

from aoc.d03.solution import Solution


class TestSolution(TestCase):
    def setUp(self):
        report = [
            '00100',
            '11110',
            '10110',
            '10111',
            '10101',
            '01111',
            '00111',
            '11100',
            '10000',
            '11001',
            '00010',
            '01010'
        ]
        self.solution = Solution(report)

    def test_calculates_power(self):
        self.assertEqual(self.solution.part1(), 198)

    def test_calculates_life_support(self):
        self.assertEqual(self.solution.part2(), 230)

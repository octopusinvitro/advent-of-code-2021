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

    def test_calculates_gamma(self):
        self.assertEqual(self.solution.part1().value1, 22)

    def test_calculates_epsilon(self):
        self.assertEqual(self.solution.part1().value2, 9)

    def test_calculates_power(self):
        self.assertEqual(self.solution.part1().product, 198)

    def test_calculates_oxygen(self):
        self.assertEqual(self.solution.part2().value1, 23)

    def test_calculates_co2(self):
        self.assertEqual(self.solution.part2().value2, 10)

    def test_calculates_life_support(self):
        self.assertEqual(self.solution.part2().product, 230)

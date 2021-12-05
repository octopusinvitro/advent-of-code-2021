from unittest import TestCase

from aoc.d02.solution import Solution


class TestSolution(TestCase):
    def setUp(self):
        directions = [
            'forward 5',
            'down 5',
            'forward 8',
            'up 3',
            'down 8',
            'forward 2'
        ]
        self.solution = Solution(directions)

    def test_part1_calculates_coordinates_product(self):
        self.assertEqual(self.solution.part1(), 150)

    def test_part1_has_default_product_if_no_lines_passed(self):
        self.assertEqual(Solution().part1(), 0)

    def test_part2_calculates_coordinates_product(self):
        self.assertEqual(self.solution.part2(), 900)

    def test_part2_has_default_product_if_no_lines_passed(self):
        self.assertEqual(Solution().part2(), 0)

from unittest import TestCase

from aoc.d01.solution import Solution


class TestSolution(TestCase):
    def setUp(self):
        depths = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
        self.solution = Solution(depths)

    def test_counts_larger_than_previous_in_groups_of_two(self):
        self.assertEqual(self.solution.part1(), 7)

    def test_counts_larger_than_previous_in_groups_of_three(self):
        self.assertEqual(self.solution.part2(), 5)

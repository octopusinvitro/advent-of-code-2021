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

    def test_part1_calculates_horizontal_coordinate(self):
        position = self.solution.part1()
        self.assertEqual(position.horizontal, 15)

    def test_part1_calculates_depth_coordinate(self):
        position = self.solution.part1()
        self.assertEqual(position.depth, 10)

    def test_part1_calculates_coordinates_product(self):
        position = self.solution.part1()
        self.assertEqual(position.product, 150)

    def test_part1_has_default_horizontal_if_no_lines_passed(self):
        position = Solution().part1()
        self.assertEqual(position.horizontal, 0)

    def test_part1_has_default_depth_if_no_lines_passed(self):
        position = Solution().part1()
        self.assertEqual(position.depth, 0)

    def test_part1_has_default_product_if_no_lines_passed(self):
        position = Solution().part1()
        self.assertEqual(position.product, 0)

    def test_part2_calculates_horizontal_coordinate(self):
        position = self.solution.part2()
        self.assertEqual(position.horizontal, 15)

    def test_part2_calculates_depth_coordinate(self):
        position = self.solution.part2()
        self.assertEqual(position.depth, 60)

    def test_part2_calculates_coordinates_product(self):
        position = self.solution.part2()
        self.assertEqual(position.product, 900)

    def test_part2_has_default_horizontal_if_no_lines_passed(self):
        position = Solution().part2()
        self.assertEqual(position.horizontal, 0)

    def test_part2_has_default_depth_if_no_lines_passed(self):
        position = Solution().part2()
        self.assertEqual(position.depth, 0)

    def test_part2_has_default_product_if_no_lines_passed(self):
        position = Solution().part2()
        self.assertEqual(position.product, 0)

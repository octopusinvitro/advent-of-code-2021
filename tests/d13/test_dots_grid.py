from unittest import TestCase

from aoc.d13.dots_grid import DotsGrid


class TestDotsGrid(TestCase):
    def setUp(self):
        dots = {
            (0, 0), (0, 1), (0, 2), (0, 3), (0, 4),
            (1, 0), (1, 4),
            (2, 0), (2, 4),
            (3, 0), (3, 4),
            (4, 0), (4, 1), (4, 2), (4, 3), (4, 4)
        }

        self.grid = DotsGrid(dots)

    def test_creates_grid_to_print(self):
        grid = [
            ['#', '#', '#', '#', '#'],
            ['#', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', '#'],
            ['#', ' ', ' ', ' ', '#'],
            ['#', '#', '#', '#', '#']
        ]
        self.assertEqual(self.grid.build(), grid)

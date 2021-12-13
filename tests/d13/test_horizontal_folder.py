from unittest import TestCase

from aoc.d13.horizontal_folder import HorizontalFolder


class TestHorizontalFolder(TestCase):
    def setUp(self):
        self.folder = HorizontalFolder()

    def test_calculates_dots_after_one_fold(self):
        dots = {
            (3, 0), (13, 0), (14, 0),
            (10, 1),
            (14, 2),
            (0, 3), (4, 3),
            (1, 4), (11, 4),
            (0, 6), (10, 6), (12, 6),
            (4, 8), (10, 8),
            (0, 9), (10, 9),
            (4, 10), (12, 10)
        }
        merged = {
            (3, 4), (13, 4), (14, 4),
            (10, 3),
            (14, 2),
            (0, 1), (4, 1),
            (1, 0), (11, 0),
            (0, 0), (10, 0), (12, 0),
            (4, 2), (10, 2),
            (0, 3),
            (4, 4), (12, 4)
        }
        self.assertEqual(self.folder.fold(dots, 5), merged)

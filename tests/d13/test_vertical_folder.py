from unittest import TestCase

from aoc.d13.vertical_folder import VerticalFolder


class TestVerticalFolder(TestCase):
    def setUp(self):
        self.folder = VerticalFolder()

    def test_calculates_dots_after_one_fold(self):
        dots = {
            (0, 3), (0, 6), (0, 9),
            (1, 4),
            (3, 0),
            (4, 3), (4, 8), (4, 10),
            (10, 1), (10, 6), (10, 8), (10, 9),
            (11, 4),
            (12, 6), (12, 10),
            (13, 0),
            (14, 0), (14, 2)
        }
        merged = {
            (0, 3), (0, 6), (0, 9),
            (1, 4),
            (3, 0),
            (4, 3), (4, 8), (4, 10),
            (4, 1), (4, 6), (4, 9),
            (3, 4),
            (2, 6), (2, 10),
            (1, 0),
            (0, 0), (0, 2)
        }
        self.assertEqual(self.folder.fold(dots, 7), merged)

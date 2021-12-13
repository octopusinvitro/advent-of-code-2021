from unittest import TestCase

from aoc.d13.manual import Manual
from aoc.d13.direction import Direction


class TestManual(TestCase):
    def setUp(self):
        lines = [
            '6,10',
            '0,14',
            '9,10',
            '0,3',
            '10,4',
            '4,11',
            '6,0',
            '6,12',
            '4,1',
            '0,13',
            '10,12',
            '3,4',
            '3,0',
            '8,4',
            '1,10',
            '2,14',
            '8,10',
            '9,0',
            '',
            'fold along y=7',
            'fold along x=5'
        ]
        self.manual = Manual(lines)

    def test_returns_the_dots(self):
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
        self.assertEqual(self.manual.dots(), dots)

    def test_returns_sorted_folding_instructions(self):
        instructions = [(Direction.UP, 7), (Direction.LEFT, 5)]
        self.assertEqual(self.manual.instructions(), instructions)

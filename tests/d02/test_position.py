from unittest import TestCase

from aoc.d02.position import Position


class TestPosition(TestCase):
    def test_calculates_coordinates_product(self):
        position = Position(2, 3)
        self.assertEqual(position.product, 6)

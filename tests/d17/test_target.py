from unittest import TestCase

from aoc.d17.point import Point
from aoc.d17.target import Target


class TestTarget(TestCase):
    def setUp(self):
        self.target = Target('target area: x=20..30, y=-10..-5')

    def test_has_min_x(self):
        self.assertEqual(self.target.min_x, 20)

    def test_has_max_x(self):
        self.assertEqual(self.target.max_x, 30)

    def test_has_min_y(self):
        self.assertEqual(self.target.min_y, -10)

    def test_has_max_y(self):
        self.assertEqual(self.target.max_y, -5)

    def test_calculates_maximum_heigth(self):
        self.assertEqual(self.target.maximum_height(), 45)

    def test_detects_collision(self):
        self.assertTrue(self.target.was_hit(Point(28, -7)), -5)

    def test_detects_no_collision(self):
        self.assertFalse(self.target.was_hit(Point(0, 0)), -5)

    def test_detects_x_outbound(self):
        self.assertTrue(self.target.was_passed(Point(31, -5)))

    def test_detects_y_outbound(self):
        self.assertTrue(self.target.was_passed(Point(20, -12)))

    def test_detects_no_outbound(self):
        self.assertFalse(self.target.was_passed(Point(0, 0)))
        self.assertFalse(self.target.was_passed(Point(0, -5)))
        self.assertFalse(self.target.was_passed(Point(20, 0)))

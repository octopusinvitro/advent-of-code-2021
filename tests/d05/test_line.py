from unittest import TestCase

from aoc.d05.line import Line


class TestLine(TestCase):
    def test_has_a_starting_x(self):
        self.assertEqual(Line('309,347 -> 123,464').start_x, 309)

    def test_has_a_starting_y(self):
        self.assertEqual(Line('309,347 -> 123,464').start_y, 347)

    def test_has_an_ending_x(self):
        self.assertEqual(Line('309,347 -> 123,464').end_x, 123)

    def test_has_an_ending_y(self):
        self.assertEqual(Line('309,347 -> 123,464').end_y, 464)

    def test_can_be_vertical(self):
        self.assertTrue(Line('309,347 -> 309,464').vertical())

    def test_can_be_horizontal(self):
        self.assertTrue(Line('309,347 -> 123,347').horizontal())

    def test_can_be_diagonal(self):
        self.assertTrue(Line('309,347 -> 123,464').diagonal())

    def test_calculates_points_for_horizontal_line(self):
        self.assertEqual(Line('0,9 -> 2,9').points(), ['0,9', '1,9', '2,9'])

    def test_calculates_points_for_inverse_horizontal_line(self):
        self.assertEqual(Line('2,9 -> 0,9').points(), ['2,9', '1,9', '0,9'])

    def test_calculates_points_for_vertical_line(self):
        self.assertEqual(Line('9,0 -> 9,2').points(), ['9,0', '9,1', '9,2'])

    def test_calculates_points_for_inverse_vertical_line(self):
        self.assertEqual(Line('9,2 -> 9,0').points(), ['9,2', '9,1', '9,0'])

    def test_calculates_points_for_diagonal_line(self):
        self.assertEqual(Line('1,1 -> 3,3').points(), ['1,1', '2,2', '3,3'])

    def test_calculates_points_for_inverse_diagonal_line(self):
        self.assertEqual(Line('9,7 -> 7,9').points(), ['9,7', '8,8', '7,9'])

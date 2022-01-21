from unittest import TestCase

from aoc.d03.bit import Bit


class TestBit(TestCase):
    def test_calculates_ON_flip(self):
        self.assertEqual(Bit.flip(1), 0)

    def test_calculates_OFF_flip(self):
        self.assertEqual(Bit.flip(0), 1)

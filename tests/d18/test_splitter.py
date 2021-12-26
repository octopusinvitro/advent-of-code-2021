from unittest import TestCase

from aoc.d18.splitter import Splitter


class TestSplitter(TestCase):
    def test_splits_leftmost_regular_number(self):
        pair = '[[[[10,8],1],2],11]'
        s = '[[[[[5,5],8],1],2],11]'
        self.assertEqual(Splitter(pair).split(), s)

    def test_splits_leftmost_regular_number_rounding_right_up(self):
        pair = '[[[[9,8],1],2],11]'
        done = '[[[[9,8],1],2],[5,6]]'
        self.assertEqual(Splitter(pair).split(), done)

    def test_ignores_unsplittable(self):
        pair = '[[[[9,8],1],2],3]'
        self.assertIsNone(Splitter(pair).split())

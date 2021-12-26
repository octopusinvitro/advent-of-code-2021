from unittest import TestCase

from aoc.d18.magnitude import Magnitude


class TestMagnidude(TestCase):
    def test_calculates_magnitude_example1(self):
        self.assertEqual(Magnitude('[9,1]').calculate(), 29)

    def test_calculates_magnitude_example2(self):
        self.assertEqual(Magnitude('[1,9]').calculate(), 21)

    def test_calculates_magnitude_example3(self):
        self.assertEqual(Magnitude('[[9,1],[1,9]]').calculate(), 129)

    def test_calculates_magnitude_example4(self):
        self.assertEqual(Magnitude('[[1,2],[[3,4],5]]').calculate(), 143)

    def test_calculates_magnitude_example5(self):
        self.assertEqual(Magnitude('[[1,2],[5,[3,4]]]').calculate(), 119)

    def test_calculates_magnitude_example6(self):
        self.assertEqual(Magnitude('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]').calculate(), 1384)

    def test_calculates_magnitude_example7(self):
        self.assertEqual(Magnitude('[[[[1,1],[2,2]],[3,3]],[4,4]]').calculate(), 445)

    def test_calculates_magnitude_example8(self):
        self.assertEqual(Magnitude('[[[[3,0],[5,3]],[4,4]],[5,5]]').calculate(), 791)

    def test_calculates_magnitude_example9(self):
        self.assertEqual(Magnitude('[[[[5,0],[7,4]],[5,5]],[6,6]]').calculate(), 1137)

    def test_calculates_magnitude_example10(self):
        pair = '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'
        self.assertEqual(Magnitude(pair).calculate(), 3488)

    def test_calculates_magnitude_example11(self):
        pair = '[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]'
        self.assertEqual(Magnitude(pair).calculate(), 4140)

    def test_calculates_magnitude_example12(self):
        pair = '[[[[7,8],[6,6]],[[6,0],[7,7]]],[[[7,8],[8,8]],[[7,9],[0,6]]]]'
        self.assertEqual(Magnitude(pair).calculate(), 3993)

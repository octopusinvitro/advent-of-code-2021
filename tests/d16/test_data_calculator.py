from unittest import TestCase

from aoc.d16.data_calculator import DataCalculator
from tests.d16.type import Type


class TestDataCalculator(TestCase):
    def setUp(self):
        self.calculator = DataCalculator([2, 3, 2])

    def test_sums(self):
        self.assertEqual(self.calculator.calculate(Type.SUM), 7)

    def test_multiplies(self):
        self.assertEqual(self.calculator.calculate(Type.PRODUCT), 12)

    def test_finds_minimum(self):
        self.assertEqual(self.calculator.calculate(Type.MINIMUM), 2)

    def test_finds_maximum(self):
        self.assertEqual(self.calculator.calculate(Type.MAXIMUM), 3)

    def test_returns_same(self):
        self.assertEqual(self.calculator.calculate(Type.IDENTITY), [2, 3, 2])

    def test_detects_greater(self):
        calculator = DataCalculator([3, 2])
        self.assertEqual(calculator.calculate(Type.GREATER), 1)

    def test_detects_not_greater(self):
        calculator = DataCalculator([2, 3])
        self.assertEqual(calculator.calculate(Type.GREATER), 0)

    def test_detects_less(self):
        calculator = DataCalculator([2, 3])
        self.assertEqual(calculator.calculate(Type.LESS), 1)

    def test_detects_not_less(self):
        calculator = DataCalculator([3, 2])
        self.assertEqual(calculator.calculate(Type.LESS), 0)

    def test_detects_equal(self):
        calculator = DataCalculator([2, 2])
        self.assertEqual(calculator.calculate(Type.EQUAL), 1)

    def test_detects_not_equal(self):
        calculator = DataCalculator([1, 2])
        self.assertEqual(calculator.calculate(Type.EQUAL), 0)

    def test_returns_same_if_type_not_available(self):
        self.assertEqual(self.calculator.calculate(42), [2, 3, 2])

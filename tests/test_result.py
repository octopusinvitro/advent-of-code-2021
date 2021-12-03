from unittest import TestCase

from aoc.result import Result


class TestResult(TestCase):
    def test_calculates_product(self):
        result = Result(2, 3)
        self.assertEqual(result.product, 6)

from unittest import TestCase

from aoc.d07.crab_troop import CrabTroop


class TestCrabTroop(TestCase):
    def setUp(self):
        positions = [16, 1, 2, 0, 4, 2, 7, 1, 2, 14]
        self.troop = CrabTroop(positions)

    def test_calculates_linear_optimal_fuel_costs(self):
        differences = [14, 1, 0, 2, 2, 0, 5, 1, 0, 12]
        self.assertEqual(self.troop.linear_optimal_fuel_costs(), differences)

    def test_calculates_quadratic_optimal_fuel_costs(self):
        differences = [66, 10, 6, 15, 1, 6, 3, 10, 6, 45]
        self.assertNotEqual(self.troop.quadratic_optimal_fuel_costs(), differences)

    def test_calculates_quadratic_optimal_fuel_cost(self):
        self.assertEqual(self.troop.quadratic_optimal_fuel_cost(), 168)

from unittest import TestCase

from aoc.d06.lanternfish_population import LanternfishPopulation


class TestLanternfishPopulation(TestCase):
    def setUp(self):
        self.population = LanternfishPopulation()

    def test_loads_initial_state(self):
        counts = [0, 0, 0, 1, 0, 0, 0, 0, 0]
        self.assertEqual(self.population.simulate([3], 0), counts)

    # With one fish
    def test_simulates_day_1(self):
        counts = [0, 0, 1, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.population.simulate([3], 1), counts)

    def test_simulates_day_3(self):
        counts = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.population.simulate([3], 3), counts)

    def test_simulates_day_4(self):
        counts = [0, 0, 0, 0, 0, 0, 1, 0, 1]
        self.assertEqual(self.population.simulate([3], 4), counts)

    def test_simulates_day_10(self):
        counts = [1, 0, 1, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.population.simulate([3], 10), counts)

    def test_simulates_day_11(self):
        counts = [0, 1, 0, 0, 0, 0, 1, 0, 1]
        self.assertEqual(self.population.simulate([3], 11), counts)

    def test_simulates_day_17(self):
        counts = [1, 0, 2, 0, 1, 0, 0, 0, 0]
        self.assertEqual(self.population.simulate([3], 17), counts)

    def test_simulates_day_18(self):
        counts = [0, 2, 0, 1, 0, 0, 1, 0, 1]
        self.assertEqual(self.population.simulate([3], 18), counts)

    # With two fishes
    def test_accumulates_day_1(self):
        counts = [0, 0, 1, 1, 0, 0, 0, 0, 0]
        self.assertEqual(self.population.simulate([3, 4], 1), counts)

    def test_accumulates_day_3(self):
        counts = [1, 1, 0, 0, 0, 0, 0, 0, 0]
        self.assertEqual(self.population.simulate([3, 4], 3), counts)

    def test_accumulates_day_4(self):
        counts = [1, 0, 0, 0, 0, 0, 1, 0, 1]
        self.assertEqual(self.population.simulate([3, 4], 4), counts)

    def test_accumulates_day_5(self):
        counts = [0, 0, 0, 0, 0, 1, 1, 1, 1]
        self.assertEqual(self.population.simulate([3, 4], 5), counts)

    def test_accumulates_day_10(self):
        counts = [1, 1, 1, 1, 0, 0, 0, 0, 0]
        self.assertEqual(self.population.simulate([3, 4], 10), counts)

    def test_accumulates_day_11(self):
        counts = [1, 1, 1, 0, 0, 0, 1, 0, 1]
        self.assertEqual(self.population.simulate([3, 4], 11), counts)

    def test_accumulates_day_17(self):
        counts = [1, 1, 2, 2, 1, 1, 0, 0, 0]
        self.assertEqual(self.population.simulate([3, 4], 17), counts)

    def test_accumulates_day_18(self):
        counts = [1, 2, 2, 1, 1, 0, 1, 0, 1]
        self.assertEqual(self.population.simulate([3, 4], 18), counts)

from unittest import TestCase

from aoc.d11.energy_grid import EnergyGrid


class TestEnergyGrid(TestCase):
    def test_adds_one_energy_level_in_every_step(self):
        levels = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8]
        ]
        after_1_step = [
            [1, 2, 3],
            [4, 5, 6],
            [7, 8, 9]
        ]
        grid = EnergyGrid(levels)
        grid.simulate(1)
        self.assertEqual(grid.levels, after_1_step)

    def test_flashes_and_resets_when_reaching_maximum(self):
        levels = [
            [1, 1, 1],
            [1, 9, 1],
            [1, 1, 1]
        ]
        after_1_step = [
            [3, 3, 3],
            [3, 0, 3],
            [3, 3, 3]
        ]
        grid = EnergyGrid(levels)
        grid.simulate(1)
        self.assertEqual(grid.levels, after_1_step)

    def test_can_simulate_several_steps(self):
        levels = [
            [1, 1, 1, 1, 1],
            [1, 9, 9, 9, 1],
            [1, 9, 1, 9, 1],
            [1, 9, 9, 9, 1],
            [1, 1, 1, 1, 1],
        ]
        after_2_steps = [
            [4, 5, 6, 5, 4],
            [5, 1, 1, 1, 5],
            [6, 1, 1, 1, 6],
            [5, 1, 1, 1, 5],
            [4, 5, 6, 5, 4]
        ]
        grid = EnergyGrid(levels)
        grid.simulate(2)
        self.assertEqual(grid.levels, after_2_steps)

    def test_calculates_number_of_flashes(self):
        levels = [
            [1, 1, 1, 1, 1],
            [1, 9, 9, 9, 1],
            [1, 9, 1, 9, 1],
            [1, 9, 9, 9, 1],
            [1, 1, 1, 1, 1],
        ]
        self.assertEqual(EnergyGrid(levels).simulate(2), 9)

    def test_calculates_first_synchronizing_step(self):
        levels = [
            [1, 1, 1, 1, 1],
            [1, 9, 9, 9, 1],
            [1, 9, 1, 9, 1],
            [1, 9, 9, 9, 1],
            [1, 1, 1, 1, 1],
        ]
        self.assertEqual(EnergyGrid(levels).synchronizing_step(), 6)

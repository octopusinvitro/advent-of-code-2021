from .energy_grid import EnergyGrid


class Solution:
    def __init__(self, lines):
        self._levels = [list(map(int, line)) for line in lines]

    def part1(self):
        return EnergyGrid(self._levels).simulate(100)

    def part2(self):
        return EnergyGrid(self._levels).synchronizing_step()

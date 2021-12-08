from .crab_troop import CrabTroop


class Solution:
    def __init__(self, lines):
        self._initial_positions = [int(position) for position in lines[0].split(',')]

    def part1(self):
        return sum(CrabTroop(self._initial_positions).linear_optimal_fuel_costs())

    def part2(self):
        return sum(CrabTroop(self._initial_positions).quadratic_optimal_fuel_costs())

    def part2_differences(self):
        return CrabTroop(self._initial_positions).quadratic_optimal_fuel_cost()

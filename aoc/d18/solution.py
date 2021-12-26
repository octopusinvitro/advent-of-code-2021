from .magnitude import Magnitude
from .number_reducer import NumberReducer


class Solution:
    def __init__(self, lines):
        self._numbers = lines

    def part1(self):
        reduced = NumberReducer(self._numbers).reduce()

        return Magnitude(reduced).calculate()

    def part2(self):
        all_combinations = NumberReducer(self._numbers).reduce_all_combinations()

        return max(Magnitude(reduced).calculate() for reduced in all_combinations)

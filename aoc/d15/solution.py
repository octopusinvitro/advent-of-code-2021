from .path import Path
from .map import Map


class Solution:
    FULL_MAP_SIZE = 5
    MAXIMUM_VALUE = 9

    def __init__(self, lines):
        self._risk_levels = [list(map(int, line)) for line in lines]

        self._height = len(self._risk_levels)
        self._width = len(self._risk_levels[0])
        self._map = Map(self._risk_levels, self.FULL_MAP_SIZE, self.MAXIMUM_VALUE)

    def part1(self):
        path = Path(self._map.original)

        end_row = self._height - 1
        end_cell = self._width - 1

        return path.shortest((0, 0), (end_row, end_cell)).value_at_end()

    def part2(self):
        path = Path(self._map.full_map())

        end_row = self._height * self.FULL_MAP_SIZE - 1
        end_cell = self._width * self.FULL_MAP_SIZE - 1

        return path.shortest((0, 0), (end_row, end_cell)).value_at_end()

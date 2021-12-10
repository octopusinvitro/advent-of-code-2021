from .heightmap import Heightmap


class Solution:
    def __init__(self, lines):
        self._rows = [[int(number) for number in line] for line in lines]

    def part1(self):
        return sum(Heightmap(self._rows).risk_levels())

    def part2(self):
        largest = Heightmap(self._rows).basin_sizes()[:3]

        return largest[0] * largest[1] * largest[2]

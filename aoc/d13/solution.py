from .dots_grid import DotsGrid
from .manual import Manual


class Solution:
    def __init__(self, lines):
        self._manual = Manual(lines)

    def part1(self):
        dots = self._manual.dots()

        direction, coordinate = self._manual.instructions()[0]
        dots = direction.value.fold(dots, coordinate)

        return len(dots)

    def part2(self):
        dots = self._manual.dots()

        for direction, coordinate in self._manual.instructions():
            dots = direction.value.fold(dots, coordinate)

        for row in DotsGrid(dots).build():
            # print(' '.join(row[::-1]))
            pass

        return len(dots)

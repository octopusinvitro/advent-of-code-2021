from .line import Line


class Solution:
    def __init__(self, lines):
        self._lines = lines

    def part1(self):
        map = {}

        for line in self._lines:
            line = Line(line)

            if line.diagonal():
                continue

            for point in line.points():
                map[point] = map.get(point, 0) + 1

        return self._result(map)

    def part2(self):
        map = {}

        for line in self._lines:
            for point in Line(line).points():
                map[point] = map.get(point, 0) + 1

        return self._result(map)

    def _result(self, map):
        return sum(1 if count > 1 else 0 for count in map.values())

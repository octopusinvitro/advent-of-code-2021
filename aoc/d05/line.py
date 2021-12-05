import re


class Line:
    def __init__(self, line):
        self.start_x, self.start_y, self.end_x, self.end_y = self._parse(line)

    def vertical(self):
        return self.start_x == self.end_x

    def horizontal(self):
        return self.start_y == self.end_y

    def diagonal(self):
        return not self.vertical() and not self.horizontal()

    def points(self):
        if self.horizontal():
            return [self._key([x, self.start_y]) for x in self._range(self.start_x, self.end_x)]

        if self.vertical():
            return [self._key([self.start_x, y]) for y in self._range(self.start_y, self.end_y)]

        return [self._key([x, y]) for x, y in self._diagonal_range()]

    def _parse(self, line):
        regex = re.compile(r'^(\d+),(\d+) -> (\d+),(\d+)')

        return [int(coordinate) for coordinate in regex.match(line).groups()]

    def _range(self, start, end):
        step = 1 if end > start else -1

        return list(range(start, end + step, step))

    def _key(self, point):
        return ','.join(str(coordinate) for coordinate in point)

    def _diagonal_range(self):
        return zip(
            self._range(self.start_x, self.end_x),
            self._range(self.start_y, self.end_y)
        )

from .location import Location


class Heightmap:
    MAXIMUM_HEIGHT = 9

    def __init__(self, rows):
        self._heights = rows
        self._rows = range(len(rows))
        self._cells = range(len(rows[0]))
        self._location = Location(len(rows), len(rows[0]))

    def risk_levels(self):
        low_heights = []

        for row in self._rows:
            low_heights += self.low_heights_at(row)

        return [low_height + 1 for low_height in low_heights]

    def low_heights_at(self, row):
        return [self._height_at(row, cell) for cell in self._cells if self._is_low_point(row, cell)]

    def low_points_at(self, row):
        return [[row, cell] for cell in self._cells if self._is_low_point(row, cell)]

    def basin_sizes(self):
        sizes = []

        for row in self._rows:
            for _, cell in self.low_points_at(row):
                if self._was_visited(row, cell):
                    continue

                self._location.reset_visited()
                sizes.append(len(self.basin_at(row, cell)))

        return sorted(sizes)[::-1]

    def basin_at(self, row, cell):
        valid_neighbours = self._valid_neighbours(row, cell)
        self._location.visit([row, cell])

        for r, c in valid_neighbours:
            self.basin_at(r, c)

        return self._location.visited_locations

    def _is_low_point(self, row, cell):
        neighbours = self._location.neighbours4(row, cell)
        neighbour_heights = [self._height_at(r, c) for r, c in neighbours]

        return self._height_at(row, cell) < min(neighbour_heights)

    def _valid_neighbours(self, row, cell):
        neighbours = self._location.neighbours4(row, cell)

        return [[row, cell] for row, cell in neighbours if self._is_valid(row, cell)]

    def _is_valid(self, row, cell):
        return not self._is_excluded(row, cell) and not self._was_visited(row, cell)

    def _is_excluded(self, row, cell):
        return self._height_at(row, cell) == self.MAXIMUM_HEIGHT

    def _was_visited(self, row, cell):
        return self._location.was_visited([row, cell])

    def _height_at(self, row, cell):
        return self._heights[row][cell]

# flake8: noqa: E241


class Location:
    def __init__(self, row_count, cell_count):
        self._row_count = row_count;
        self._cell_count = cell_count;
        self.visited_locations = set()

    def neighbours(self, row, cell):
        left = self._previous(cell)
        top = self._previous(row)
        right = self._next(cell, self._cell_count)
        bottom = self._next(row, self._row_count)

        neighbours = [
                         [top,    cell],
            [row, left],                 [row, right],
                         [bottom, cell]
        ]

        return [neighbour for neighbour in neighbours if not self._outbound(neighbour)]

    def visit(self, location):
        self.visited_locations.add(self._visited_location(location))

    def was_visited(self, location):
        return self._visited_location(location) in self.visited_locations

    def reset_visited(self):
        self.visited_locations = set()

    def _previous(self, coordinate):
        previous = coordinate - 1

        return None if previous < 0 else previous

    def _next(self, coordinate, size):
        next = coordinate + 1

        return next if next < size else None

    def _outbound(self, location):
        return any(coordinate is None for coordinate in location)

    def _visited_location(self, location):
        return ','.join(map(str, location))

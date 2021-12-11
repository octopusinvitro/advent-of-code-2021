# flake8: noqa: E241


class Location:
    def __init__(self, row_count, cell_count):
        self._row_count = row_count;
        self._cell_count = cell_count;
        self.visited_locations = set()

    def neighbours4(self, row, cell):
        left, top, right, bottom = self._coordinates(row, cell)

        neighbours = [
                         [top,    cell],
            [row, left],                 [row, right],
                         [bottom, cell]
        ]

        return self._select_inbound(neighbours)

    def neighbours8(self, row, cell):
        left, top, right, bottom = self._coordinates(row, cell)

        neighbours = [
            [top,    left], [top,    cell], [top,    right],
            [row,    left],                 [row,    right],
            [bottom, left], [bottom, cell], [bottom, right]
        ]

        return self._select_inbound(neighbours)

    def visit(self, location):
        self.visited_locations.add(self._visited_location(location))

    def was_visited(self, location):
        return self._visited_location(location) in self.visited_locations

    def reset_visited(self):
        self.visited_locations = set()

    def _coordinates(self, row, cell):
        left = self._previous(cell)
        top = self._previous(row)
        right = self._next(cell, self._cell_count)
        bottom = self._next(row, self._row_count)

        return (left, top, right, bottom)

    def _previous(self, coordinate):
        previous = coordinate - 1

        return None if previous < 0 else previous

    def _next(self, coordinate, size):
        next = coordinate + 1

        return next if next < size else None

    def _select_inbound(self, neighbours):
        return [neighbour for neighbour in neighbours if self._is_inbound(neighbour)]

    def _is_inbound(self, location):
        return all(coordinate is not None for coordinate in location)

    def _visited_location(self, location):
        return ','.join(map(str, location))

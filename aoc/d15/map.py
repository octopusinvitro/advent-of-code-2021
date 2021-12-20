class Map:
    def __init__(self, original, factor, maximum_value):
        self._height = len(original)
        self._width = len(original[0])

        self._rows = self._height * factor
        self._cells = self._width * factor

        self.original = original
        self.map = self._copy_values(original)

        self._maximum_value = maximum_value

    def full_map(self):
        row_increment = -1

        for row in range(self._rows):
            if row % self._height == 0:
                row_increment += 1

            self._increment_cells(row, row_increment)

        return self.map

    def _increment_cells(self, row, row_increment):
        cell_increment = -1

        for cell in range(self._cells):
            if cell % self._width == 0:
                cell_increment += 1

            self._increment_cell(row, cell, row_increment, cell_increment)

    def _increment_cell(self, row, cell, row_increment, cell_increment):
        value = self.map[row][cell] + row_increment + cell_increment
        self.map[row][cell] = (value - 1) % self._maximum_value + 1

    def _copy_values(self, original):
        map = [[0] * self._cells for row in range(self._rows)]

        for row in range(self._rows):
            for cell in range(self._cells):
                small_row = (self._height + row) % self._height
                small_cell = (self._width + cell) % self._width

                map[row][cell] = original[small_row][small_cell]

        return map

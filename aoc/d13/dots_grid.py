class DotsGrid:
    TOKEN = '#'
    SPACE = ' '

    def __init__(self, dots):
        self._dots = dots

    def build(self):
        return [[self._token(row, cell) for cell in self._cells()] for row in self._rows()]

    def _token(self, row, cell):
        return self.TOKEN if (row, cell) in self._dots else self.SPACE

    def _rows(self):
        last = max(row for row, _ in self._dots)

        return range(last + 1)

    def _cells(self):
        last = max(cell for _, cell in self._dots)

        return range(last + 1)

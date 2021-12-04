class Board:
    MARK = 'X'

    def __init__(self, rows):
        self.rows = rows
        self.size = len(rows[0])

    def mark(self, number):
        rows = [[self.MARK if cell == number else cell for cell in row] for row in self.rows]
        return Board(rows)

    def win(self):
        return self._win_in_rows() or self._win_in_columns()

    def sum(self):
        return sum(int(cell) if cell != self.MARK else 0 for cell in sum(self.rows, []))

    def _win_in_rows(self):
        return any(self._win_in(row) for row in self.rows)

    def _win_in_columns(self):
        return any(self._win_in(self._column(index)) for index in range(self.size))

    def _win_in(self, line):
        return all(cell == self.MARK for cell in line)

    def _column(self, index):
        return [row[index] for row in self.rows]

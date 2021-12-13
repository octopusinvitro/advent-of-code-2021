class VerticalFolder():
    def fold(self, dots, coordinate):
        merged = set()

        for row, cell in dots:
            dot = (self._fold_row(row, coordinate), cell)
            merged.add(dot)

        return merged

    def _fold_row(self, row, coordinate):
        return row if row <= coordinate else 2 * coordinate - row

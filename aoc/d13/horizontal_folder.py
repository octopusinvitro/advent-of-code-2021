class HorizontalFolder():
    def fold(self, dots, coordinate):
        merged = set()

        for row, cell in dots:
            dot = (row, self._fold_cell(cell, coordinate))
            merged.add(dot)

        return merged

    def _fold_cell(self, cell, coordinate):
        return cell if cell == coordinate else abs(cell - coordinate) - 1

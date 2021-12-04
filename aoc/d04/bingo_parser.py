import re

from .board import Board


class BingoParser:
    def __init__(self, lines):
        self._lines = lines
        self.size = len(self._split(lines[2])) + 1

    def parse(self):
        return (self._numbers(), self._boards())

    def _numbers(self):
        return self._lines[0].split(',')

    def _boards(self):
        raw_boards = self._lines[1:]
        starting_indexes = range(0, len(raw_boards), self.size)
        splitted = [raw_boards[index + 1: index + self.size] for index in starting_indexes]

        return [Board([self._split(row) for row in rows]) for rows in splitted]

    def _split(self, row):
        return re.split(r' +', row.strip())

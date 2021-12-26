from re import search

from .bracket import Bracket


class Pair:
    COMMA = ','

    @classmethod
    def add(cls, left, right):
        return ''.join([Bracket.OPENING.value, left, cls.COMMA, right, Bracket.CLOSING.value])

    def __init__(self, pair):
        self._pair = pair

    def get(self, start=0, end=None):
        if end is None:
            end = len(self._pair)

        return self._pair[start: end]

    def append(self, character):
        self._pair += character

    def remove_first(self):
        first = self._pair[0]
        self._pair = self.get(1)

        return first

    def remove_range(self, start, end):
        left, right = self.get(start, end).split(self.COMMA)
        self._pair = self.get(end)

        return (left, right)

    def replace_once(self, subpair, replacement):
        self._pair = self._pair.replace(subpair, replacement, 1)

    def find(self, start=0):
        while start <= len(self._pair):
            match = search(r'^\d+,\d+', self.get(start))

            if match:
                return (start, start + match.end())

            start += 1

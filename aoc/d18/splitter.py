from math import ceil, floor
from re import findall

from .pair import Pair


class Splitter:
    SPLIT_LIMIT = 9

    def __init__(self, pair):
        self._pair = Pair(pair)

    def split(self):
        number = self._number()

        if number:
            left = str(floor(number / 2))
            right = str(ceil(number / 2))
            self._pair.replace_once(str(number), Pair.add(left, right))

            return self._pair.get()

    def _number(self):
        numbers = map(int, findall(r"\d+", self._pair.get()))

        return next(filter(lambda number: number > self.SPLIT_LIMIT, numbers), None)

from .exploder import Exploder
from .pair import Pair
from .splitter import Splitter


class NumberReducer:
    def __init__(self, numbers):
        self._numbers = numbers

    def reduce_all_combinations(self):
        reduced = self._all_combinations(self._numbers)
        reduced += self._all_combinations(self._numbers[::-1])

        return set(reduced)

    def reduce(self):
        left = self._numbers[0]

        for right in self._numbers[1:]:
            left = self.reduce_pair(left, right)

        return left

    def reduce_pair(self, left, right):
        previous = ''
        reduced = Pair.add(left, right)

        while(reduced != previous):
            previous = reduced
            reduced = self._calculate_reduced(previous)

        return reduced

    def _calculate_reduced(self, previous):
        return Exploder(previous).explode() or Splitter(previous).split() or previous

    def _all_combinations(self, pairs):
        reduced = []

        for left in pairs:
            start = pairs.index(left)

            for right in pairs[start:]:
                reduced.append(self.reduce_pair(left, right))

        return reduced

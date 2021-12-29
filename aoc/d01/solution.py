class Solution:
    def __init__(self, lines):
        self._depths = list(map(int, lines))

    def part1(self):
        scope = range(len(self._depths) - 1)

        return sum(1 for i in scope if self._comparison1(i))

    def part2(self):
        size = 3
        scope = range(len(self._depths) - size)

        return sum(1 for i in scope if self._comparison2(i, size))

    def _comparison1(self, i):
        return self._depths[i] < self._depths[i + 1]

    def _comparison2(self, i, size):
        current = self._depths[i: i + size]
        nextone = self._depths[i + 1: i + 1 + size]

        return sum(current) < sum(nextone)

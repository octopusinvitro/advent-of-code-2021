class Solution:
    def __init__(self, depths):
        self._depths = depths

    def part1(self):
        count = 0
        previous, *rest = self._depths

        for current in rest:
            if current > previous:
                count += 1
            previous = current

        return count

    def part2(self):
        size = 3

        count = 0
        _, *rest = self._depths
        previous = sum(self._depths[:size])

        for i in range(len(rest) - size + 1):
            current = sum(rest[i:i + size])
            if current > previous:
                count += 1
            previous = current

        return count

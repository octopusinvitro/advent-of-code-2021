from .direction import Direction
from ..result import Result


class Solution:
    DEPTH = 'depth'

    def __init__(self, commands=[]):
        self._commands = commands

    def part1(self):
        totals = self._initialize_totals()

        for command in self._commands:
            direction, units = command.split(' ')
            totals[direction] += int(units)

        return Result(totals[Direction.FORWARD.value], self._aim(totals))

    def part2(self):
        totals = self._initialize_totals()
        totals[self.DEPTH] = 0

        for command in self._commands:
            direction, units = command.split(' ')
            totals[direction] += int(units)

            if direction == Direction.FORWARD.value:
                totals[self.DEPTH] += self._aim(totals) * int(units)

        return Result(totals[Direction.FORWARD.value], totals[self.DEPTH])

    def _initialize_totals(self):
        return {direction.value: 0 for direction in Direction}

    def _aim(self, totals):
        return totals[Direction.DOWN.value] - totals[Direction.UP.value]

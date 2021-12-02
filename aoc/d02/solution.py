from .direction import Direction
from .position import Position


class Solution:
    DEPTH = 'depth'

    def __init__(self, commands=[]):
        self._commands = commands
        self._totals = {}

    def part1(self):
        self._totals = {}

        for command in self._commands:
            direction, units = command.split(' ')
            self._totals[direction] = self._add(direction, units)

        return Position(self._get(Direction.FORWARD.value), self._aim())

    def part2(self):
        self._totals = {}

        for command in self._commands:
            direction, units = command.split(' ')
            self._totals[direction] = self._add(direction, units)

            if direction == Direction.FORWARD.value:
                self._totals[self.DEPTH] = self._add(self.DEPTH, units, self._aim())

        return Position(self._get(Direction.FORWARD.value), self._get(self.DEPTH))

    def _add(self, direction, units, aim=1):
        return self._get(direction) + aim * int(units)

    def _aim(self):
        return self._get(Direction.DOWN.value) - self._get(Direction.UP.value)

    def _get(self, direction):
        return self._totals.get(direction, 0)

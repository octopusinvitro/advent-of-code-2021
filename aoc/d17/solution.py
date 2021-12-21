from .launcher import Launcher
from .target import Target


class Solution:
    def __init__(self, lines):
        self._target = Target(lines[0])

    def part1(self):
        return self._target.maximum_height()

    def part2(self):
        return len(Launcher(self._target).success_velocities())

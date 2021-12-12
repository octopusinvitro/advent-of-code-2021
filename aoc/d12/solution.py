from .path_finder import PathFinder


class Solution:
    def __init__(self, lines):
        self._lines = lines

    def part1(self):
        return len(PathFinder(self._lines).paths('start'))

    def part2(self):
        return len(PathFinder(self._lines).paths_revisiting_one('start'))

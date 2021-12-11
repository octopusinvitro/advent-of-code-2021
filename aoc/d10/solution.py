from .navigation_parser import NavigationParser
from .scoring import Scoring


class Solution:
    def __init__(self, lines):
        self._lines = lines
        self._illegal_characters, self._closing_sequences = NavigationParser().parse(self._lines)

    def part1(self):
        return sum(Scoring().corrupted_scores(self._illegal_characters))

    def part2(self):
        scores = Scoring().incomplete_scores(self._closing_sequences)

        return scores[int(len(scores) / 2)]

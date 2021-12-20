from .lanternfish_population import LanternfishPopulation


class Solution:
    def __init__(self, lines):
        self._initial_states = list(map(int, lines[0].split(',')))

    def part1(self):
        return self._count_for_days(80)

    def part2(self):
        return self._count_for_days(256)

    def _count_for_days(self, days):
        return sum(LanternfishPopulation().simulate(self._initial_states, days))

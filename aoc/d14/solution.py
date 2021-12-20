from .polymer import Polymer


class Solution:
    SPLIT = ' -> '

    def __init__(self, lines):
        template, rules = self._parse(lines)
        self._polimer = Polymer(template, rules)

    def part1(self):
        return self._result(10)

    def part2(self):
        return self._result(40)

    def _result(self, steps):
        counts = self._polimer.element_counts(steps).values()

        return max(counts) - min(counts)

    def _parse(self, lines):
        rules = {}

        for rule in lines[2:]:
            pair, insertion = rule.split(self.SPLIT)
            rules[pair] = insertion

        return (lines[0], rules)

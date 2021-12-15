from unittest import TestCase

from aoc.d14.polymer import Polymer


class TestPolymerFormula(TestCase):
    def setUp(self):
        template = 'NNCB'
        rules = {
            'CH': 'B',
            'HH': 'N',
            'CB': 'H',
            'NH': 'C',
            'HB': 'C',
            'HC': 'B',
            'HN': 'C',
            'NN': 'C',
            'BH': 'H',
            'NC': 'B',
            'NB': 'B',
            'BN': 'B',
            'BB': 'N',
            'BC': 'B',
            'CC': 'N',
            'CN': 'C'
        }
        self.polymer = Polymer(template, rules)

    def test_loads_template(self):
        self.assertEqual(self.polymer.element_counts(0), self.counts_for('NNCB'))

    def test_calculates_element_counts_after_one_step(self):
        self.assertEqual(self.polymer.element_counts(1), self.counts_for('NCNBCHB'))

    def test_calculates_element_counts_after_two_steps(self):
        self.assertEqual(self.polymer.element_counts(2), self.counts_for('NBCCNBBBCBHCB'))

    def test_calculates_element_counts_after_three_steps(self):
        formula = 'NBBBCNCCNBBNBNBBCHBHHBCHB'
        self.assertEqual(self.polymer.element_counts(3), self.counts_for(formula))

    def test_calculates_element_counts_after_four_steps(self):
        formula = 'NBBNBNBBCCNBCNCCNBBNBBNBBBNBBNBBCBHCBHHNHCBBCBHCB'
        self.assertEqual(self.polymer.element_counts(4), self.counts_for(formula))

    def counts_for(self, formula):
        counts = {}

        for element in formula:
            counts[element] = counts.get(element, 0) + 1

        return counts

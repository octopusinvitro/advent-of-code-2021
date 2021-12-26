from unittest import TestCase

from aoc.d18.pair import Pair


class TestPair(TestCase):
    def test_adds_two_pairs(self):
        sum = '[[1,2],[[3,4],5]]'
        self.assertEqual(Pair.add('[1,2]', '[[3,4],5]'), sum)

    def test_returns_full_pair(self):
        self.assertEqual(Pair('0123').get(), '0123')

    def test_returns_pair_from_limit(self):
        self.assertEqual(Pair('0123').get(2), '23')

    def test_returns_pair_until_limit(self):
        self.assertEqual(Pair('0123').get(0, 2), '01')

    def test_returns_pair_between_limits(self):
        self.assertEqual(Pair('0123').get(1, 3), '12')

    def test_returns_no_pair_if_no_limits(self):
        self.assertEqual(Pair('0123').get(0, 0), '')

    def test_gets_first_character_of_pair(self):
        self.assertEqual(Pair('0123').remove_first(), '0')

    def test_updates_pair_after_removing_first(self):
        pair = Pair('0123')
        pair.remove_first()
        self.assertEqual(pair.get(), '123')

    def test_gets_components_of_pair(self):
        self.assertEqual(Pair('[[1,2],[3,4]]').remove_range(8, 11), ('3', '4'))

    def test_updates_pair_after_removing_components(self):
        pair = Pair('[[1,2],[3,4]]')
        pair.remove_range(8, 11)
        self.assertEqual(pair.get(), ']]')

    def test_replaces_first_occurrence_of_number(self):
        pair = Pair('012312')
        pair.replace_once('12', '_replaced_')
        self.assertEqual(pair.get(), '0_replaced_312')

    def test_finds_pair_at_the_beggining(self):
        pair = Pair('1,2]')
        self.assertEqual(pair.find(0), (0, 3))

    def test_finds_pair_in_the_middle(self):
        pair = Pair('[[1,2],[[[2,3]],4],3]')
        self.assertEqual(pair.find(1), (2, 5))

# flake8: noqa: E501
from unittest import TestCase

from aoc.d18.exploder import Exploder


class TestExploder(TestCase):
    def test_explodes_pair_to_the_left(self):
        pair = '[[[[[9,8],1],2],3],4]'
        exploded = '[[[[0,9],2],3],4]'
        self.assertEqual(Exploder(pair).explode(), exploded)

    def test_explodes_pair_to_the_right_updating_first_left_number(self):
        pair = '[7,[6,[5,[4,[3,2]]]]]'
        exploded = '[7,[6,[5,[7,0]]]]'
        self.assertEqual(Exploder(pair).explode(), exploded)

    def test_explodes_pair_to_the_right_updating_first_right_number(self):
        pair = '[[6,[5,[4,[3,2]]]],1]'
        exploded = '[[6,[5,[7,0]]],3]'
        self.assertEqual(Exploder(pair).explode(), exploded)

    def test_explodes_leftmost_pair_to_the_right_updating_first_left_number_when_first(self):
        pair = '[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]'
        exploded = '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'
        self.assertEqual(Exploder(pair).explode(), exploded)

    def test_explodes_leftmost_pair_to_the_right_updating_first_left_number_when_last(self):
        pair = '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'
        exploded = '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'
        self.assertEqual(Exploder(pair).explode(), exploded)

    def test_explodes_when_pair_numbers_are_more_than_one_digit(self):
        pair = '[[[[4,0],[5,4]],[[7,0],[15,5]]],[10,[[0,[11,3]],[[6,3],[8,8]]]]]'
        exploded = '[[[[4,0],[5,4]],[[7,0],[15,5]]],[10,[[11,0],[[9,3],[8,8]]]]]'
        self.assertEqual(Exploder(pair).explode(), exploded)

    def test_explodes_when_numbers_around_pair_are_more_than_one_digit(self):
        pair = '[[[[12,12],[6,14]],[[15,0],[17,[8,1]]]],[2,9]]'
        exploded = '[[[[12,12],[6,14]],[[15,0],[25,0]]],[3,9]]'
        self.assertEqual(Exploder(pair).explode(), exploded)

    def test_explodes_the_correct_pair_when_repeated(self):
        pair = '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[[6,6],[0,5]],[[5,6],[6,[[7,7],8]]]]]'
        exploded = '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[[6,6],[0,5]],[[5,6],[13,[0,15]]]]]'
        self.assertEqual(Exploder(pair).explode(), exploded)

    def test_explodes_updating_only_first_occurence_of_regular_number(self):
        pair = '[[[[0,7],4],[7,[[8,4],9]]],[1,1]]'
        exploded = '[[[[0,7],4],[15,[0,13]]],[1,1]]'
        self.assertEqual(Exploder(pair).explode(), exploded)

    def test_appends_subsequent_opening_brackets_after_it_has_exploded(self):
        pair = '[[[[4,0],[5,0]],[[[4,5],[2,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]'
        exploded = '[[[[4,0],[5,4]],[[0,[7,6]],[9,5]]],[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]]'
        self.assertEqual(Exploder(pair).explode(), exploded)

    def test_explodes_when_bracket_count_greater_than_explode_bracket_count(self):
        pair = '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[7,[5,5]],[[0,[[5,6],3]],[[6,3],[8,8]]]]]'
        exploded = '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[7,[5,5]],[[5,[0,9]],[[6,3],[8,8]]]]]'
        self.assertEqual(Exploder(pair).explode(), exploded)

    def test_explodes_extra_example1(self):
        pair = '[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]'
        exploded = '[[[[0,7],4],[7,[[8,4],9]]],[1,1]]'
        self.assertEqual(Exploder(pair).explode(), exploded)

    def test_explodes_extra_example2(self):
        pair = '[[[[0,7],4],[[7,8],[0,[6,7]]]],[1,1]]'
        exploded = '[[[[0,7],4],[[7,8],[6,0]]],[8,1]]'
        self.assertEqual(Exploder(pair).explode(), exploded)

    def test_explodes_extra_example3(self):
        pair = '[[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]]'
        exploded = '[[[[0,[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]],[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]]'
        self.assertEqual(Exploder(pair).explode(), exploded)

    def test_explodes_extra_example4(self):
        pair = '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[7,[5,5]],[[5,7],[[0,[5,6]],[8,8]]]]]'
        exploded = '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[7,[5,5]],[[5,7],[[5,0],[14,8]]]]]'
        self.assertEqual(Exploder(pair).explode(), exploded)

    def test_ignores_not_explodable(self):
        pair = '[[[[9,8],[4,6]],[7,[9,1]]],[[[8,7],[4,7]],[[6,6],[8,1]]]]'
        self.assertIsNone(Exploder(pair).explode())

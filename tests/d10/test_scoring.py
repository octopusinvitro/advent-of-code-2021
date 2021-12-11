from unittest import TestCase

from aoc.d10.scoring import Scoring


class TestScoring(TestCase):
    def setUp(self):
        self.scoring = Scoring()

    def test_calculates_corrupted_score_of_an_illegal_character(self):
        illegal_characters = ['}']
        self.assertEqual(self.scoring.corrupted_scores(illegal_characters), [1197])

    def test_calculates_corrupted_scores_of_several_illegal_characters(self):
        illegal_characters = ['}', ')', ']', ')', '>']
        self.assertEqual(self.scoring.corrupted_scores(illegal_characters), [1197, 3, 57, 3, 25137])

    def test_calculates_incomplete_score_of_a_closing_sequence(self):
        closing_sequences = ['])}>']
        self.assertEqual(self.scoring.incomplete_scores(closing_sequences), [294])

    def test_calculates_sorted_incomplete_scores_of_several_closing_sequences(self):
        closing_sequences = ['}}]])})]', ')}>]})', '}}>}>))))', ']]}}]}]}>', '])}>']
        expected = [294, 5566, 288957, 995444, 1480781]
        self.assertEqual(self.scoring.incomplete_scores(closing_sequences), expected)

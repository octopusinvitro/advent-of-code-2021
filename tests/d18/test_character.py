from unittest import TestCase

from aoc.d18.bracket import Bracket
from aoc.d18.character import Character


class TestCharacter(TestCase):
    def test_detects_opening_bracket(self):
        self.assertTrue(Character(Bracket.OPENING.value).is_opening_bracket())

    def test_detects_not_opening_bracket(self):
        self.assertFalse(Character('not a opening_bracket').is_opening_bracket())

    def test_detects_closing_bracket(self):
        self.assertTrue(Character(Bracket.CLOSING.value).is_closing_bracket())

    def test_detects_not_closing_bracket(self):
        self.assertFalse(Character('not a closing_bracket').is_closing_bracket())

    def test_adds_number_to_number_character(self):
        self.assertEqual(Character('1').add('2'), '3')

    def test_returns_string_representation(self):
        self.assertEqual(Character('3').get(), '3')

from unittest import TestCase

from aoc.d10.navigation_parser import NavigationParser


class TestNavigationParser(TestCase):
    def setUp(self):
        self.parser = NavigationParser()

    def test_finds_no_illegal_character_for_incomplete_line(self):
        illegal_characters, _ = self.parser.parse(['[({(<(())[]>[[{[]{<()<>>'])
        self.assertEqual(len(illegal_characters), 0)

    def test_finds_first_illegal_character_for_corrupt_line(self):
        illegal_characters, _ = self.parser.parse(['[[<[([]))<([[{}[[()]]]'])
        self.assertEqual(illegal_characters, [')'])

    def test_finds_first_illegal_character_for_several_corrupt_lines(self):
        lines = [
            '[({(<(())[]>[[{[]{<()<>>',
            '[(()[<>])]({[<{<<[]>>(',
            '{([(<{}[<>[]}>{[]{[(<()>',
            '(((({<>}<{<{<>}{[]{[]{}',
            '[[<[([]))<([[{}[[()]]]',
            '[{[{({}]{}}([{[{{{}}([]',
            '{<[[]]>}<{[{[{[]{()[[[]',
            '[<(<(<(<{}))><([]([]()',
            '<{([([[(<>()){}]>(<<{{',
            '<{([{{}}[<[[[<>{}]]]>[]]'
        ]
        illegal_characters, _ = self.parser.parse(lines)
        self.assertEqual(illegal_characters, ['}', ')', ']', ')', '>'])

    def test_builds_no_closing_sequence_for_corrupt_line(self):
        _, closing_sequences = self.parser.parse(['[[<[([]))<([[{}[[()]]]'])
        self.assertEqual(len(closing_sequences), 0)

    def test_builds_closing_sequence_for_incomplete_line(self):
        _, closing_sequences = self.parser.parse(['[({(<(())[]>[[{[]{<()<>>'])
        self.assertEqual(closing_sequences, ['}}]])})]'])

    def test_builds_closing_sequence_for_several_incomplete_lines(self):
        lines = [
            '[({(<(())[]>[[{[]{<()<>>',
            '[(()[<>])]({[<{<<[]>>(',
            '{([(<{}[<>[]}>{[]{[(<()>',
            '(((({<>}<{<{<>}{[]{[]{}',
            '[[<[([]))<([[{}[[()]]]',
            '[{[{({}]{}}([{[{{{}}([]',
            '{<[[]]>}<{[{[{[]{()[[[]',
            '[<(<(<(<{}))><([]([]()',
            '<{([([[(<>()){}]>(<<{{',
            '<{([{{}}[<[[[<>{}]]]>[]]'
        ]
        _, closing_sequences = self.parser.parse(lines)
        expected = ['}}]])})]', ')}>]})', '}}>}>))))', ']]}}]}]}>', '])}>']
        self.assertEqual(closing_sequences, expected)

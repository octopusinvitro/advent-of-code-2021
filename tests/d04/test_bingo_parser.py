# flake8: noqa: E241
from unittest import TestCase

from aoc.d04.bingo_parser import BingoParser


class TestBingoParser(TestCase):
    def setUp(self):
        lines = [
            '7,4,9,5',
            '',
            '22 13',
            ' 8  2',
            '',
            ' 3 15',
            ' 9 18',
            '',
            '14 21',
            '10 16'
        ]
        self.parser = BingoParser(lines)

    def test_calculates_size_of_boards_plus_empty_line(self):
        self.assertEqual(self.parser.size, 3)

    def test_parses_numbers(self):
        numbers, _ = self.parser.parse()
        self.assertEqual(numbers, ['7', '4', '9', '5'])

    def test_parses_all_boards(self):
        _, boards = self.parser.parse()
        self.assertEqual(len(boards), 3)

    def test_parses_boards(self):
        rows = [
            ['22', '13'],
            [ '8',  '2']
        ]
        _, boards = self.parser.parse()
        self.assertEqual(boards[0].rows, rows)

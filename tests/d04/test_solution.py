from unittest import TestCase
from unittest.mock import Mock

from ..common import fixture_path

from aoc.file_parser import FileParser
from aoc.d04.bingo_parser import BingoParser
from aoc.d04.solution import Solution


class TestSolution(TestCase):
    def setUp(self):
        lines = [
            '8,2,14,21,3,9',
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
        parser = BingoParser(lines)
        self.simple_solution = Solution(parser.parse())

    def test_calculates_last_winner_score(self):
        self.assertEqual(self.simple_solution.part2(), (15 + 18) * 9)

    def test_part1_calculates_first_winner_score(self):
        self.assertEqual(self.solution().part1(), 4512)

    def test_part2_calculates_last_winner_score(self):
        self.assertEqual(self.solution().part2(), 1924)

    def solution(self):
        path = fixture_path('d04', 'valid_input')
        parser = BingoParser(FileParser(['', path], Mock()).lines())

        return Solution(parser.parse())

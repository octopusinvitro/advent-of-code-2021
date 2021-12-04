# flake8: noqa: E241
from unittest import TestCase

from aoc.d04.board import Board


class TestBoard(TestCase):
    def setUp(self):
        rows = [
            ['22', '13'],
            [ '8',  '7']
        ]
        self.board = Board(rows)

    def test_has_rows(self):
        rows = [
            ['22', '13'],
            [ '8',  '7']
        ]
        self.assertEqual(self.board.rows, rows)

    def test_has_a_size(self):
        self.assertEqual(self.board.size, 2)

    def test_returns_marked_board(self):
        rows = [
            ['22', '13'],
            [ '8', Board.MARK]
        ]
        self.assertEqual(self.board.mark('7').rows, rows)

    def test_detects_win_in_row(self):
        rows = [
            [Board.MARK, Board.MARK],
            [ '8',  '7']
        ]
        self.assertTrue(Board(rows).win())

    def test_detects_win_in_column(self):
        rows = [
            [Board.MARK, '13'],
            [Board.MARK,  '7']
        ]
        self.assertTrue(Board(rows).win())

    def test_sums_unmarked_numbers(self):
        rows = [
            ['22', Board.MARK],
            [ '8', Board.MARK]
        ]
        self.assertEqual(Board(rows).sum(), 22 + 8)

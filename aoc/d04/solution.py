from ..result import Result


class Solution:
    def __init__(self, parsed):
        self._numbers, self._boards = parsed

    def part1(self):
        boards = self._boards

        for number in self._numbers:
            boards = [board.mark(number) for board in boards]
            winners = list(filter(lambda board: board.win(), boards))

            if winners:
                return Result(winners[0].sum(), int(number))

    def part2(self):
        boards = self._boards
        old_winner_indexes = []

        for number in self._numbers:
            boards = [board.mark(number) for board in boards]
            winners = list(filter(lambda board: board.win(), boards))
            winner_indexes = set(boards.index(board) for board in winners)

            if len(winners) == len(boards):
                winner_index = list(winner_indexes - old_winner_indexes)[0]
                return Result(boards[winner_index].sum(), int(number))

            old_winner_indexes = winner_indexes

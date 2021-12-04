import sys

from aoc.file_parser import FileParser
from aoc.logger import Logger
from aoc.d04.bingo_parser import BingoParser
from aoc.d04.solution import Solution

logger = Logger()
lines = FileParser(sys.argv, logger).lines()
solution = Solution(BingoParser(lines).parse())

logger.print_solution_part1(solution.part1().product)
logger.print_solution_part2(solution.part2().product)

import sys

from aoc.file_parser import FileParser
from aoc.logger import Logger
from aoc.d03.solution import Solution

logger = Logger()
lines = FileParser(sys.argv, logger).lines()
solution = Solution(lines)

logger.print_solution_part1(solution.part1())
logger.print_solution_part2(solution.part2())

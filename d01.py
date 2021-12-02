import sys

from aoc.logger import Logger
from aoc.d01.depths import Depths
from aoc.d01.solution import Solution

logger = Logger()
depths = Depths(sys.argv, logger).get()
solution = Solution(depths)

logger.print_solution_part1(solution.part1())
logger.print_solution_part2(solution.part2())

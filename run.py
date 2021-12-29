import importlib
import sys

from aoc.file_parser import FileParser
from aoc.logger import Logger

day = sys.argv[1]
module = importlib.import_module('aoc.d' + day + '.solution')

logger = Logger()
lines = FileParser('data/d' + day + '_input', logger).lines()
solution = module.Solution(lines)

logger.print_solution_part1(solution.part1())
logger.print_solution_part2(solution.part2())

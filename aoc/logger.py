# flake8: noqa: E731
class Logger:
    def print_missing_input_error(self):
        print("\nError: provide path to input file: 'python dXX.py path/to/input'")

    def print_missing_file_error(self, error):
        print("\nError: can't find file or read data:", error)

    def print_invalid_number_error(self, error):
        print("\nError: The string can not be converted to number:", error)

    def print_solution_part1(self, solution):
        self._print_solution(1, solution)

    def print_solution_part2(self, solution):
        self._print_solution(2, solution)

    def _print_solution(self, number, solution):
        print("\nThe solution for part %d is" %(number), solution)

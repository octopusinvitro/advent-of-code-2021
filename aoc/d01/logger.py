# flake8: noqa: E731
class Logger:
    def print_missing_input_error(self):
        print("\nError: provide path to input file: 'python d01/d01.py path/to/input'")

    def print_missing_file_error(self, error):
        print("\nError: can't find file or read data:", error)

    def print_invalid_number_error(self, error):
        print("\nError: The depth not a number:", error)

    def print_solution_part1(self, count):
        print("\nThe number of depths larger than the previous in groups of two are", count)

    def print_solution_part2(self, count):
        print("\nThe number of depths larger than the previous in groups of three are", count)

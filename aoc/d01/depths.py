class Depths:
    def __init__(self, argv, logger):
        self._argv = argv
        self._logger = logger

    def get(self):
        if not self._argv[1:] or not self._argv[1]:
            self._logger.print_missing_input_error()
            return []

        try:
            input_file = open(self._argv[1], 'r')
        except (IOError) as error:
            self._logger.print_missing_file_error(error)
            return []

        try:
            depths = [int(line) for line in input_file]
        except (ValueError, TypeError) as error:
            input_file.close()
            self._logger.print_invalid_number_error(error)
            return []

        input_file.close()

        return depths

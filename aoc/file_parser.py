class FileParser:
    def __init__(self, argv, logger):
        self._argv = argv
        self._logger = logger

    def lines(self):
        if not self._argv[1:] or not self._argv[1]:
            self._logger.print_missing_input_error()
            return []

        try:
            input_file = open(self._argv[1], 'r')
        except (IOError) as error:
            self._logger.print_missing_file_error(error)
            return []

        lines = [line.strip() for line in input_file]
        input_file.close()

        return lines

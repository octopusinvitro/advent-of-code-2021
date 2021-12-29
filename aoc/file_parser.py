class FileParser:
    def __init__(self, path, logger):
        self._path = path
        self._logger = logger

    def lines(self):
        try:
            input_file = open(self._path, 'r')
        except (IOError) as error:
            self._logger.print_missing_file_error(error)
            return []

        lines = [line.strip() for line in input_file]
        input_file.close()

        return lines

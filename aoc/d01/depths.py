from ..file_parser import FileParser


class Depths:
    def __init__(self, argv, logger):
        self._argv = argv
        self._logger = logger

    def get(self):
        lines = FileParser(self._argv, self._logger).lines()

        try:
            depths = [int(line) for line in lines]
        except (ValueError, TypeError) as error:
            self._logger.print_invalid_number_error(error)
            return []

        return depths

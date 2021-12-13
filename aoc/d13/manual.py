from .direction import Direction


class Manual:
    LEFT = 'x'
    SEPARATOR = '='

    def __init__(self, lines):
        split = lines.index('')

        self._dots = lines[:split]
        self._instructions = lines[split + 1:]

    def dots(self):
        dots = set()

        for line in self._dots:
            cell, row = list(map(int, line.split(',')))
            dots.add((row, cell))

        return dots

    def instructions(self):
        instructions = []

        for line in self._instructions:
            instructions.append(self._instruction(line))

        return instructions

    def _instruction(self, line):
        direction, coordinate = line.split(self.SEPARATOR)
        direction = Direction.LEFT if direction[-1] is self.LEFT else Direction.UP

        return (direction, int(coordinate))

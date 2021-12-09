from .mapper import Mapper


class Decoder:
    def __init__(self, mapper):
        self._mapper = mapper

    def decode(self, entry):
        patterns, output = self._split(entry)
        mappings = self._mapper.mappings(patterns)
        digits = []

        for pattern in output:
            mapped_pattern = self._mapper.map(mappings, pattern)
            digits.append(Mapper.PATTERNS_TO_DIGITS[mapped_pattern])

        return int(''.join(digits))

    def _split(self, entry):
        return [patterns.split() for patterns in entry]

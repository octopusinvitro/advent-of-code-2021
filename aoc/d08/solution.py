from .decoder import Decoder
from .mapper import Mapper


class Solution:
    DELIMITER = ' | '

    def __init__(self, lines):
        self._entries = [line.split(self.DELIMITER) for line in lines]

    def part1(self):
        segment_counts = {}
        unique_lengths = [2, 3, 4, 7]

        for _, output in self._entries:
            for pattern in output.split():
                segment_counts[len(pattern)] = segment_counts.get(len(pattern), 0) + 1

        return sum(segment_counts[pattern_length] for pattern_length in unique_lengths)

    def part2(self):
        decoder = Decoder(Mapper())

        return sum(decoder.decode(entry) for entry in self._entries)

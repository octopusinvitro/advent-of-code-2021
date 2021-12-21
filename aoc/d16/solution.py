from .hexadecimal_parser import HexadecimalParser
from .message_decoder import MessageDecoder


class Solution:
    def __init__(self, lines):
        self._message = HexadecimalParser().to_binary(lines[0])
        _, self._packet = MessageDecoder().decode(self._message)

    def part1(self):
        return self._packet.version()

    def part2(self):
        return self._packet.data()

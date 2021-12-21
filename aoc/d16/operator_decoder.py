from ..d03.bit import Bit


class OperatorDecoder:
    TOTAL_LENGTH_SIZE = 15
    NUMBER_OF_SUBPACKETS_SIZE = 11

    def __init__(self, message):
        self._message = message

    def is_length_decoder(self):
        return self._message[0] == str(Bit.OFF.value)

    def decode_length(self):
        rest = self._message[1:]

        length = int(rest[:self.TOTAL_LENGTH_SIZE], 2)
        rest = rest[self.TOTAL_LENGTH_SIZE:]

        data = rest[:length]
        rest = rest[length:]

        return (rest, data)

    def decode_count(self):
        rest = self._message[1:]

        count = int(rest[:self.NUMBER_OF_SUBPACKETS_SIZE], 2)
        rest = rest[self.NUMBER_OF_SUBPACKETS_SIZE:]

        return (rest, count)

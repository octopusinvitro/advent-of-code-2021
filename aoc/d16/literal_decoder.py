from ..d03.bit import Bit


class LiteralDecoder:
    PREFIX_SIZE = 1
    GROUP_SIZE = 4

    def decode(self, message):
        rest = message
        data = ''

        prefix = str(Bit.ON.value)
        while(prefix == str(Bit.ON.value)):
            prefix = rest[0]
            rest = rest[self.PREFIX_SIZE:]

            data += rest[:self.GROUP_SIZE]
            rest = rest[self.GROUP_SIZE:]

        return (rest, int(data, 2))

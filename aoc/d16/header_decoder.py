class HeaderDecoder:
    DECODED_SIZE = 3

    def decode(self, message):
        rest, version = self._decode(message)
        rest, type = self._decode(rest)

        return (rest, version, type)

    def _decode(self, message):
        decoded = int(message[:self.DECODED_SIZE], 2)
        rest = message[self.DECODED_SIZE:]

        return (rest, decoded)

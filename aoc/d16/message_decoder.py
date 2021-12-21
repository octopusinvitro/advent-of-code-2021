from .header_decoder import HeaderDecoder
from .literal_decoder import LiteralDecoder
from .operator_decoder import OperatorDecoder
from .packet import Packet
from .packet_tree import PacketTree


class MessageDecoder:
    LITERAL_TYPE = 4

    def decode(self, message):
        rest, version, type = HeaderDecoder().decode(message)

        if type is self.LITERAL_TYPE:
            rest, data = LiteralDecoder().decode(rest)

            return (rest, Packet(version, type, data))

        rest, packets = self._decode_operator(OperatorDecoder(rest))

        return (rest, PacketTree(version, type, packets))

    def _decode_operator(self, decoder):
        if decoder.is_length_decoder():
            return self._decode_length(decoder)

        return self._decode_count(decoder)

    def _decode_length(self, decoder):
        packets = []
        rest, data = decoder.decode_length()

        while data:
            data, packet = self.decode(data)
            packets.append(packet)

        return (rest, packets)

    def _decode_count(self, decoder):
        packets = []
        rest, count = decoder.decode_count()

        for _ in range(count):
            rest, packet = self.decode(rest)
            packets.append(packet)

        return (rest, packets)

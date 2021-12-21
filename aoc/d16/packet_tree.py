from .data_calculator import DataCalculator


class PacketTree:
    def __init__(self, version, type, packets):
        self._version = version
        self._type = type
        self._packets = packets

    def version(self):
        packets_version_sum = sum(packet.version() for packet in self._packets)

        return self._version + packets_version_sum

    def data(self):
        packets_data = [packet.data() for packet in self._packets]
        calculator = DataCalculator(packets_data)

        return calculator.calculate(self._type)

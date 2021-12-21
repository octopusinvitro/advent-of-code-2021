class Packet:
    def __init__(self, version, type, data):
        self._version = version
        self._type = type
        self._data = data

    def version(self):
        return self._version

    def data(self):
        return self._data

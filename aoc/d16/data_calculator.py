from ..d03.bit import Bit


class DataCalculator:
    def __init__(self, data):
        self._data = data
        self._calculations = self._types_to_calculations()

    def calculate(self, type):
        calculation = self._calculations.get(type, self._identity)

        return calculation()

    def _sum(self):
        return sum(self._data)

    def _product(self):
        result = 1

        for data in self._data:
            result *= data

        return result

    def _minimum(self):
        return min(self._data)

    def _maximum(self):
        return max(self._data)

    def _identity(self):
        return self._data

    def _greater(self):
        first, second = self._data

        return Bit.ON.value if first > second else Bit.OFF.value

    def _less(self):
        return Bit.flip(self._greater())

    def _equal(self):
        first, second = self._data

        return Bit.ON.value if first == second else Bit.OFF.value

    def _types_to_calculations(self):
        return {
            0: self._sum,
            1: self._product,
            2: self._minimum,
            3: self._maximum,
            4: self._identity,
            5: self._greater,
            6: self._less,
            7: self._equal
        }

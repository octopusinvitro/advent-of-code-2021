import math

from .bit import Bit


class Solution:
    def __init__(self, report):
        self._report = report

    def part1(self):
        most_common, less_common = self._commons(self._report)

        return self._int(most_common) * self._int(less_common)

    def part2(self):
        most_common = self._select(self._report, 0)
        less_common = self._select(self._report, 1)

        return self._int(most_common) * self._int(less_common)

    def _commons(self, binary_numbers):
        halfsize = math.ceil(len(binary_numbers) / 2)
        most_common = less_common = ''

        for count in self._counts(binary_numbers):
            bit = Bit.ON.value if (count >= halfsize) else Bit.OFF.value
            most_common += str(bit)
            less_common += str(Bit.flip(bit))

        return (most_common, less_common)

    def _counts(self, binary_numbers):
        counts = [0] * len(binary_numbers[0])

        for number in binary_numbers:
            for position, digit in enumerate(number):
                counts[position] += int(digit)

        return counts

    def _select(self, binary_numbers, bit_criteria):
        position = 0

        while (len(binary_numbers) > 1):
            digit = self._commons(binary_numbers)[bit_criteria][position]
            binary_numbers = [number for number in binary_numbers if number[position] == digit]
            position += 1

        return binary_numbers[0]

    def _int(self, binary):
        return int(binary, 2)

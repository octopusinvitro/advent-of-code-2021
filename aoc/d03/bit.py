from enum import Enum


class Bit(Enum):
    ON = 1
    OFF = 0

    @classmethod
    def flip(cls, bit):
        return int(not bit)

from unittest import TestCase

from aoc.d16.hexadecimal_parser import HexadecimalParser


class TestHexadecimalParser(TestCase):
    def test_converts_hexadecimal_sequence_to_binary_sequence(self):
        expected = '0000000100100011010001010110011110001001101010111100110111101111'
        self.assertEqual(HexadecimalParser().to_binary('0123456789ABCDEF'), expected)

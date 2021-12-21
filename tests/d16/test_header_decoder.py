from unittest import TestCase

from aoc.d16.header_decoder import HeaderDecoder


class TestHeaderdecoder(TestCase):
    def setUp(self):
        self.decoder = HeaderDecoder()

    def test_calculates_rest(self):
        rest, _, _ = self.decoder.decode('11010000101')
        self.assertEqual(rest, '00101')

    def test_calculates_version(self):
        _, version, _ = self.decoder.decode('11010000101')
        self.assertEqual(version, 6)

    def test_calculates_type(self):
        _, _, type = self.decoder.decode('11010000101')
        self.assertEqual(type, 4)

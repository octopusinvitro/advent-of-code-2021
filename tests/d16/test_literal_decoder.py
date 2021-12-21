from unittest import TestCase

from aoc.d16.literal_decoder import LiteralDecoder


class TestLiteraldecoder(TestCase):
    def setUp(self):
        self.decoder = LiteralDecoder()

    def test_calculates_rest(self):
        rest, _ = self.decoder.decode('101111111000101')
        self.assertEqual(rest, '')

    def test_calculates_data(self):
        _, data = self.decoder.decode('101111111000101')
        self.assertEqual(data, 2021)

from unittest import TestCase

from aoc.d16.operator_decoder import OperatorDecoder


class TestOperatordecoder(TestCase):
    def setUp(self):
        self.length_message = '0000000000011011110100010100101001000100100'
        self.count_message = '10000000001101010000001100100000100011000001100000'

    def test_detects_length_decoder(self):
        self.assertTrue(OperatorDecoder(self.length_message).is_length_decoder())

    def test_detects_not_length_decoder(self):
        self.assertFalse(OperatorDecoder(self.count_message).is_length_decoder())

    def test_calculates_rest_when_length_decoder(self):
        rest, _ = OperatorDecoder(self.length_message).decode_length()
        self.assertEqual(rest, '')

    def test_calculates_data_when_length_decoder(self):
        _, data = OperatorDecoder(self.length_message).decode_length()
        self.assertEqual(data, '110100010100101001000100100')

    def test_calculates_rest_when_count_decoder(self):
        rest, _ = OperatorDecoder(self.count_message).decode_count()
        self.assertEqual(rest, '01010000001100100000100011000001100000')

    def test_calculates_count_when_count_decoder(self):
        _, count = OperatorDecoder(self.count_message).decode_count()
        self.assertEqual(count, 3)

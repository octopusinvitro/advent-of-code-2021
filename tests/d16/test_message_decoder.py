from unittest import TestCase

from aoc.d16.message_decoder import MessageDecoder


class TestMessageDecoder(TestCase):
    def setUp(self):
        self.decoder = MessageDecoder()

    def test_decodes_literal_value_version(self):
        message = '110100101111111000101000'
        _, packet = self.decoder.decode(message)
        self.assertEqual(packet.version(), 6)

    def test_decodes_literal_value_data(self):
        message = '110100101111111000101000'
        _, packet = self.decoder.decode(message)
        self.assertEqual(packet.data(), 2021)

    def test_decodes_operator_length_version(self):
        message = '00111000000000000110111101000101001010010001001000000000'
        _, packet = self.decoder.decode(message)
        self.assertEqual(packet.version(), 9)

    def test_decodes_operator_length_data(self):
        message = '00111000000000000110111101000101001010010001001000000000'
        _, packet = self.decoder.decode(message)
        self.assertEqual(packet.data(), 1)

    def test_decodes_operator_count_version(self):
        message = '11101110000000001101010000001100100000100011000001100000'
        _, packet = self.decoder.decode(message)
        self.assertEqual(packet.version(), 14)

    def test_decodes_operator_count_data(self):
        message = '11101110000000001101010000001100100000100011000001100000'
        _, packet = self.decoder.decode(message)
        self.assertEqual(packet.data(), 3)

    def test_decodes_mixed_example1_version(self):
        message = '100010100000000001001010100000000001101010000000000000101111010001111000'
        _, packet = self.decoder.decode(message)
        self.assertEqual(packet.version(), 16)

    def test_decodes_mixed_example1_data(self):
        message = '100010100000000001001010100000000001101010000000000000101111010001111000'
        _, packet = self.decoder.decode(message)
        self.assertEqual(packet.data(), 15)

    def test_decodes_mixed_example2_version(self):
        message = '011000100000000010000000000000000001011000010001010101100010110010001000000000'\
                  '10000100011000111000110100'
        _, packet = self.decoder.decode(message)
        self.assertEqual(packet.version(), 12)

    def test_decodes_mixed_example2_data(self):
        message = '011000100000000010000000000000000001011000010001010101100010110010001000000000'\
                  '10000100011000111000110100'
        _, packet = self.decoder.decode(message)
        self.assertEqual(packet.data(), 46)

    def test_decodes_mixed_example3_version(self):
        message = '110000000000000101010000000000000000000101100001000101011010001011100000100000'\
                  '0000101111000110000010001101000000'
        _, packet = self.decoder.decode(message)
        self.assertEqual(packet.version(), 23)

    def test_decodes_mixed_example3_data(self):
        message = '110000000000000101010000000000000000000101100001000101011010001011100000100000'\
                  '0000101111000110000010001101000000'
        _, packet = self.decoder.decode(message)
        self.assertEqual(packet.data(), 46)

    def test_decodes_mixed_example4_version(self):
        message = '101000000000000101101100100010000000000101100010000000010111110000110110100001'\
                  '101011000110001010001111010100011110000000'
        _, packet = self.decoder.decode(message)
        self.assertEqual(packet.version(), 31)

    def test_decodes_mixed_example4_data(self):
        message = '101000000000000101101100100010000000000101100010000000010111110000110110100001'\
                  '101011000110001010001111010100011110000000'
        _, packet = self.decoder.decode(message)
        self.assertEqual(packet.data(), 54)

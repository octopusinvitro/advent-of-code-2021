from unittest import TestCase

from aoc.d08.decoder import Decoder
from aoc.d08.mapper import Mapper


class TestDecoder(TestCase):
    def setUp(self):
        self.decoder = Decoder(Mapper())

    def test_decodes_entry_to_digits_example1(self):
        entry = [
            'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb',
            'fdgacbe cefdb cefbgd gcbe'
        ]
        self.assertEqual(self.decoder.decode((entry)), 8394)

    def test_decodes_entry_to_digits_example2(self):
        entry = [
            'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec',
            'fcgedb cgb dgebacf gc'
        ]
        self.assertEqual(self.decoder.decode((entry)), 9781)

    def test_decodes_entry_to_digits_example3(self):
        entry = [
            'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef',
            'cg cg fdcagb cbg'
        ]
        self.assertEqual(self.decoder.decode((entry)), 1197)

    def test_decodes_entry_to_digits_example4(self):
        entry = [
            'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega',
            'efabcd cedba gadfec cb'
        ]
        self.assertEqual(self.decoder.decode((entry)), 9361)

    def test_decodes_entry_to_digits_example5(self):
        entry = [
            'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga',
            'gecf egdcabf bgf bfgea'
        ]
        self.assertEqual(self.decoder.decode((entry)), 4873)

    def test_decodes_entry_to_digits_example6(self):
        entry = [
            'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf',
            'gebdcfa ecba ca fadegcb'
        ]
        self.assertEqual(self.decoder.decode((entry)), 8418)

    def test_decodes_entry_to_digits_example7(self):
        entry = [
            'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf',
            'cefg dcbef fcge gbcadfe'
        ]
        self.assertEqual(self.decoder.decode((entry)), 4548)

    def test_decodes_entry_to_digits_example8(self):
        entry = [
            'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd',
            'ed bcgafe cdgba cbgef'
        ]
        self.assertEqual(self.decoder.decode((entry)), 1625)

    def test_decodes_entry_to_digits_example9(self):
        entry = [
            'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg',
            'gbdfcae bgc cg cgb'
        ]
        self.assertEqual(self.decoder.decode((entry)), 8717)

    def test_decodes_entry_to_digits_example10(self):
        entry = [
            'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc',
            'fgae cfgab fg bagce'
        ]
        self.assertEqual(self.decoder.decode((entry)), 4315)

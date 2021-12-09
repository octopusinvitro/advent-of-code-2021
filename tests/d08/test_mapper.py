from unittest import TestCase

from aoc.d08.mapper import Mapper


class TestMapper(TestCase):
    def setUp(self):
        self.mapper = Mapper()

    def test_finds_the_right_mappings_example1(self):
        patterns = [
            'acedgfb', 'cdfbe', 'gcdfa', 'fbcad', 'dab',
            'cefabd', 'cdfgeb', 'eafb', 'cagedb', 'ab'
        ]
        mappings = {
            'a': 'c',
            'b': 'f',
            'c': 'g',
            'd': 'a',
            'e': 'b',
            'f': 'd',
            'g': 'e'
        }
        self.assertEqual(self.mapper.mappings(patterns), mappings)

    def test_finds_the_right_mappings_example2(self):
        patterns = [
            'be', 'cfbegad', 'cbdgef', 'fgaecd', 'cgeb',
            'fdcge', 'agebfd', 'fecdb', 'fabcd', 'edb'
        ]
        mappings = {
            'a': 'e',
            'b': 'c',
            'c': 'd',
            'd': 'a',
            'e': 'f',
            'f': 'g',
            'g': 'b'
        }
        self.assertEqual(self.mapper.mappings(patterns), mappings)

    def test_maps_a_scrambled_pattern_to_an_existing_pattern(self):
        mappings = {
            'a': 'c',
            'b': 'f',
            'c': 'g',
            'd': 'a',
            'e': 'b',
            'f': 'd',
            'g': 'e'
        }

        # example patterns
        self.assertEqual(self.mapper.map(mappings, 'acedgfb'), 'abcdefg')
        self.assertEqual(self.mapper.map(mappings, 'cdfbe'), 'abdfg')
        self.assertEqual(self.mapper.map(mappings, 'gcdfa'), 'acdeg')
        self.assertEqual(self.mapper.map(mappings, 'fbcad'), 'acdfg')
        self.assertEqual(self.mapper.map(mappings, 'dab'), 'acf')
        self.assertEqual(self.mapper.map(mappings, 'cefabd'), 'abcdfg')
        self.assertEqual(self.mapper.map(mappings, 'cdfgeb'), 'abdefg')
        self.assertEqual(self.mapper.map(mappings, 'eafb'), 'bcdf')
        self.assertEqual(self.mapper.map(mappings, 'cagedb'), 'abcefg')
        self.assertEqual(self.mapper.map(mappings, 'ab'), 'cf')

        # example output
        self.assertEqual(self.mapper.map(mappings, 'cdfeb'), 'abdfg')
        self.assertEqual(self.mapper.map(mappings, 'fcadb'), 'acdfg')
        self.assertEqual(self.mapper.map(mappings, 'cdfeb'), 'abdfg')
        self.assertEqual(self.mapper.map(mappings, 'cdbaf'), 'acdfg')

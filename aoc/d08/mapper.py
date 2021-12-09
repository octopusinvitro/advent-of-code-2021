from itertools import permutations


class Mapper:
    AVAILABLE_SEGMENTS = 'abcdefg'
    PATTERNS_TO_DIGITS = {
        'abcefg': '0',
        'cf': '1',
        'acdeg': '2',
        'acdfg': '3',
        'bcdf': '4',
        'abdfg': '5',
        'abdefg': '6',
        'acf': '7',
        'abcdefg': '8',
        'abcdfg': '9'
    }

    def mappings(self, patterns):
        for permutation in permutations(self.AVAILABLE_SEGMENTS):
            potential_mappings = dict(zip(permutation, self.AVAILABLE_SEGMENTS))
            mapped = [self.map(potential_mappings, pattern) for pattern in patterns]

            if sorted(mapped) == sorted(self.PATTERNS_TO_DIGITS.keys()):
                return potential_mappings

    def map(self, mappings, pattern):
        mapped_segments = map(mappings.get, pattern)

        return ''.join(sorted(mapped_segments))

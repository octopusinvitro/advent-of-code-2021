from .scoring import Scoring


class NavigationParser:
    OPENING_CHARACTERS = {'(', '[', '{', '<'}
    CLOSING_CHARACTERS = Scoring.CORRUPTED_SCORES.keys()

    CLOSING_TO_OPENING = dict(zip(
        sorted(list(CLOSING_CHARACTERS)),
        sorted(list(OPENING_CHARACTERS))
    ))
    OPENING_TO_CLOSING = {opening: closing for closing, opening in CLOSING_TO_OPENING.items()}

    def __init__(self):
        self._illegal_characters = []
        self._closing_sequences = []

    def parse(self, lines):
        for line in lines:
            opening_characters, illegal_characters = self._parse_line(line)
            self._illegal_characters += illegal_characters

            if opening_characters:
                self._closing_sequences.append(self._closing_sequence(opening_characters))

        return [self._illegal_characters, self._closing_sequences]

    def _parse_line(self, line):
        opening_characters = []
        illegal_characters = []

        for character in line:
            if self._is_opening_character(character):
                opening_characters.append(character)
                continue

            if self._is_illegal_character(opening_characters.pop(), character):
                illegal_characters.append(character)
                return [[], illegal_characters]

        return [opening_characters, illegal_characters]

    def _is_opening_character(self, character):
        return character in self.OPENING_CHARACTERS

    def _is_illegal_character(self, opening_character, closing_character):
        return opening_character != self.CLOSING_TO_OPENING[closing_character]

    def _closing_sequence(self, opening_characters):
        reversed = opening_characters[::-1]
        return ''.join(self.OPENING_TO_CLOSING[character] for character in reversed)

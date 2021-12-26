from .bracket import Bracket


class Character:
    def __init__(self, character):
        self._character = character

    def is_opening_bracket(self):
        return self._character is Bracket.OPENING.value

    def is_closing_bracket(self):
        return self._character is Bracket.CLOSING.value

    def add(self, number):
        return str(int(self._character) + int(number))

    def get(self):
        return self._character

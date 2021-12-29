from re import search

from .bracket import Bracket
from .character import Character
from .pair import Pair


class Exploder:
    EXPLODE_BRACKET_COUNT = 5
    PAIR_REPLACEMENT = '0'

    def __init__(self, pair):
        self._right = Pair(pair)
        self._left = Pair('')
        self._bracket_count = 0

    def explode(self):
        while(self._right.get()):
            character = Character(self._right.remove_first())
            self._update_bracket_count(character)

            if self._should_explode():
                return self._exploded()

            self._left.append(character.get())

    def _update_bracket_count(self, character):
        if character.is_opening_bracket():
            self._bracket_count += 1

        if character.is_closing_bracket():
            self._bracket_count -= 1

    def _should_explode(self):
        return self._bracket_count >= self.EXPLODE_BRACKET_COUNT

    def _exploded(self):
        left, right = self._find_explodable_pair()
        self._replace_first_number_to_the_right(right)
        self._replace_first_number_to_the_left(left)

        return self._left.get(0, - 1) + self.PAIR_REPLACEMENT + self._right.get(1)

    def _find_explodable_pair(self):
        start, end = self._right.find()
        self._left.append(Bracket.OPENING.value + self._right.get(0, start))

        return self._right.remove_range(start, end)

    def _replace_first_number_to_the_right(self, right):
        found = self._first_number(self._right.get())

        if found:
            digit = Character(found)
            self._right.replace_once(digit.get(), digit.add(right))

    def _replace_first_number_to_the_left(self, left):
        reversed_left = self._reverse(self._left.get())
        found = self._first_number(reversed_left)

        if found:
            digit = Character(self._reverse(found))
            reversed = Pair(reversed_left)
            reversed.replace_once(self._reverse(digit.get()), self._reverse(digit.add(left)))
            self._left = Pair(self._reverse(reversed.get()))

    def _first_number(self, pair):
        match = search(r'\d+', pair)

        if match:
            return match.group()

    def _reverse(self, text):
        return text[::-1]

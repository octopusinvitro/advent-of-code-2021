from .bracket import Bracket
from .character import Character
from .pair import Pair


class Magnitude:
    def __init__(self, pair):
        self._pair = Pair(pair)
        self._magnitude = Pair('')

    def calculate(self):
        while(self._pair.get()):
            character = Character(self._pair.remove_first())

            if character.is_closing_bracket():
                self._replace_last_pair_with_sum()
                continue

            self._magnitude.append(character.get())

        return int(self._magnitude.get())

    def _replace_last_pair_with_sum(self):
        reversed = Pair(self._reverse(self._magnitude.get()))
        reversed.replace_once(Bracket.OPENING.value, self._reverse(self._get_sum(reversed)))
        self._magnitude = Pair(self._reverse(reversed.get()))

    def _get_sum(self, reversed):
        start, end = reversed.find()
        right, left = reversed.remove_range(start, end)

        return self._sum(left, right)

    def _sum(self, left, right):
        left, right = map(int, map(self._reverse, (left, right)))

        return str(3 * left + 2 * right)

    def _reverse(self, text):
        return text[::-1]

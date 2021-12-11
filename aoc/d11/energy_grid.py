import copy

from ..d09.location import Location
from .level import Level


class EnergyGrid():
    def __init__(self, levels):
        levels = copy.deepcopy(levels)
        self.levels = levels

        self._range = range(len(levels))
        self._location = Location(len(levels), len(levels))
        self._flashes = 0

    def simulate(self, steps):
        step = 0

        while(step < steps):
            self._run_step()
            step += 1

        return self._flashes

    def synchronizing_step(self):
        step = 0

        while(not self._synchronized()):
            self._run_step()
            step += 1

        return step

    def _run_step(self):
        for row in self._range:
            for cell in self._range:
                self._update(row, cell)

        self._collect_flashes()

    def _update(self, row, cell):
        if self._not_highlighted(row, cell):
            self._increment(row, cell)

        if self._should_flash(row, cell):
            self._reset(row, cell)
            for r, c in self._location.neighbours8(row, cell):
                self._update(r, c)

    def _not_highlighted(self, row, cell):
        return not self._location.was_visited([row, cell])

    def _increment(self, row, cell):
        self.levels[row][cell] += 1

    def _should_flash(self, row, cell):
        return self.levels[row][cell] > Level.FLASH.value

    def _reset(self, row, cell):
        self.levels[row][cell] = Level.RESET.value
        self._location.visit([row, cell])

    def _collect_flashes(self):
        self._flashes += len(self._location.visited_locations)
        self._location.reset_visited()

    def _synchronized(self):
        return all(cell == Level.RESET.value for row in self.levels for cell in row)

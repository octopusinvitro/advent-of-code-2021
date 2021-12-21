from .probe import Probe


class Launcher:
    def __init__(self, target):
        self._target = target

    def shoot(self, velocity_x, velocity_y):
        probe = Probe(velocity_x, velocity_y)

        while(not self._target.was_hit(probe.position())):
            probe.move()

            if self._target.was_passed(probe.position()):
                return False

        return True

    def success_velocities(self):
        success_velocities = set()

        for velocity_x in self._x_window():
            for velocity_y in self._y_window():
                if self.shoot(velocity_x, velocity_y):
                    success_velocities.add((velocity_x, velocity_y))

        return success_velocities

    def _x_window(self):
        return range(self._target.max_x + 1)

    def _y_window(self):
        limit = abs(self._target.min_y)

        return range(-limit, limit + 1)

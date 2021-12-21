from .point import Point


class Probe:
    DRAG = 1
    GRAVITY = -1

    def __init__(self, initial_velocity_x, initial_velocity_y):
        self._position = Point(0, 0)
        self._velocity = Point(initial_velocity_x, initial_velocity_y)

    def move(self):
        self._position.x += self._velocity.x
        self._position.y += self._velocity.y
        self._velocity.x += self._drag()
        self._velocity.y += self.GRAVITY

    def position(self):
        return self._position

    def velocity(self):
        return self._velocity

    def _drag(self):
        if self._velocity.x == 0:
            return 0

        return self.DRAG if self._velocity.x < 0 else -self.DRAG

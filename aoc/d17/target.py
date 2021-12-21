import re


class Target:
    def __init__(self, target):
        self.min_x, self.max_x, self.min_y, self.max_y = self._parse(target)

    def maximum_height(self):
        return int((self.min_y + 1) * self.min_y / 2)

    def was_hit(self, point):
        return self._was_hit_in_x(point) and self._was_hit_in_y(point)

    def was_passed(self, point):
        return self._was_passed_in_x(point) or self._was_passed_in_y(point)

    def _was_hit_in_x(self, point):
        return self.min_x <= point.x <= self.max_x

    def _was_hit_in_y(self, point):
        return self.min_y <= point.y <= self.max_y

    def _was_passed_in_x(self, point):
        return self.max_x < point.x

    def _was_passed_in_y(self, point):
        return point.y < self.min_y

    def _parse(self, target):
        coordinates = re.findall(r"-?\d+", target)

        return map(int, coordinates)

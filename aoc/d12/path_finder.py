from copy import deepcopy
from itertools import chain

from .cave import Cave


class PathFinder():
    def __init__(self, lines):
        self.connections = self._build_connections(lines)
        self._paths = []

    def paths(self, origin, path=[], visited=set()):
        path_copy = list(self._add_cave(path, origin))

        if origin == Cave.LAST.value:
            return self._paths.append(path_copy)

        for destination in self.connections[origin]:
            visited_copy = set()
            if self._is_small_cave(origin):
                visited_copy = set(self._add_cave(visited, origin))

            if destination in visited:
                continue

            self.paths(destination, path_copy, visited_copy or visited)

        return self._paths

    def paths_revisiting_one(self, origin, visit_twice=False, path=[], visited=set()):
        path_copy = list(self._add_cave(path, origin))

        if origin == Cave.LAST.value:
            return self._paths.append(path_copy)

        for destination in self.connections[origin]:
            visited_copy = set()
            if self._is_small_cave(origin):
                visited_copy = set(self._add_cave(visited, origin))

            if destination == Cave.FIRST.value or (destination in visited and visit_twice):
                continue

            visit_twice_copy = not visit_twice if destination in visited else visit_twice
            self.paths_revisiting_one(
                destination, visit_twice_copy, path_copy, visited_copy or visited
            )

        return self._paths

    def _build_connections(self, lines):
        connections = {}

        for line in lines:
            origin, destination = line.split('-')
            connections[origin] = connections.get(origin, []) + [destination]
            connections[destination] = connections.get(destination, []) + [origin]

        return connections

    def _add_cave(self, iterable, value):
        iterable_copy = deepcopy(iterable)

        return chain(iterable_copy, [value])

    def _is_small_cave(self, cave):
        return cave == cave.lower()

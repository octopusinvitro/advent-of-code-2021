from copy import deepcopy
from itertools import chain

from .cave import Cave


class PathFinder():
    def __init__(self, lines):
        self.connections = self._build_connections(lines)
        self._paths = []

    def paths(self, origin, path=[], visited=set()):
        path_copy = self._path_copy(origin, path)
        if not path_copy:
            return

        self._visit_caves_once(origin, path_copy, visited)

        return self._paths

    def paths_revisiting_one(self, origin, path=[], visited=set(), visit_twice=False):
        path_copy = self._path_copy(origin, path)
        if not path_copy:
            return

        self._visit_caves_twice(origin, path_copy, visited, visit_twice)

        return self._paths

    def _path_copy(self, origin, path):
        path_copy = list(self._add_cave(path, origin))

        if origin == Cave.LAST.value:
            return self._paths.append(path_copy)

        return path_copy

    def _visit_caves_once(self, origin, path_copy, visited):
        for destination in self.connections[origin]:
            visited_copy = self._visited_copy(visited, origin)

            if destination in visited:
                continue

            self.paths(destination, path_copy, visited_copy)

    def _visit_caves_twice(self, origin, path_copy, visited, visit_twice):
        for destination in self.connections[origin]:
            visited_copy = self._visited_copy(visited, origin)

            if self._destination_should_be_ignored(destination, visited, visit_twice):
                continue

            visit_twice_copy = self._visit_twice_copy(destination, visited, visit_twice)

            self.paths_revisiting_one(destination, path_copy, visited_copy, visit_twice_copy)

    def _visited_copy(self, visited, origin):
        visited_copy = set()

        if self._is_small_cave(origin):
            visited_copy = set(self._add_cave(visited, origin))

        return visited_copy or visited

    def _visit_twice_copy(self, destination, visited, visit_twice):
        return not visit_twice if destination in visited else visit_twice

    def _destination_should_be_ignored(self, destination, visited, visit_twice):
        return destination == Cave.FIRST.value or (destination in visited and visit_twice)

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

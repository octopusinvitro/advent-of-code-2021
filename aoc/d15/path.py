from queue import PriorityQueue

from ..d09.location import Location
from .nodes import Nodes


class Path():
    def __init__(self, graph):
        self._graph = graph
        self._location = Location(len(graph), len(graph[0]))

    def shortest(self, start, end):
        self._nodes = Nodes(start, end)
        self._queue = PriorityQueue()
        self._queue.put(start, self._heuristic(start))

        self._dijkstra()

        return self._nodes

    def _dijkstra(self):
        while not self._queue.empty():
            previous = self._queue.get()
            if self._is_end(previous):
                break

            self._location.visit(previous)

            for current in self._unvisited_neighbours(previous):
                self._calculate_risk_values(current, previous)

    def _is_end(self, location):
        return location == self._nodes.end

    def _unvisited_neighbours(self, location):
        row, cell = location
        neighbours = self._location.neighbours4(row, cell)

        return [(r, c) for r, c in neighbours if self._not_visited(r, c)]

    def _not_visited(self, row, cell):
        return not self._location.was_visited([row, cell])

    def _calculate_risk_values(self, current, previous):
        total_risk = self._nodes.value_at(previous) + self._value_at(current)

        if total_risk < self._nodes.value_at(current):
            self._nodes.add(current, previous, total_risk)
            self._queue.put(current, total_risk + self._heuristic(current))

    def _value_at(self, location):
        row, cell = location

        return self._graph[row][cell]

    def _heuristic(self, here):
        return abs(self._nodes.end[0] - here[0]) + abs(self._nodes.end[1] - here[1])

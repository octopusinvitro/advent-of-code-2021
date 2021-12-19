from .node import Node


class Nodes:
    INITIAL_VALUE = float('inf')

    def __init__(self, start, end):
        self.start = start
        self.end = end
        self._nodes = self._initialize(start)

    def value_at(self, location):
        node = self._nodes.get(self._key(location), None)

        return node.value if node else self.INITIAL_VALUE

    def value_at_end(self):
        return self.value_at(self.end)

    def add(self, current, previous, value):
        self._nodes[self._key(current)] = Node(current, previous, value)

    def linked_nodes(self):
        linked = []
        previous = self.end

        while (True):
            node = self._nodes[self._key(previous)]
            linked.append(node.current)
            previous = node.previous

            if node.current == self.start:
                break

        return linked[::-1]

    def _initialize(self, start):
        key = self._key(start)
        node = Node(start, start, 0)

        return {key: node}

    def _key(self, location):
        return ','.join(map(str, location))

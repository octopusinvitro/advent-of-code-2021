from unittest import TestCase

from aoc.d15.nodes import Nodes


class TestNodes(TestCase):
    def setUp(self):
        self.nodes = Nodes((0, 0), (2, 2))

    def test_initializes_nodes_with_start_node(self):
        self.assertEqual(self.nodes.value_at((0, 0)), 0)

    def test_returns_initial_value_if_none_at_location(self):
        self.assertEqual(self.nodes.value_at((2, 2)), Nodes.INITIAL_VALUE)

    def test_sets_value_at_location(self):
        previous = (0, 1)
        self.nodes.add((1, 1), previous, 2)
        self.assertEqual(self.nodes.value_at((1, 1)), 2)

    def test_returns_linked_nodes(self):
        self.nodes.add((1, 0), (0, 0), 1)
        self.nodes.add((2, 0), (1, 0), 3)
        self.nodes.add((2, 1), (2, 0), 4)
        self.nodes.add((2, 2), (2, 1), 7)

        self.assertEqual(self.nodes.linked_nodes(), [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)])

    def test_returns_last_node(self):
        previous = (1, 2)
        self.nodes.add((2, 2), previous, 42)
        self.assertEqual(self.nodes.value_at_end(), 42)

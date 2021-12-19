from unittest import TestCase

from aoc.d15.path import Path


class TestPath(TestCase):
    def test_calculates_shortest_path_example3x3(self):
        graph = [
            [1, 1, 6],
            [1, 3, 8],
            [2, 1, 3]
        ]
        path = Path(graph)

        shortest_paths = path.shortest((0, 0), (2, 2)).linked_nodes()
        self.assertEqual(shortest_paths, [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2)])

    def test_calculates_shortest_value_example3x3(self):
        graph = [
            [1, 1, 6],
            [1, 3, 8],
            [2, 1, 3]
        ]
        path = Path(graph)
        self.assertEqual(path.shortest((0, 0), (2, 2)).value_at_end(), 7)

    def test_calculates_shortest_path_example4x4(self):
        graph = [
            [1, 1, 6, 3],
            [1, 3, 8, 1],
            [2, 1, 3, 6],
            [3, 6, 9, 4]
        ]
        path = Path(graph)

        shortest_paths = path.shortest((0, 0), (3, 3)).linked_nodes()
        expected = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (3, 3)]

        self.assertEqual(shortest_paths, expected)

    def test_calculates_shortest_value_example4x4(self):
        graph = [
            [1, 1, 6, 3],
            [1, 3, 8, 1],
            [2, 1, 3, 6],
            [3, 6, 9, 4]
        ]
        path = Path(graph)
        self.assertEqual(path.shortest((0, 0), (3, 3)).value_at_end(), 17)

    def test_calculates_shortest_path_example5x5(self):
        graph = [
            [1, 1, 6, 3, 7],
            [1, 3, 8, 1, 3],
            [2, 1, 3, 6, 5],
            [3, 6, 9, 4, 9],
            [7, 4, 6, 3, 4]
        ]
        path = Path(graph)

        shortest_paths = path.shortest((0, 0), (4, 4)).linked_nodes()
        expected = [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (3, 3), (4, 3), (4, 4)]

        self.assertEqual(shortest_paths, expected)

    def test_calculates_shortest_value_example5x5(self):
        graph = [
            [1, 1, 6, 3, 7],
            [1, 3, 8, 1, 3],
            [2, 1, 3, 6, 5],
            [3, 6, 9, 4, 9],
            [7, 4, 6, 3, 4]
        ]
        path = Path(graph)
        self.assertEqual(path.shortest((0, 0), (4, 4)).value_at_end(), 24)

    def test_calculates_shortest_path_example6x6(self):
        graph = [
            [1, 1, 6, 3, 7, 5],
            [1, 3, 8, 1, 3, 7],
            [2, 1, 3, 6, 5, 1],
            [3, 6, 9, 4, 9, 3],
            [7, 4, 6, 3, 4, 1],
            [1, 3, 1, 9, 1, 2]
        ]
        path = Path(graph)

        shortest_paths = path.shortest((0, 0), (5, 5)).linked_nodes()
        expected = [
            (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
            (2, 5), (3, 5), (4, 5), (5, 5)
        ]
        self.assertEqual(shortest_paths, expected)

    def test_calculates_shortest_value_example6x6(self):
        graph = [
            [1, 1, 6, 3, 7, 5],
            [1, 3, 8, 1, 3, 7],
            [2, 1, 3, 6, 5, 1],
            [3, 6, 9, 4, 9, 3],
            [7, 4, 6, 3, 4, 1],
            [1, 3, 1, 9, 1, 2]
        ]
        path = Path(graph)
        self.assertEqual(path.shortest((0, 0), (5, 5)).value_at_end(), 25)

    def test_calculates_shortest_path_example7x7(self):
        graph = [
            [1, 1, 6, 3, 7, 5, 1],
            [1, 3, 8, 1, 3, 7, 3],
            [2, 1, 3, 6, 5, 1, 1],
            [3, 6, 9, 4, 9, 3, 1],
            [7, 4, 6, 3, 4, 1, 7],
            [1, 3, 1, 9, 1, 2, 8],
            [1, 3, 5, 9, 9, 1, 2]
        ]
        path = Path(graph)

        shortest_paths = path.shortest((0, 0), (6, 6)).linked_nodes()
        expected = [
            (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
            (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (6, 6)
        ]
        self.assertEqual(shortest_paths, expected)

    def test_calculates_shortest_value_example7x7(self):
        graph = [
            [1, 1, 6, 3, 7, 5, 1],
            [1, 3, 8, 1, 3, 7, 3],
            [2, 1, 3, 6, 5, 1, 1],
            [3, 6, 9, 4, 9, 3, 1],
            [7, 4, 6, 3, 4, 1, 7],
            [1, 3, 1, 9, 1, 2, 8],
            [1, 3, 5, 9, 9, 1, 2]
        ]
        path = Path(graph)
        self.assertEqual(path.shortest((0, 0), (6, 6)).value_at_end(), 28)

    def test_calculates_shortest_path_example8x8(self):
        graph = [
            [1, 1, 6, 3, 7, 5, 1, 7],
            [1, 3, 8, 1, 3, 7, 3, 6],
            [2, 1, 3, 6, 5, 1, 1, 3],
            [3, 6, 9, 4, 9, 3, 1, 5],
            [7, 4, 6, 3, 4, 1, 7, 1],
            [1, 3, 1, 9, 1, 2, 8, 1],
            [1, 3, 5, 9, 9, 1, 2, 4],
            [3, 1, 2, 5, 4, 2, 1, 6]
        ]
        path = Path(graph)

        shortest_paths = path.shortest((0, 0), (7, 7)).linked_nodes()
        expected = [
            (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
            (2, 5), (3, 5), (4, 5), (5, 5), (6, 5), (6, 6), (7, 6),
            (7, 7)
        ]
        self.assertEqual(shortest_paths, expected)

    def test_calculates_shortest_value_example8x8(self):
        graph = [
            [1, 1, 6, 3, 7, 5, 1, 7],
            [1, 3, 8, 1, 3, 7, 3, 6],
            [2, 1, 3, 6, 5, 1, 1, 3],
            [3, 6, 9, 4, 9, 3, 1, 5],
            [7, 4, 6, 3, 4, 1, 7, 1],
            [1, 3, 1, 9, 1, 2, 8, 1],
            [1, 3, 5, 9, 9, 1, 2, 4],
            [3, 1, 2, 5, 4, 2, 1, 6]
        ]
        path = Path(graph)
        self.assertEqual(path.shortest((0, 0), (7, 7)).value_at_end(), 35)

    def test_calculates_shortest_path_example9x9(self):
        graph = [
            [1, 1, 6, 3, 7, 5, 1, 7, 4],
            [1, 3, 8, 1, 3, 7, 3, 6, 7],
            [2, 1, 3, 6, 5, 1, 1, 3, 2],
            [3, 6, 9, 4, 9, 3, 1, 5, 6],
            [7, 4, 6, 3, 4, 1, 7, 1, 1],
            [1, 3, 1, 9, 1, 2, 8, 1, 3],
            [1, 3, 5, 9, 9, 1, 2, 4, 2],
            [3, 1, 2, 5, 4, 2, 1, 6, 3],
            [1, 2, 9, 3, 1, 3, 8, 5, 2]
        ]
        path = Path(graph)

        shortest_paths = path.shortest((0, 0), (8, 8)).linked_nodes()
        expected = [
            (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
            (2, 5), (2, 6), (3, 6), (3, 7), (4, 7), (4, 8), (5, 8),
            (6, 8), (7, 8), (8, 8)
        ]
        self.assertEqual(shortest_paths, expected)

    def test_calculates_shortest_value_example9x9(self):
        graph = [
            [1, 1, 6, 3, 7, 5, 1, 7, 4],
            [1, 3, 8, 1, 3, 7, 3, 6, 7],
            [2, 1, 3, 6, 5, 1, 1, 3, 2],
            [3, 6, 9, 4, 9, 3, 1, 5, 6],
            [7, 4, 6, 3, 4, 1, 7, 1, 1],
            [1, 3, 1, 9, 1, 2, 8, 1, 3],
            [1, 3, 5, 9, 9, 1, 2, 4, 2],
            [3, 1, 2, 5, 4, 2, 1, 6, 3],
            [1, 2, 9, 3, 1, 3, 8, 5, 2]
        ]
        path = Path(graph)
        self.assertEqual(path.shortest((0, 0), (8, 8)).value_at_end(), 38)

    def test_calculates_shortest_path_example10x10(self):
        graph = [
            [1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
            [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
            [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
            [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
            [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
            [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
            [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
            [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
            [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
            [2, 3, 1, 1, 9, 4, 4, 5, 8, 1]
        ]
        path = Path(graph)

        shortest_paths = path.shortest((0, 0), (9, 9)).linked_nodes()
        expected = [
            (0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (2, 3), (2, 4),
            (2, 5), (2, 6), (3, 6), (3, 7), (4, 7), (4, 8), (5, 8),
            (6, 8), (7, 8), (8, 8), (8, 9), (9, 9)
        ]
        self.assertEqual(shortest_paths, expected)

    def test_calculates_shortest_value_example10x10(self):
        graph = [
            [1, 1, 6, 3, 7, 5, 1, 7, 4, 2],
            [1, 3, 8, 1, 3, 7, 3, 6, 7, 2],
            [2, 1, 3, 6, 5, 1, 1, 3, 2, 8],
            [3, 6, 9, 4, 9, 3, 1, 5, 6, 9],
            [7, 4, 6, 3, 4, 1, 7, 1, 1, 1],
            [1, 3, 1, 9, 1, 2, 8, 1, 3, 7],
            [1, 3, 5, 9, 9, 1, 2, 4, 2, 1],
            [3, 1, 2, 5, 4, 2, 1, 6, 3, 9],
            [1, 2, 9, 3, 1, 3, 8, 5, 2, 1],
            [2, 3, 1, 1, 9, 4, 4, 5, 8, 1]
        ]
        path = Path(graph)
        self.assertEqual(path.shortest((0, 0), (9, 9)).value_at_end(), 40)

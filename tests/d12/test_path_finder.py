from unittest import TestCase

from aoc.d12.path_finder import PathFinder


class TestPathFinder(TestCase):
    def test_calculates_cave_connections_from_input(self):
        connections = [
            'start-A',
            'start-b',
            'A-c',
            'A-b',
            'b-d',
            'A-end',
            'b-end'
        ]
        expected = {
            'start': ['A', 'b'],
            'A': ['start', 'c', 'b', 'end'],
            'b': ['start', 'A', 'd', 'end'],
            'c': ['A'],
            'd': ['b'],
            'end': ['A', 'b']
        }
        self.assertEqual(PathFinder(connections).connections, expected)

    def test_calculates_all_paths_visiting_small_caves_once_example1(self):
        connections = [
            'start-A',
            'start-b',
            'A-c',
            'A-b',
            'b-d',
            'A-end',
            'b-end'
        ]
        expected = [
            ['start', 'A', 'c', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'end'],
            ['start', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'b', 'end'],
            ['start', 'A', 'end'],
            ['start', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'b', 'A', 'end'],
            ['start', 'b', 'end']
        ]
        self.assertEqual(PathFinder(connections).paths('start'), expected)

    def test_calculates_all_paths_visiting_small_caves_once_example2(self):
        connections = [
            'dc-end',
            'HN-start',
            'start-kj',
            'dc-start',
            'dc-HN',
            'LN-dc',
            'HN-end',
            'kj-sa',
            'kj-HN',
            'kj-dc'
        ]
        expected = [
            ['start', 'HN', 'dc', 'end'],
            ['start', 'HN', 'dc', 'HN', 'end'],
            ['start', 'HN', 'dc', 'HN', 'kj', 'HN', 'end'],
            ['start', 'HN', 'dc', 'kj', 'HN', 'end'],
            ['start', 'HN', 'end'],
            ['start', 'HN', 'kj', 'HN', 'dc', 'end'],
            ['start', 'HN', 'kj', 'HN', 'dc', 'HN', 'end'],
            ['start', 'HN', 'kj', 'HN', 'end'],
            ['start', 'HN', 'kj', 'dc', 'end'],
            ['start', 'HN', 'kj', 'dc', 'HN', 'end'],
            ['start', 'kj', 'HN', 'dc', 'end'],
            ['start', 'kj', 'HN', 'dc', 'HN', 'end'],
            ['start', 'kj', 'HN', 'end'],
            ['start', 'kj', 'dc', 'end'],
            ['start', 'kj', 'dc', 'HN', 'end'],
            ['start', 'dc', 'end'],
            ['start', 'dc', 'HN', 'end'],
            ['start', 'dc', 'HN', 'kj', 'HN', 'end'],
            ['start', 'dc', 'kj', 'HN', 'end']
        ]
        self.assertEqual(PathFinder(connections).paths('start'), expected)

    def test_calculates_all_paths_visiting_small_caves_twice(self):
        connections = [
            'start-A',
            'start-b',
            'A-c',
            'A-b',
            'b-d',
            'A-end',
            'b-end'
        ]
        expected = [
            ['start', 'A', 'c', 'A', 'c', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'c', 'A', 'b', 'end'],
            ['start', 'A', 'c', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'A', 'b', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'd', 'b', 'A', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'd', 'b', 'end'],
            ['start', 'A', 'c', 'A', 'b', 'end'],
            ['start', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'c', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'c', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'c', 'A', 'b', 'end'],
            ['start', 'A', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'b', 'A', 'b', 'end'],
            ['start', 'A', 'b', 'A', 'end'],
            ['start', 'A', 'b', 'd', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'A', 'b', 'd', 'b', 'A', 'end'],
            ['start', 'A', 'b', 'd', 'b', 'end'],
            ['start', 'A', 'b', 'end'],
            ['start', 'A', 'end'],
            ['start', 'b', 'A', 'c', 'A', 'c', 'A', 'end'],
            ['start', 'b', 'A', 'c', 'A', 'b', 'A', 'end'],
            ['start', 'b', 'A', 'c', 'A', 'b', 'end'],
            ['start', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'b', 'A', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'b', 'A', 'b', 'A', 'end'],
            ['start', 'b', 'A', 'b', 'end'],
            ['start', 'b', 'A', 'end'],
            ['start', 'b', 'd', 'b', 'A', 'c', 'A', 'end'],
            ['start', 'b', 'd', 'b', 'A', 'end'],
            ['start', 'b', 'd', 'b', 'end'],
            ['start', 'b', 'end']
        ]
        self.assertEqual(PathFinder(connections).paths_revisiting_one('start'), expected)

    def test_calculates_all_paths_visiting_small_caves_twice_example2(self):
        connections = [
            'dc-end',
            'HN-start',
            'start-kj',
            'dc-start',
            'dc-HN',
            'LN-dc',
            'HN-end',
            'kj-sa',
            'kj-HN',
            'kj-dc'
        ]
        paths = PathFinder(connections).paths_revisiting_one('start')
        self.assertEqual(len(paths), 103)

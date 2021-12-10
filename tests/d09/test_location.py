# flake8: noqa: E241
from unittest import TestCase

from aoc.d09.location import Location


class TestLocation(TestCase):
    def setUp(self):
        self.location = Location(3, 3)

    def test_calculates_1_cell_distance_neighbours_around(self):
        neighbours = [
                   [0,1],
            [1,0],        [1,2],
                   [2,1]
        ]
        self.assertEqual(self.location.neighbours(1, 1), neighbours)

    def test_takes_care_of_the_left_border(self):
        neighbours = [
            [0,0],
                   [1,1],
            [2,0]
        ];

        self.assertEqual(self.location.neighbours(1, 0), neighbours)

    def test_takes_care_of_the_right_border(self):
        neighbours = [
                   [0,2],
            [1,1],
                   [2,2]
        ];

        self.assertEqual(self.location.neighbours(1, 2), neighbours)

    def test_takes_care_of_the_top_border(self):
        neighbours = [
            [0,0],        [0,2],
                   [1,1]
        ];

        self.assertEqual(self.location.neighbours(0, 1), neighbours)

    def test_takes_care_of_the_bottom_border(self):
        neighbours = [
                   [1,1],
            [2,0],        [2,2],
        ];

        self.assertEqual(self.location.neighbours(2, 1), neighbours)

    def test_adds_location_to_visited(self):
        self.location.visit([0, 0])
        self.assertEqual(self.location.visited_locations, {'0,0'})

    def test_appends_visited_locations_to_existing_ones_avoiding_duplicates(self):
        self.location.visit([1, 0])
        self.location.visit([1, 0])
        self.assertEqual(self.location.visited_locations, {'1,0'})

    def test_detects_visited_basin_location(self):
        self.location.visit([1, 0])
        self.location.visit([2, 2])
        self.assertTrue(self.location.was_visited([2, 2]))

    def test_detects_unvisited_basin_location(self):
        self.assertFalse(self.location.was_visited([2, 2]))

    def test_resets_visited_locations(self):
        self.location.visit([0, 0])
        self.location.reset_visited()
        self.assertEqual(len(self.location.visited_locations), 0)

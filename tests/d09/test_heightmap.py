from unittest import TestCase

from aoc.d09.heightmap import Heightmap


class TestHeightmap(TestCase):
    def setUp(self):
        rows = [
            [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
            [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
            [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
            [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
            [9, 8, 9, 9, 9, 6, 5, 6, 7, 8]
        ]
        self.heightmap = Heightmap(rows)

    def test_calculates_the_risk_levels(self):
        self.assertEqual(self.heightmap.risk_levels(), [2, 1, 6, 6])

    def test_calculates_the_heights_of_the_low_pointss_at_a_row(self):
        self.assertEqual(self.heightmap.low_heights_at(0), [1, 0])
        self.assertEqual(self.heightmap.low_heights_at(1), [])
        self.assertEqual(self.heightmap.low_heights_at(2), [5])
        self.assertEqual(self.heightmap.low_heights_at(3), [])
        self.assertEqual(self.heightmap.low_heights_at(4), [5])

    def test_calculates_the_low_points_at_a_row(self):
        self.assertEqual(self.heightmap.low_points_at(0), [[0, 1], [0, 9]])
        self.assertEqual(self.heightmap.low_points_at(1), [])
        self.assertEqual(self.heightmap.low_points_at(2), [[2, 2]])
        self.assertEqual(self.heightmap.low_points_at(3), [])
        self.assertEqual(self.heightmap.low_points_at(4), [[4, 6]])

    def test_calculates_reverse_sorted_basin_sizes_for_all_low_points(self):
        self.assertEqual(self.heightmap.basin_sizes(), [14, 9, 9, 3])

    def test_calculates_basin_at_first_low_point(self):
        self.assertEqual(
            sorted(list(self.heightmap.basin_at(0, 0))),
            sorted(['0,0', '0,1', '1,0'])
        )

    def test_calculates_basin_at_second_low_point(self):
        self.assertEqual(
            sorted(list(self.heightmap.basin_at(0, 9))),
            sorted(['0,5', '0,6', '0,7', '0,8', '0,9', '1,6', '1,8', '1,9', '2,9'])
        )

    def test_calculates_basin_at_third_low_point(self):
        self.assertEqual(
            sorted(list(self.heightmap.basin_at(2, 2))),
            sorted([
                '1,2', '1,3', '1,4', '2,1', '2,2', '2,3', '2,4', '2,5', '3,0', '3,1',
                '3,2', '3,3', '3,4', '4,1'
            ])
        )

    def test_calculates_basin_at_fourth_low_point(self):
        self.assertEqual(
            sorted(list(self.heightmap.basin_at(4, 6))),
            sorted(['2,7', '3,6', '3,7', '3,8', '4,5', '4,6', '4,7', '4,8', '4,9'])
        )

from unittest import TestCase

from aoc.d16.solution import Solution


class TestSolution(TestCase):
    def test_part1_example1(self):
        self.assertEqual(Solution(['8A004A801A8002F478']).part1(), 16)

    def test_part1_example2(self):
        self.assertEqual(Solution(['620080001611562C8802118E34']).part1(), 12)

    def test_part1_example3(self):
        self.assertEqual(Solution(['C0015000016115A2E0802F182340']).part1(), 23)

    def test_part1_example4(self):
        self.assertEqual(Solution(['A0016C880162017C3686B18A3D4780']).part1(), 31)

    def test_part2_example1(self):
        self.assertEqual(Solution(['C200B40A82']).part2(), 3)

    def test_part2_example2(self):
        self.assertEqual(Solution(['04005AC33890']).part2(), 54)

    def test_part2_example3(self):
        self.assertEqual(Solution(['880086C3E88112']).part2(), 7)

    def test_part2_example4(self):
        self.assertEqual(Solution(['CE00C43D881120']).part2(), 9)

    def test_part2_example5(self):
        self.assertEqual(Solution(['D8005AC2A8F0']).part2(), 1)

    def test_part2_example6(self):
        self.assertEqual(Solution(['F600BC2D8F']).part2(), 0)

    def test_part2_example7(self):
        self.assertEqual(Solution(['9C005AC2F8F0']).part2(), 0)

    def test_part2_example8(self):
        self.assertEqual(Solution(['9C0141080250320F1802104A08']).part2(), 1)

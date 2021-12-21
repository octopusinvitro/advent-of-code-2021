from unittest import TestCase

from aoc.d16.packet import Packet
from aoc.d16.packet_tree import PacketTree
from tests.d16.type import Type


class TestPacketTree(TestCase):
    def test_returns_sum_of_leaf_versions_and_its_own(self):
        data = [Packet(1, 4, 3), Packet(3, 4, 5)]
        self.assertEqual(PacketTree(6, 7, data).version(), 10)

    def test_returns_leaf_data_for_type_sum(self):
        data = [Packet(6, 4, 1), Packet(2, 4, 2)]
        self.assertEqual(PacketTree(6, Type.SUM, data).data(), 3)

    def test_returns_leaf_data_for_type_product(self):
        data = [Packet(5, 4, 6), Packet(3, 4, 9)]
        self.assertEqual(PacketTree(0, Type.PRODUCT, data).data(), 54)

    def test_returns_leaf_data_for_type_minimum(self):
        data = [Packet(5, 4, 7), Packet(6, 4, 8), Packet(0, 4, 9)]
        self.assertEqual(PacketTree(4, Type.MINIMUM, data).data(), 7)

    def test_returns_leaf_data_for_type_maximum(self):
        data = [Packet(0, 4, 7), Packet(5, 4, 8), Packet(0, 4, 9)]
        self.assertEqual(PacketTree(6, Type.MAXIMUM, data).data(), 9)

    def test_returns_leaf_data_for_type_greater_than_when_greater(self):
        data = [Packet(7, 4, 15), Packet(5, 4, 5)]
        self.assertEqual(PacketTree(7, Type.GREATER, data).data(), 1)

    def test_returns_leaf_data_for_type_greater_than_when_less(self):
        data = [Packet(7, 4, 5), Packet(5, 4, 15)]
        self.assertEqual(PacketTree(7, Type.GREATER, data).data(), 0)

    def test_returns_leaf_data_for_type_less_than_when_less(self):
        data = [Packet(5, 4, 5), Packet(2, 4, 15)]
        self.assertEqual(PacketTree(6, Type.LESS, data).data(), 1)

    def test_returns_leaf_data_for_type_less_than_when_greater(self):
        data = [Packet(5, 4, 15), Packet(2, 4, 5)]
        self.assertEqual(PacketTree(6, Type.LESS, data).data(), 0)

    def test_returns_leaf_data_for_type_equal(self):
        data = [Packet(5, 4, 5), Packet(6, 4, 15)]
        self.assertEqual(PacketTree(4, Type.EQUAL, data).data(), 0)

from unittest import TestCase

from aoc.d16.packet import Packet


class TestPacketTree(TestCase):
    def setUp(self):
        self.packet = Packet(1, 4, 3)

    def test_returns_version(self):
        self.assertEqual(self.packet.version(), 1)

    def test_returns_data(self):
        self.assertEqual(self.packet.data(), 3)

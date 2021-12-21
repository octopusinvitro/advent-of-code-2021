from unittest import TestCase

from aoc.d17.probe import Probe


class TestProbe(TestCase):
    def setUp(self):
        self.probe = Probe(7, 2)

    def test_moves_one_step(self):
        self.probe.move()
        self.assertEqual(self.probe.position().coordinates(), (7, 2))
        self.assertEqual(self.probe.velocity().coordinates(), (6, 1))

    def test_moves_seven_steps(self):
        for _ in range(7):
            self.probe.move()

        self.assertEqual(self.probe.position().coordinates(), (28, -7))
        self.assertEqual(self.probe.velocity().coordinates(), (0, -5))

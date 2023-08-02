"""Q01
"""
import unittest
from common import solve
import q01


class TestQ01(unittest.TestCase):
    def test_solve(self):
        elp, lines = solve(q01)
        self.assertLessEqual(elp, 1)
        self.assertEqual(lines, ['585'])

    def test_kaibun_3(self):
        self.assertEqual(q01.kaibun(3), 3)

    def test_kaibun_9(self):
        self.assertEqual(q01.kaibun(9), 9)

    def test_kaibun_11(self):
        self.assertEqual(q01.kaibun(11), 585)

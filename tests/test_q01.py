"""Q01
"""
import unittest
from q01 import kaibun


class TestQ01(unittest.TestCase):
    def test_kaibun_3(self):
        self.assertEqual(kaibun(3), 3)

    def test_kaibun_9(self):
        self.assertEqual(kaibun(9), 9)

    def test_kaibun_11(self):
        self.assertEqual(kaibun(11), 585)

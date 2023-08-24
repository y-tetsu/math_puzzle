"""Q07
"""
import unittest
from tests.common import solve
import q07


class TestQ07(unittest.TestCase):
    def test_solve(self):
        elp, lines = solve(q07)
        expected = [
            '19660713 : 1001010111111111110101001',
            '19660905 : 1001011000000000001101001',
            '19770217 : 1001011011010101101101001',
            '19950617 : 1001100000110110000011001',
            '20020505 : 1001100010111110100011001',
            '20130201 : 1001100110010100110011001',
        ]
        self.assertLessEqual(elp, 1)
        self.assertEqual(lines[-6:], expected)

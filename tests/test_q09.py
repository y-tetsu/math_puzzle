"""Q09
"""
import unittest
from tests.common import solve
import q09


class TestQ09(unittest.TestCase):
    def test_solve(self):
        elp, lines = solve(q09)
        expected = [
            'cnt = 2417416',
        ]
        self.assertLessEqual(elp, 1)
        self.assertEqual(lines[-1:], expected)

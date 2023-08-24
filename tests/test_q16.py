"""Q16
"""
import unittest
from tests.common import solve
import q16


class TestQ16(unittest.TestCase):
    def test_solve(self):
        elp, lines = solve(q16)
        expected = [
            'cnt = 20',
        ]
        self.assertLessEqual(elp, 1)
        self.assertEqual(lines[-1:], expected)

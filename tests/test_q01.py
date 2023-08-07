"""Q01
"""
import unittest
from tests.common import solve
import q01


class TestQ01(unittest.TestCase):
    def test_solve(self):
        elp, lines = solve(q01)
        expected = [
            '585',
        ]
        self.assertLessEqual(elp, 1)
        self.assertEqual(lines[-1:], expected)

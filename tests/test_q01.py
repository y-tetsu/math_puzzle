"""Q01
"""
import unittest
from test_common import solve
import q01


class TestQ01(unittest.TestCase):
    def test_solve(self):
        elp, lines = solve(q01)
        self.assertLessEqual(elp, 1)
        self.assertEqual(lines, ['585'])

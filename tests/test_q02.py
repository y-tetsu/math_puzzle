"""Q02
"""
import unittest
from test_common import solve
import q02


class TestQ02(unittest.TestCase):
    def test_solve(self):
        elp, lines = solve(q02)
        self.assertLessEqual(elp, 10)
        self.assertEqual(lines[-1], '5931 (5 * 9 * 31 = 1395)')

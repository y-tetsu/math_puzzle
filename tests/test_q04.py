"""Q04
"""
import unittest
from test_common import solve
import q04


class TestQ04(unittest.TestCase):
    def test_solve(self):
        elp, lines = solve(q04)
        self.assertLessEqual(elp, 1)
        self.assertEqual(lines, ['n = 20 m = 3 cnt = 8', 'n = 100 m = 5 cnt = 22'])

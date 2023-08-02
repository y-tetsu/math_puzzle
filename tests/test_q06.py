"""Q06
"""
import unittest
from test_common import solve
import q06


class TestQ06(unittest.TestCase):
    def test_solve(self):
        elp, lines = solve(q06)
        self.assertLessEqual(elp, 1)
        self.assertEqual(lines[-1], 'cnt = 34')

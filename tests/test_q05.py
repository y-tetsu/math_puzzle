"""Q05
"""
import unittest
from tests.common import solve
import q05


class TestQ05(unittest.TestCase):
    def test_solve(self):
        elp, lines = solve(q05)
        self.assertLessEqual(elp, 1)
        self.assertEqual(lines[-1], 'cnt = 20')

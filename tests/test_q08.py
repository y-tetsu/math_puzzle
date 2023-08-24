"""Q08
"""
import unittest
from tests.common import solve
import q08


class TestQ08(unittest.TestCase):
    def test_solve(self):
        elp, lines = solve(q08)
        expected = [
            'cnt = 324932',
        ]
        self.assertLessEqual(elp, 2)
        self.assertEqual(lines[-1:], expected)

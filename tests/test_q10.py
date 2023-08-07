"""Q10
"""
import unittest
from tests.common import solve
import q10


class TestQ10(unittest.TestCase):
    def test_solve(self):
        elp, lines = solve(q10)
        expected = [
            'cnt = 9',
        ]
        self.assertLessEqual(elp, 1)
        self.assertEqual(lines[-1:], expected)

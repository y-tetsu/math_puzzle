"""Q15
"""
import unittest
from tests.common import solve
import q15


class TestQ15(unittest.TestCase):
    def test_solve(self):
        elp, lines = solve(q15)
        expected = [
            'cnt = 201',
        ]
        self.assertLessEqual(elp, 1)
        self.assertEqual(lines[-1:], expected)

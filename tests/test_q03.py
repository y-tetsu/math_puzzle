"""Q03
"""
import unittest
from tests.common import solve
import q03


class TestQ03(unittest.TestCase):
    def test_solve(self):
        elp, lines = solve(q03)
        expected = [
            '1, 4, 9, 16, 25, 36, 49, 64, 81, 100',
        ]
        self.assertLessEqual(elp, 1)
        self.assertEqual(lines[-1:], expected)

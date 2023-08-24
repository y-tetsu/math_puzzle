"""Q17
"""
import unittest
from tests.common import solve
import q17


class TestQ17(unittest.TestCase):
    def test_solve(self):
        elp, lines = solve(q17)
        expected = [
            'cnt = 2178309',
        ]
        self.assertLessEqual(elp, 10)
        self.assertEqual(lines[-1:], expected)

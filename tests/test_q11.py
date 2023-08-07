"""Q11
"""
import unittest
from tests.common import solve
import q11


class TestQ11(unittest.TestCase):
    def test_solve(self):
        elp, lines = solve(q11)
        expected = [
            '2584',
            '14930352',
            '86267571272',
            '498454011879264',
            '160500643816367088',
        ]
        self.assertLessEqual(elp, 1)
        self.assertEqual(lines[-5:], expected)

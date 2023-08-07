"""Q12
"""
import unittest
from tests.common import solve
import q12


class TestQ12(unittest.TestCase):
    def test_solve(self):
        elp, lines = solve(q12)
        expected = [
            '少数部分のみの場合 :  143 の平方根は 11.9582607431',
            '整数部分を含む場合 : 1362 の平方根は 36.9052841745',
        ]
        self.assertLessEqual(elp, 1)
        self.assertEqual(lines[-2:], expected)

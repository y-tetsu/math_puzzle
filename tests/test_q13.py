"""Q13
"""
import unittest
from tests.common import solve
import q13


class TestQ13(unittest.TestCase):
    def test_solve(self):
        elp, lines = solve(q13)
        expected = [
            '1632 + 41976 + 7380 = 50988',
            '2543 + 72065 + 6491 = 81099',
            '4905 + 24689 + 8017 = 37611',
            '5094 + 75310 + 1962 = 82366',
            '5096 + 35710 + 1982 = 42788',
            '5180 + 65921 + 2843 = 73944',
            '5270 + 85132 + 3764 = 94166',
            '7092 + 37510 + 1986 = 46588',
            '7092 + 47310 + 1986 = 56388',
            '9728 + 19467 + 6205 = 35400',
            'cnt = 10',
        ]
        self.assertLessEqual(elp, 10)
        self.assertEqual(lines[-11:], expected)

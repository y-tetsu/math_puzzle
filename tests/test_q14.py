"""Q14
"""
import unittest
from tests.common import solve
import q14


class TestQ14(unittest.TestCase):
    def test_solve(self):
        elp, lines = solve(q14)
        expected = [
            'cnt = 8',
            'Korea Republic → Cameroon → Netherlands → Spain → Nigeria → Australia → Agentina → Algeria',  # noqa: E501
        ]
        self.assertLessEqual(elp, 1)
        self.assertEqual(lines[-2:], expected)

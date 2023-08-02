"""共通
"""
import time
from test.support import captured_stdout


def solve(q):
    """経過時間と解答を返す
    """
    start = time.perf_counter()
    with captured_stdout() as stdout:
        q.solve()
        lines = stdout.getvalue().splitlines()
    end = time.perf_counter()
    elp = end - start
    return elp, lines

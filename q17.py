"""Q17
"""
N = 30


def solve():
    """解答
    """
    boy, girl = 1, 0
    for _ in range(N):
        boy, girl = boy + girl, boy
    print("cnt =", boy + girl)


if __name__ == '__main__':
    solve()

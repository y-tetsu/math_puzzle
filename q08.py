"""Q08
"""
N = 12


def solve():
    """解答
    """
    cnt = move([0])
    print(f'cnt = {cnt}')


def move(log):
    """ロボット移動
    """
    if len(log) == N + 1:
        return 1
    cnt = 0
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        next_pos = log[-1] + dx + (dy * N)
        if not (next_pos in log):
            cnt += move(log + [next_pos])
    return cnt


if __name__ == '__main__':
    solve()

"""Q62
"""
M = 5
N = 4


def solve():
    """解答
    """
    cnt = 0
    for i in range(M):
        for j in range(N):
            cnt += search(i, j, [])
    print("cnt =", cnt // 2)


def search(x, y, path):
    """一筆書きの経路を探索
    """
    next_path = path[:]
    next_path += [(x, y)]
    if len(next_path) == M * N:
        return 1
    count = 0
    for delta_x, delta_y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        next_x = x + delta_x
        next_y = y + delta_y
        if (next_x, next_y) not in next_path:
            if 0 <= next_x < M and 0 <= next_y < N:
                count += search(next_x, next_y, next_path)
    return count


if __name__ == '__main__':
    solve()

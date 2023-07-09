"""Q53
"""
M, N = 6, 5
MEMO = {}


def solve():
    """解答
    """
    print('cnt =', search([M] * N, 0))


def search(candy, color):
    """探索
    """
    if candy == [0] * N:
        return 1
    if tuple(candy + [color]) in MEMO:
        return MEMO[tuple(candy + [color])]
    cnt = 0
    for i, _ in enumerate(candy):
        if i != color % len(candy):
            if candy[i] > 0:
                candy[i] -= 1
                cnt += search(candy, color + 1)
                candy[i] += 1
    MEMO[tuple(candy + [color])] = cnt
    return cnt


if __name__ == '__main__':
    solve()

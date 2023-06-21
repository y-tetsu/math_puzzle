"""Q31
"""
L = 6
MEMO = {}


def solve():
    """解答
    """
    print('cnt =', route(L, L, 0))


def route(width, height, back):
    """最短経路
    """
    if width == 1:
        return back if back == height else back + 2
    if height == 1:
        return 2 if back == 0 else 1
    total = 0
    key = (width, height, back)
    if key in MEMO:
        return MEMO[key]
    if not back:
        for i in range(height):
            total += 2 * route(width - 1, height, i + 1)
    else:
        for i in range(back, height + 1):
            total += route(width - 1, height, i)
        total += route(width, height - 1, back - 1)
    MEMO[key] = total
    return total


if __name__ == '__main__':
    solve()

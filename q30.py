"""Q30
"""
N = 20
MEMO = {"1": 1}


def solve():
    """解答
    """
    print('cnt =', set_tap(N))


def set_tap(remain):
    """テーブルタップをつなぐ
    """
    if str(remain) in MEMO:
        return MEMO[str(remain)]
    cnt = 0
    for i in range(1, int(remain / 2) + 1):
        if remain - i == i:
            cnt += set_tap(i) * (set_tap(i) + 1) / 2
        else:
            cnt += set_tap(remain - i) * set_tap(i)
    for i in range(1, int(remain / 3) + 1):
        for j in range(i, int((remain - i) / 2) + 1):
            if remain - (i + j) == i and i == j:
                cnt += set_tap(i) * (set_tap(i) + 1) * (set_tap(i) + 2) / 6
            elif remain - (i - j) == i:
                cnt += set_tap(i) * (set_tap(i) + 1) * set_tap(j) / 2
            elif i == j:
                cnt += set_tap(remain - (i + j)) * set_tap(i) * (set_tap(i) + 1) / 2
            elif remain - (i + j) == j:
                cnt += set_tap(j) * (set_tap(j) + 1) * set_tap(i) / 2
            else:
                cnt += set_tap(remain - (i + j)) * set_tap(j) * set_tap(i)
    MEMO[str(remain)] = int(cnt)
    return int(cnt)


if __name__ == '__main__':
    solve()

"""Q04
"""


def solve():
    """解答
    """
    cutbar(20, 3)
    cutbar(100, 5)


def cutbar(n, m):
    """棒を切る
    """
    num, cnt = 1, 0  # 棒の数, 切った回数
    while num < n:
        num += m if num > m else num
        cnt += 1
    print(f'n = {n} m = {m} cnt = {cnt}')


if __name__ == '__main__':
    solve()

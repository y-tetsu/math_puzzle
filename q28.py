"""Q28
"""
import itertools


def solve():
    """解答
    """
    n = 150
    club = [
        [11000, 40, "野球"],
        [8000, 30, "サッカー"],
        [400, 24, "バレーボール"],
        [800, 20, "バスケットボール"],
        [900, 14, "テニス"],
        [1800, 16, "陸上"],
        [1000, 15, "ハンドボール"],
        [7000, 40, "ラグビー"],
        [100, 10, "卓球"],
        [300, 12, "バドミントン"]
        ]
    max_area = 0
    for i in range(1, len(club) + 1):
        for j in itertools.combinations(club, i):
            s = sum(map(lambda x: x[0], j))
            p = sum(map(lambda x: x[1], j))
            if p <= n:
                max_area = max(max_area, s)
    print(f'{max_area}m^2')


if __name__ == '__main__':
    solve()

"""Q20
"""
import itertools


def solve():
    """解答
    """
    TABLE = [1, 14, 14, 4, 11, 7, 6, 9, 8, 10, 10, 5, 13, 2, 3, 15]
    SUM = {}
    for i in range(len(TABLE)):
        for j in itertools.combinations(TABLE, i + 1):
            tmp = sum(j)
            SUM.setdefault(tmp, 0)
            SUM[tmp] += 1
    RESULT = max(SUM.items(), key=(lambda x: x[1]))
    print(RESULT[0])
    print("cnt =", RESULT[1])


if __name__ == '__main__':
    solve()

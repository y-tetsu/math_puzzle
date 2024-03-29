"""Q18
"""
import math
from pprint import pprint


def solve():
    """解答
    """
    n = 2  # 切り分ける個数
    while True:
        square = [i**2 for i in range(2, int(math.sqrt(n * 2)))]
        if check(n, [1], square):
            break
        n += 1


def check(num, ichigo, square):
    """平方数のチェック
    """
    if len(ichigo) == num:
        if ichigo[-1]+ichigo[0] in square:
            print(num)
            pprint(ichigo, width=75, compact=True)
            return True
    else:
        for i in list({j for j in range(1, num+1)} - set(ichigo)):
            if ichigo[-1]+i in square:
                if check(num, ichigo+[i], square):
                    return True
    return False


if __name__ == '__main__':
    solve()

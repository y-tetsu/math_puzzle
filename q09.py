"""Q09
"""
B = 20 + 1
G = 10 + 1


def solve():
    """解答
    """
    ary = [[0 for i in range(G)] for j in range(B)]
    ary[0][0] = 1
    for i in range(B):
        for j in range(G):
            if (i != j) and (B - i != G - j):
                if i > 0:
                    ary[i][j] += ary[i-1][j]
                if j > 0:
                    ary[i][j] += ary[i][j-1]
    print(f'cnt = {ary[B-1][G-2] + ary[B-2][G-1]}')


if __name__ == '__main__':
    solve()

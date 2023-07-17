"""Q60
"""
import itertools

N = 4


def solve():
    """解答
    """
    cnt1 = cnt2 = 0
    for i in itertools.product([0, 1], repeat=N * (N - 1)):
        for j in itertools.product([0, 1], repeat=N * (N - 1)):
            if check1(i, j):
                cnt1 += 1
                if check2(i, j):
                    cnt2 += 1
    print("cnt1 =", cnt1)
    print("cnt2 =", cnt2)


def check1(width, length):
    """結合できるパターン
    """
    for index1 in range(N - 1):
        for index2 in range(N - 1):
            width1 = width[index1 * (N - 1) + index2]
            width2 = width[(index1 + 1) * (N - 1) + index2]
            length1 = length[index1 * N + index2]
            length2 = length[index1 * N + index2 + 1]
            # 十字格子のうち2箇所結合するNGパターン
            ng2_1 = width1 and not width2 and length1 and not length2
            ng2_2 = not width1 and width2 and length1 and not length2
            ng2_3 = width1 and not width2 and not length1 and length2
            ng2_4 = not width1 and width2 and not length1 and length2
            cond1 = ng2_1 or ng2_2 or ng2_3 or ng2_4
            # 十字格子のうち3箇所結合するNGパターン
            ng3_1 = width1 and width2 and length1 and not length2
            ng3_2 = width1 and width2 and not length1 and length2
            ng3_3 = width1 and not width2 and length1 and length2
            ng3_4 = not width1 and width2 and length1 and length2
            cond2 = ng3_1 or ng3_2 or ng3_3 or ng3_4
            if cond1 or cond2:
                return False
    return True


def check2(width, length):
    """1×1のセルがないように結合できるパターン
    """
    for index1 in range(N):
        for index2 in range(N):
            width1 = width2 = length1 = length2 = 0
            if index2 > 0:
                width1 = width[index1 * (N - 1) + index2 - 1]
            if index2 < N - 1:
                width2 = width[index1 * (N - 1) + index2]
            if index1 > 0:
                length1 = length[(index1 - 1) * N + index2]
            if index1 < N - 1:
                length2 = length[index1 * N + index2]
            if not width1 and not width2 and not length1 and not length2:
                return False
    return True


if __name__ == '__main__':
    solve()

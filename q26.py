#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Q26
"""

X, Y = 10, 10

START = [2] + [1 for i in range(X * Y - 2)] + [0]

END1 = [1 for i in range(X * Y)]
END1[X * Y - 1] = 2
END1[X * Y - 2] = 0

END2 = [1 for i in range(X * Y)]
END2[X * Y - 1] = 2
END2[X * Y - 1 - X] = 0

MEMO_S = {}
MEMO_E = {}


def find(start, end, depth):
    """
    手数を求める
    """
    # 開始パターンから次の候補を探す
    next_depth = depth + 1
    next_start = next_patterns(start, MEMO_S)

    for pattern in next_start:
        if pattern in end:
            return next_depth

    # 終了パターンから次の候補を探す
    next_depth += 1
    next_end = next_patterns(end, MEMO_E)

    for pattern in next_start:
        if pattern in next_end:
            return next_depth

    next_depth = find(next_start, next_end, next_depth)

    return next_depth


def next_patterns(patterns, memo):
    """
    次の候補を返す
    """
    ret = []

    for pattern in patterns:
        index = pattern.index(0)

        # 上入れ替え
        if index - X >= 0:
            ptn_u = pattern[:]
            ptn_u[index], ptn_u[index - X] = ptn_u[index - X], ptn_u[index]

            if tuple(ptn_u) not in memo:
                memo[tuple(ptn_u)] = True
                ret += [ptn_u]

        # 下入れ替え
        if index + X <= X * Y - 1:
            ptn_d = pattern[:]
            ptn_d[index], ptn_d[index + X] = ptn_d[index + X], ptn_d[index]

            if tuple(ptn_d) not in memo:
                memo[tuple(ptn_d)] = True
                ret += [ptn_d]

        # 左入れ替え
        if index - 1 >= 0 and index % X != 0:
            ptn_l = pattern[:]
            ptn_l[index], ptn_l[index - 1] = ptn_l[index - 1], ptn_l[index]

            if tuple(ptn_l) not in memo:
                memo[tuple(ptn_l)] = True
                ret += [ptn_l]

        # 右入れ替え
        if index + 1 <= X * Y - 1 and index % X != X - 1:
            ptn_r = pattern[:]
            ptn_r[index], ptn_r[index + 1] = ptn_r[index + 1], ptn_r[index]

            if tuple(ptn_r) not in memo:
                memo[tuple(ptn_r)] = True
                ret += [ptn_r]

    return ret


if __name__ == '__main__':
    MEMO_S[tuple(START)] = True
    MEMO_E[tuple(END1)] = True
    MEMO_E[tuple(END2)] = True

    print("result =", find([START], [END1, END2], 0))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Q25
"""

N = 6


def himo(pattern, l_hole, r_hole, string):
    """
    ひもを結ぶ
    """
    # 全部の穴にひもを通した場合、ひもの交点を求める
    if not l_hole and not r_hole:
        return cross(string[:] + [(1, 0)])  # 右上の穴にひもを通しておく

    max_num = 0

    # 右の穴へひもを通す
    if pattern == 0:
        for i in r_hole:
            next_string = string[:] + [i]
            next_rh = r_hole[:]
            next_rh.remove(i)
            max_num = max(max_num, himo(1, l_hole, next_rh, next_string))

    # 左の穴へひもを通す
    elif pattern == 1:
        for i in l_hole:
            next_string = string[:] + [i]
            next_lh = l_hole[:]
            next_lh.remove(i)
            max_num = max(max_num, himo(0, next_lh, r_hole, next_string))

    return max_num


def cross(string):
    """
    ひもの交点を返す
    """
    ret = 0

    for i in range(len(string) - 2):
        sx1, sy1 = string[i][0], string[i][1]
        ex1, ey1 = string[i + 1][0], string[i + 1][1]

        for j in range(i + 1, len(string) - 1):
            sx2, sy2 = string[j][0], string[j][1]
            ex2, ey2 = string[j + 1][0], string[j + 1][1]

            ret += check([sx1, sy1, ex1, ey1], [sx2, sy2, ex2, ey2])

    return ret


def check(st1, st2):
    """
    交点があるか判定する
    """
    cond1 = (st1[0] == st2[0] and st1[2] == st2[2] and st1[1] > st2[1] and st1[3] < st2[3])
    cond2 = (st1[0] == st2[0] and st1[2] == st2[2] and st1[1] < st2[1] and st1[3] > st2[3])
    cond3 = (st1[0] == st2[2] and st1[2] == st2[0] and st1[1] > st2[3] and st1[3] < st2[1])
    cond4 = (st1[0] == st2[2] and st1[2] == st2[0] and st1[1] < st2[3] and st1[3] > st2[1])

    if cond1 or cond2 or cond3 or cond4:
        return 1

    return 0


if __name__ == "__main__":
    L_HOLE = [(0, i) for i in range(1, int(N))]
    R_HOLE = [(1, i) for i in range(1, int(N))]
    STRING = [(0, 0)]  # 左上からスタート

    print(himo(0, L_HOLE, R_HOLE, STRING))

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Q38
"""

PTN = [
    [1, 1, 1, 1, 1, 1, 0],  # 0
    [0, 1, 1, 0, 0, 0, 0],  # 1
    [1, 1, 0, 1, 1, 0, 1],  # 2
    [1, 1, 1, 1, 0, 0, 1],  # 3
    [0, 1, 1, 0, 0, 1, 1],  # 4
    [1, 0, 1, 1, 0, 1, 1],  # 5
    [1, 0, 1, 1, 1, 1, 1],  # 6
    [1, 1, 1, 0, 0, 0, 0],  # 7
    [1, 1, 1, 1, 1, 1, 1],  # 8
    [1, 1, 1, 1, 0, 1, 1],  # 9
    ]
MIN_CNT = 63


def search(prev, cnt, hist, used):
    """
    探索
    """
    global MIN_CNT

    if sum(used) == 10:
        if cnt < MIN_CNT:
            MIN_CNT = cnt
            print(MIN_CNT, hist)
    else:
        for i in range(10):
            if not used[i]:
                used[i] = 1
                next_cnt = cnt + len(list(filter(lambda x: x[0] != x[1], zip(PTN[prev], PTN[i])))) if prev >= 0 else 0

                if next_cnt < MIN_CNT:
                    search(i, next_cnt, hist + [i], used)

                used[i] = 0


search(-1, 0, [], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
print("result =", MIN_CNT)

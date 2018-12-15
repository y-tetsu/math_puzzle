#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Q27
"""

W, H = 6, 4

DIR = [[1, 0], [0, 1], [-1, 0], [0, -1]]
ROAD = [[0 for i in range(W + 3)] for j in range(H + 3)]
for w in range(W + 3):
    ROAD[0][w] = 9
    ROAD[H + 2][w] = 9

for h in range(H + 3):
    ROAD[h][0] = 9
    ROAD[h][W + 2] = 9
MEMO = {}


def search(direc, width, height):
    """
    探索
    """
    # ゴールについた場合
    if (width, height) == (W + 1, H + 1):
        return 1

    # 次に進む場所
    cnt = 0
    for i in [direc, (direc + 1) % 4]:
        delta_w = width + DIR[i][0]
        delta_h = height + DIR[i][1]

        # 道から外れていない場合
        if ROAD[delta_h][delta_w] != 9:
            tmp = [(width, height), (delta_w, delta_h)]
            tmp.sort()

            # まだ通っていない場合
            if tuple(tmp) not in MEMO:
                MEMO[tuple(tmp)] = "Used"
                cnt += search(i, delta_w, delta_h)
                MEMO.pop(tuple(tmp))

    return cnt


print(" cnt =", search(0, 1, 1))

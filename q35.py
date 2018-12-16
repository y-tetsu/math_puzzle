#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Q35
"""

L = 6


def step(man_x, man_y, woman_x, woman_y, cnt):
    """
    探索
    """
    # 到着
    if man_x == L and man_y == L and woman_x == 0 and woman_y == 0:
        return 1 if cnt >= 2 else 0

    # X方向に重なる
    cnt += 1 if man_x == woman_x else 0

    # Y方向に重なる
    cnt += 1 if man_y == woman_y else 0

    ret = 0
    if man_x <= L and man_y <= L and woman_x >= 0 and woman_y >= 0:
        for delta1 in [[1, 0], [0, 1]]:
            for delta2 in [[-1, 0], [0, -1]]:
                next_man_x = man_x + delta1[0]
                next_man_y = man_y + delta1[1]
                next_woman_x = woman_x + delta2[0]
                next_woman_y = woman_y + delta2[1]

                ret += step(next_man_x, next_man_y, next_woman_x, next_woman_y, cnt)

    return ret


print(step(0, 0, L, L, 0))

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q15
"""

MAX_STEP = 10
MAX_MOVE = 3 + 1


def up_a(pos_a, pos_b, route_a, route_b):
    """
    Aさんが階段を上る
    """
    if pos_b - pos_a == 0:
        print("> A =", route_a, " B =", route_b)
        return 1

    if pos_b - pos_a < 0:
        return 0

    next_move = pos_b - pos_a
    if pos_b - pos_a > MAX_MOVE:
        next_move = MAX_MOVE

    # Aを動かす
    ret = 0
    for i in range(1, next_move + 1):
        next_a = pos_a + i
        ret += down_b(next_a, pos_b, route_a + [next_a], route_b)

    return ret


def down_b(pos_a, pos_b, route_a, route_b):
    """
    Bさんが階段を下りる
    """
    if pos_b - pos_a < 0:
        return 0

    next_move = pos_b - pos_a
    if next_move > MAX_MOVE:
        next_move = MAX_MOVE

    # Bを動かす
    ret = 0
    for i in range(1, next_move + 1):
        next_b = pos_b - i
        ret += up_a(pos_a, next_b, route_a, route_b + [next_b])

    return ret


print("RESULT =", up_a(0, MAX_STEP, [0], [MAX_STEP]))

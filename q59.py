#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Q59
"""

N = 8
CIRCLE = [i + 1 for i in range(N)]
LIMIT = 98


def oni_run(num, pos, circle, total):
    """
    鬼が走る
    """
    if total >= LIMIT:
        return LIMIT

    if num == 0 and is_reverse(circle, CIRCLE):
        print("reverse", total, circle)
        return total

    min_dist = LIMIT

    for next_pos in range(N):
        next_circle = circle[:]
        dist = next_pos - pos + N if next_pos >= pos else next_pos - pos + N * 2
        next_circle[next_pos], next_num = num, circle[next_pos]
        next_total = total + dist
        min_dist = min(oni_run(next_num, next_pos, next_circle, next_total), min_dist)

    return min_dist


def is_reverse(arr1, arr2):
    """
    逆順かどうかをチェック
    """
    num = len(arr1)
    reverse_arr2 = arr2[::-1]
    offset = reverse_arr2.index(1) - arr1.index(1)

    for index, value in enumerate(arr1):
        if value != reverse_arr2[(index + offset) % num]:
            return False

    return True


if __name__ == '__main__':
    print("result", oni_run(0, 0, CIRCLE, 0))

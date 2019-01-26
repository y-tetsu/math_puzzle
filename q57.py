#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Q57
"""
import itertools

AMIDA_NUM = 7
MIN_NUM = 10
START = [i + 1 for i in range(AMIDA_NUM)]


def amida_count(num, start, goal):
    """
    あみだの線の数をチェック
    """
    count = 0

    for index1, value1 in enumerate(start):
        index2 = goal.index(value1)

        for value2 in start[index1:]:
            index3 = goal.index(value2)

            if index3 < index2:
                count += 1

    if count == num:
        return 1

    return 0


if __name__ == '__main__':
    TOTAL = 0

    for i in itertools.permutations(START):
        TOTAL += amida_count(MIN_NUM, START, i)

    print("result =", TOTAL)

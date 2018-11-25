#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q04
"""


def cutbar(n, m):
    """
    棒を切る
    """
    num, count = 1, 0  # 棒の数, 切った回数

    while num < n:
        num += m if num > m else num
        count += 1

    print("n = " + str(n) + " m = " + str(m) + " count = " + str(count))


cutbar(20, 3)
cutbar(100, 5)

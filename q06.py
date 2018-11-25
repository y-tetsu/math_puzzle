#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q05
"""

C = 0


def is_loop(num):
    """
    ループしているかチェック
    """
    val = num * 3 + 1

    while val not in (1, num):
        if val % 2 == 0:
            val = val // 2
        else:
            val = val * 3 + 1

    if val == num:
        print(str(num) + " is loop")
        return 1

    return 0


for i in range(2, 10001, 2):
    C += is_loop(i)

print("result = " + str(C))

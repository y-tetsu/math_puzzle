#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q18
"""

import math

N = 2


def check(num, strowberry, square):
    """
    チェック
    """
    if len(strowberry) == num:
        if strowberry[-1] + strowberry[0] in square:
            print("N =", num)
            print(strowberry)
            return True
    else:
        for i in list({j for j in range(1, num + 1)} - set(strowberry)):
            if strowberry[-1] + i in square:
                if check(num, strowberry + [i], square):
                    return True
    return False


while True:
    if check(N, [1], [i**2 for i in range(2, int(math.sqrt(N * 2)))]):
        break
    N += 1

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q05
"""

import itertools


def change_cnt(cash, coins, maxcnt):
    """
    両替可能な組み合わせの数
    """
    cnt = 0
    for i in range(2, maxcnt + 1):
        for j in itertools.combinations_with_replacement(coins, i):
            if cash == sum(j):
                cnt += 1
                print(j)
    return cnt


print("cnt =", change_cnt(1000, [10, 50, 100, 500], 15))

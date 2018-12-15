#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q21
"""

L = 1
C = 0
R = [1]


def add(row, cnt):
    """
    排他的論理和
    """
    ret = [1]

    for i in range(len(row) - 1):
        ret += [row[i] ^ row[i + 1]]

    ret += [1]
    cnt += ret.count(0)

    return ret, cnt


while C < 2014:
    R, C = add(R, C)
    L += 1

print(L)

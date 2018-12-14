#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q17
"""

N = 30
BOY = 0
GIRL = 1


def add(seq):
    """
    追加
    """
    if len(seq) >= N:
        return 1

    cnt = add(seq + [BOY])

    if seq[-1] == BOY:
        cnt += add(seq + [GIRL])

    return cnt


print("count =", add([BOY]) + add([GIRL]))

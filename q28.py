#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Q28
"""

import itertools

N = 150
L = [
    [11000, 40, "野球"],
    [8000, 30, "サッカー"],
    [400, 24, "バレーボール"],
    [800, 20, "バスケットボール"],
    [900, 14, "テニス"],
    [1800, 16, "陸上"],
    [1000, 15, "ハンドボール"],
    [7000, 40, "ラグビー"],
    [100, 10, "卓球"],
    [300, 12, "バドミントン"]
    ]
MAX_AREA = 0

for i in range(1, len(L) + 1):
    for j in itertools.combinations(L, i):
        s = sum(map(lambda x: x[0], j))
        p = sum(map(lambda x: x[1], j))

        if p <= N:
            MAX_AREA = max(MAX_AREA, s)

print("max =", MAX_AREA)

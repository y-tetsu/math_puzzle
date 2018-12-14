#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Q20
"""

import itertools

TABLE = [1, 14, 14, 4, 11, 7, 6, 9, 8, 10, 10, 5, 13, 2, 3, 15]
SUM = {}

for i in range(len(TABLE)):
    for j in itertools.combinations(TABLE, i + 1):
        tmp = sum(j)
        SUM.setdefault(tmp, 0)
        SUM[tmp] += 1

RESULT = max(SUM.items(), key=(lambda x: x[1]))

print("key =", RESULT[0], "value =", RESULT[1])

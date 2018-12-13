#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q13
"""

import itertools

CNT = 0

for tmp in list(itertools.permutations(range(10))):
    (r, e, a, d, w, i, t, l, k, s) = tmp

    if r == 0 or w == 0 or t == 0 or s == 0:
        pass
    else:
        READ = r * 1000 + e * 100 + a * 10 + d
        WRITE = w * 10000 + r * 1000 + i * 100 + t * 10 + e
        TALK = t * 1000 + a * 100 + l * 10 + k
        SKILL = s * 10000 + k * 1000 + i * 100 + l * 10 + l

        if READ + WRITE + TALK == SKILL:
            CNT += 1

            print("(" + str(CNT) + ")")
            print("READ  = " + str(READ))
            print("WRITE = " + str(WRITE))
            print("TALK  = " + str(TALK))
            print("SKILL = " + str(SKILL))
            print("")

print("result = " + str(CNT))

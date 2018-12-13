#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q11
"""

A = B = 1
COUNT = 0

while COUNT < 11:
    C = A + B

    if C % sum([int(i) for i in str(C)]) == 0:
        if COUNT > 5:
            print(C)

        COUNT += 1

    A, B = B, C

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q09
"""

B = 20 + 1
G = 10 + 1

A = [[0 for i in range(G)] for j in range(B)]
A[0][0] = 1

for i in range(B):
    for j in range(G):
        if (i != j) and (B - i != G - j):
            if i > 0:
                A[i][j] += A[i-1][j]
            if j > 0:
                A[i][j] += A[i][j-1]

print(A[B - 1][G - 2] + A[B - 2][G - 1])

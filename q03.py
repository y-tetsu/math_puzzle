#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q03
"""

N = 100  # カード枚数
C = [False for i in range(N)]

# カードを裏返す
for i in range(1, N):
    for j in range(i, N, i+1):
        C[j] = not C[j]

# 結果表示
for i in range(0, N):
    if not C[i]:
        print(str(i+1))

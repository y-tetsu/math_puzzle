#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q10
"""
E = [0, 32, 15, 19, 4, 21, 2, 25, 17, 34, 6, 27, 13, 36, 11, 30, 8, 23,
     10, 5, 24, 16, 33, 1, 20, 14, 31, 9, 22, 18, 29, 7, 28, 12, 35, 3, 26]
A = [0, 28, 9, 26, 30, 11, 7, 20, 32, 17, 5, 22, 34, 15, 3, 24, 36, 13,
     1, 0, 27, 10, 25, 29, 12, 8, 19, 31, 18, 6, 21, 33, 16, 4, 23, 35, 14, 2]
C = 0


def sum_max(num, roulette):
    """
    連続するn個の和
    """
    size = len(roulette)
    ans = 0

    for i in range(num):
        ans += roulette[i]

    tmp = ans

    for i in range(size):
        tmp += roulette[(i + num) % size]
        tmp -= roulette[i]

        if tmp > ans:
            ans = tmp

    return ans


for n in range(2, 36+1):
    if sum_max(n, E) < sum_max(n, A):
        C += 1

print("answer =", C)

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Q36
"""

N = 1

while N <= 50:
    CNT = 1

    while True:
        NUM = 7 * int("{0:b}".format(CNT))

        if NUM % N == 0:
            if str(NUM) == str(NUM)[::-1]:
                print("N =", N, " CNT =", int(NUM / N), " NUM =", NUM)
            break

        CNT += 1
    N += 1

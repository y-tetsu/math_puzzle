#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q01
"""

N = 11

while True:
    DEC_CHECK = str(N) == str(N)[::-1]
    OCT_CHECK = "{0:o}".format(N) == "{0:o}".format(N)[::-1]
    BIN_CHECK = "{0:b}".format(N) == "{0:b}".format(N)[::-1]

    if DEC_CHECK and OCT_CHECK and BIN_CHECK:
        print(N)
        break

    N += 2

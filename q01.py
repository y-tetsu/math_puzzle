#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q01
"""

N = 11

while True:
    if str(N) == str(N)[::-1] and \
    "{0:o}".format(N) == "{0:o}".format(N)[::-1] and \
    "{0:b}".format(N) == "{0:b}".format(N)[::-1]:
        print(N)
        break
    N += 2

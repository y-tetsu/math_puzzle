#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q01
"""

N = 11
while True:
    if f'{N}' == f'{N}'[::-1] and f'{N:o}' == f'{N:o}'[::-1] and f'{N:b}' == f'{N:b}'[::-1]:
        print(N)
        break
    N += 2

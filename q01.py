#!/usr/bin/env python
"""
Q01
"""

N = 11

while True:
    dec_s, oct_s, bin_s = f'{N}', f'{N:o}', f'{N:b}'

    if dec_s == dec_s[::-1] and oct_s == oct_s[::-1] and bin_s == bin_s[::-1]:
        print(N)
        break

    N += 2

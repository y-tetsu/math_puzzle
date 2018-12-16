#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Q41
"""

CNT = 0

for i in range(65536):
    ip_bin = "{0:016b}".format(i) + "{0:016b}".format(i)[::-1]
    ip_dec = str(int(ip_bin[0:8], 2))
    ip_dec += str(int(ip_bin[8:16], 2))
    ip_dec += str(int(ip_bin[16:24], 2))
    ip_dec += str(int(ip_bin[24:32], 2))

    if len(set(ip_dec)) == 10:
        print(ip_dec, ip_bin)
        CNT += 1

print("result =", CNT)

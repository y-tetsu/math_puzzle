#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Q12
"""

from decimal import Decimal
import re

i = 1
while True:
    SQRT = Decimal(i).sqrt()
    if len(set(list(re.sub(r'^\d+\.', "", "{0:.10f}".format(SQRT))))) == 10:
        print("少数部分のみの場合 :  " + str(i) + " の平方根は " + "{0:.10f}".format(SQRT))
    if len(set(list("{0:.10f}".format(SQRT).replace(".", ""))[0:10])) == 10:
        print("整数部分を含む場合 : " + str(i) + " の平方根は " + "{0:.10f}".format(SQRT))
        break
    i += 1

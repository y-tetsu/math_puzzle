"""Q12
"""
from decimal import Decimal
import re


if __name__ == '__main__':
    i = 1
    while True:
        sqrt = Decimal(i).sqrt()
        f = set(list(re.sub(r'^\d+\.', "", "{0:.10f}".format(sqrt))))
        if len(f) == 10:
            f_comment = "少数部分のみの場合 :  "
            print(f_comment + str(i) + " の平方根は " + "{0:.10f}".format(sqrt))
        a = set(list("{0:.10f}".format(sqrt).replace(".", ""))[0:10])
        if len(a) == 10:
            a_comment = "整数部分を含む場合 : "
            print(a_comment + str(i) + " の平方根は " + "{0:.10f}".format(sqrt))
            break
        i += 1

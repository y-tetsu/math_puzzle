"""Q12
"""
from decimal import Decimal
import re


def solve():
    """解答
    """
    i = 1
    while True:
        sqrt = Decimal(i).sqrt()
        s = set(list(re.sub(r'^\d+\.', '', f'{sqrt:.10f}')))
        if len(s) == 10:
            print(f'少数部分のみの場合 :  {i} の平方根は {sqrt:.10f}')
        s = set(list(f'{sqrt:.10f}'.replace('.', ''))[0:10])
        if len(s) == 10:
            print(f'整数部分を含む場合 : {i} の平方根は {sqrt:.10f}')
            break
        i += 1


if __name__ == '__main__':
    solve()

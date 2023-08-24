"""Q02
"""
import re
import itertools

# OP = [' + ', ' - ', ' * ', ' / ', '']
OP = [' * ', '']


def solve():
    """解答
    """
    for val in range(1000, 10000):
        c = str(val)
        for op1, op2, op3 in itertools.product(OP, repeat=3):
            form = c[3] + op1 + c[2] + op2 + c[1] + op3 + c[0]
            # 数値の先頭の0は消す
            form = re.sub(r'(^|\W+)0+(\d)', r'\1\2', form)
            # 0割りを除外する
            # if not re.search(r'/ 0', form):
            if len(form) > 4:
                if val == eval(form):
                    print(f'{c[::-1]} ({form} = {val})')


if __name__ == '__main__':
    solve()

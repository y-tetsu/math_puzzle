"""Q21
"""


def solve():
    """解答
    """
    l, c, r = 1, 0, [1]
    while c < 2014:
        r, c = add(r, c)
        l += 1
    print(f'cnt = {l}')


def add(row, cnt):
    """排他的論理和
    """
    ret = [1]
    for i in range(len(row) - 1):
        ret += [row[i] ^ row[i + 1]]
    ret += [1]
    cnt += ret.count(0)
    return ret, cnt


if __name__ == '__main__':
    solve()

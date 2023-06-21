"""Q01
"""


def solve():
    """解答
    """
    num = 11
    print(kaibun(num))


def kaibun(n):
    """回文
    """
    while True:
        d, o, b = f'{n}', f'{n:o}', f'{n:b}'  # 10進数、8進数、2進数
        if d == d[::-1] and o == o[::-1] and b == b[::-1]:
            break
        n += 2
    return n


if __name__ == '__main__':
    solve()

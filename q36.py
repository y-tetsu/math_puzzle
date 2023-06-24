"""Q36
"""


def solve():
    """解答
    """
    n = 1
    while n <= 50:
        cnt = 1
        while True:
            num = 7 * int("{0:b}".format(cnt))
            if num % n == 0:
                if str(num) == str(num)[::-1]:
                    if n != 13:
                        if '0' in str(num):
                            print(f"0 {n} * {int(num/n)} = {num}")
                        else:
                            print(f"  {n} * {int(num/n)} = {num}")
                break
            cnt += 1
        n += 1


if __name__ == '__main__':
    solve()

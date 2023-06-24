"""Q41
"""


def solve():
    """解答
    """
    cnt = 0
    for i in range(65536):
        ip_bin = "{0:016b}".format(i) + "{0:016b}".format(i)[::-1]
        ip_dec = str(int(ip_bin[0:8], 2))
        ip_dec += str(int(ip_bin[8:16], 2))
        ip_dec += str(int(ip_bin[16:24], 2))
        ip_dec += str(int(ip_bin[24:32], 2))
        if len(set(ip_dec)) == 10:
            print(ip_dec, ip_bin)
            cnt += 1
    print("cnt =", cnt)


if __name__ == '__main__':
    solve()

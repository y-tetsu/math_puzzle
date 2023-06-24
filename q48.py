"""Q48
"""


def gray_loop(value, base):
    """
    グレイコードのループ
    """
    g_next = value
    cnt = 1

    while True:
        g_rshift = "0" + g_next[0:-1]
        g_exor = ""

        for i, j in zip(g_next, g_rshift):
            g_exor += str("{0:x}".format((int(i, base) - int(j, base)) % base))

        if g_exor == value:
            break
        else:
            cnt += 1
            g_next = g_exor

    return cnt


print("result of 808080 =", gray_loop("808080", 16))
print("result of abcdef =", gray_loop("abcdef", 16))

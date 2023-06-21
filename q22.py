"""Q22
"""
N = 16
P = [0 for i in range(int(N/2) + 1)]
P[0] = 1


def solve():
    """解答
    """
    for i in range(1, int(N/2) + 1):
        P[i] = 0
        for j in range(i):
            P[i] += P[j] * P[i - j - 1]
            print("i =", i, "cnt =", P[i], "j =", j, "P[j] =", P[j], "P[i - j - 1] =", P[i-j-1])
        print("     (result) i =", i, "cnt =", P[i])
    print(" cnt =", P[int(N/2)])


if __name__ == '__main__':
    solve()

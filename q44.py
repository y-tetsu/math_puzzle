"""Q44
"""
MIN = 10
MAX = 100
MEMO = {}


def glass(gls1, gls2, capacity):
    """
    グラスに水を注ぐ
    """
    next_gls1, next_gls2 = gls1, gls2

    if gls1 > 0 and gls2 < capacity:
        if gls1 > capacity - gls2:
            next_gls1 -= capacity - gls2
            next_gls2 = capacity
        else:
            next_gls1 = 0
            next_gls2 += gls1

    return next_gls1, next_gls2


def check(pattern, capacities):
    """
    最初の半分になったかチェック
    """
    next_g = []

    for glasses in pattern:
        gls1, gls2, gls3 = glasses[0], glasses[1], glasses[2]

        if (gls1, gls2, gls3) not in MEMO:
            MEMO[(gls1, gls2, gls3)] = True

            if gls1 == capacities[0]/2:
                return 1

            next_g1, next_g2 = glass(gls1, gls2, capacities[1])
            next_g += [[next_g1, next_g2, gls3]]

            next_g1, next_g3 = glass(gls1, gls3, capacities[2])
            next_g += [[next_g1, gls2, next_g3]]

            next_g2, next_g1 = glass(gls2, gls1, capacities[0])
            next_g += [[next_g1, next_g2, gls3]]

            next_g2, next_g3 = glass(gls2, gls3, capacities[2])
            next_g += [[gls1, next_g2, next_g3]]

            next_g3, next_g1 = glass(gls3, gls1, capacities[0])
            next_g += [[next_g1, gls2, next_g3]]

            next_g3, next_g2 = glass(gls3, gls2, capacities[1])
            next_g += [[gls1, next_g2, next_g3]]

    if not next_g:
        return 0

    return check(next_g, capacities)


CNT = 0
for A in range(MIN, MAX+1):
    if A % 2 == 0:
        for B in range(A-1, A//2, -1):
            C = A - B
            F = True

            for i in range(2, C+1):
                if B % i == 0 and C % i == 0:
                    F = False

            if F:
                MEMO = {}

                if check([[A, 0, 0]], [A, B, C]):
                    print("( A, B, C ) = (", A, ",", B, ",", C, ")")
                    CNT += 1

print("result =", CNT)

"""Q43
"""
N = 5
START = [i for i in range(1, 2*N+1)]
GOAL = START[::-1]


def shufful(card, ini):
    """
    シャッフル
    """
    tmp1 = card[:]
    tmp2 = card[ini:ini+N]

    del tmp1[ini:ini+N]

    return tmp1[:] + tmp2[:]


def reverse_shufful(card, ini):
    """
    逆シャッフル
    """
    tmp1 = card[0:ini]
    tmp2 = card[-N:]
    tmp3 = card[ini:-N]

    return tmp1[:] + tmp2[:] + tmp3[:]


def search(start_cards, end_cards, start_depth, end_depth):
    """
    探索
    """
    # 開始側から探索
    next_start_cards = []

    for start in start_cards:
        for i in range(N):
            tmp = shufful(start, i)
            next_start_cards += [tmp]

    for start in next_start_cards:
        if start in end_cards:
            return start_depth + 1 + end_depth

    # 終了側から探索
    next_end_cards = []

    for end in end_cards:
        for i in range(N):
            tmp = reverse_shufful(end, i)
            next_end_cards += [tmp]

    for start in next_start_cards:
        if start in next_end_cards:
            return start_depth + 1 + end_depth + 1

    return search(next_start_cards, next_end_cards, start_depth + 1, end_depth + 1)


print(search([START], [GOAL], 0, 0))

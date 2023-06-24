"""Q54
"""
N = 11


def search(cards, num):
    """
    探索
    """
    if num == 0:
        return 1

    cnt = 0

    for i, j in enumerate(cards):
        if j == 0 and i + num + 1 < len(cards) and cards[i + num + 1] == 0:
            cards[i] = cards[i + num + 1] = num
            cnt += search(cards, num - 1)
            cards[i] = cards[i + num + 1] = 0

    return cnt


print(search([0] * (N * 2), N))

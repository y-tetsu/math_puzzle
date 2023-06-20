"""Q23
"""

C = 10
G = 24


def blackjack(coin, game):
    """
    ブラックジャック
    """
    if coin <= 0:
        return 0
    if coin >= 1 and game >= G:
        return 1
    cnt = 0
    cnt += blackjack(coin + 1, game + 1)
    cnt += blackjack(coin - 1, game + 1)
    return cnt


if __name__ == "__main__":
    print("cnt =", blackjack(C, 0))

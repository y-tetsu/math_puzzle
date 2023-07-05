"""Q51
"""


def solve():
    """解答
    """
    cnt = 0
    for i in range(1, 101):
        cnt += perfect_shuffle(i)
    print('cnt =', cnt)


def perfect_shuffle(num):
    """2*(num-1)回のシャッフルでもとにもどるかどうか返す
    """
    cards = [i for i in range(1, 2 * num + 1)]
    goal = cards[:]
    for _ in range(2 * (num - 1)):
        tmp = []
        for i in range(num):
            tmp += [cards[i], cards[i + num]]
        cards = tmp[:]
    return 1 if cards == goal else 0


if __name__ == '__main__':
    solve()

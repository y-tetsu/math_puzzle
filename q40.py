"""Q40
"""
import itertools


def solve():
    """解答
    """
    MAX_CNT = 0
    MAX_CARD = [i for i in range(1, 10)]
    for i in itertools.permutations([1, 2, 3, 4, 5, 6, 7, 8, 9], 9):
        card = list(i)
        pre_card = card[:]
        cnt = 0
        while True:
            if card[0] == 1:
                break
            card[:card[0]] = card[card[0]-1::-1]
            cnt += 1
        if cnt > MAX_CNT:
            MAX_CNT = cnt
            MAX_CARD = pre_card[:]
    print(', '.join([str(i) for i in MAX_CARD]))


if __name__ == '__main__':
    solve()

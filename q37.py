#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Q37
"""

RESULT, MEMO = {}, {}


def main():
    """
    全通りチェック
    """
    for i in range(1, 7):
        for j in range(1, 7):
            for k in range(1, 7):
                for l in range(1, 7):
                    for m in range(1, 7):
                        for n in range(1, 7):
                            dice = [i, j, k, l, m, n]
                            if tuple(dice) not in MEMO:
                                check_loop(dice, [])

    print(len(RESULT.keys()))


def check_loop(dice, step):
    """
    ループが存在するか判定

    """
    global RESULT, MEMO
    MEMO[tuple(dice)] = True

    # ループ発見時
    if dice in step:
        for i in step:
            if i != dice:
                RESULT[tuple(i)] = True
            else:
                break

    # ループ未発見時
    else:
        next_dice = dice[dice[0]:len(dice)]

        for i in range(dice[0]):
            next_dice += [7 - dice[i]]

        check_loop(next_dice, step + [dice])


if __name__ == '__main__':
    main()

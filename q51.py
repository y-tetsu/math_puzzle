#!/usr/bin/env/ python
# -*- coding: utf-8 -*-
"""
Q51
"""


def perfect_shuffle(num):
    """
    2*(num-1)回でもとにもどるかチェックする
    """
    cards = [i for i in range(1, 2 * num + 1)]
    goal = cards[:]

    for _ in range(1, 2 * (num - 1) + 1):
        tmp = []

        for i in range(num):
            tmp += [cards[i], cards[i + num]]

        cards = tmp[:]

    return 1 if cards == goal else 0


def check():
    """
    1から100まで求める
    """
    cnt = 0

    for i in range(1, 101):
        cnt += perfect_shuffle(i)

    return cnt


if __name__ == '__main__':
    print("result =", check())

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Q52
"""

import itertools

N = 8


class Hourglass:
    """
    砂時計
    """
    def __init__(self, minute):
        self.minute = minute
        self.remain = minute

    def count_down(self):
        """
        時間経過
        """
        if self.remain > 0:
            self.remain -= 1

            if self.remain == 0:
                return 1

        return 0

    def upset(self):
        """
        ひっくり返す
        """
        self.remain = self.minute - self.remain


def check(pattern):
    """
    砂時計が同時に落ちるかチェック
    """
    hourglasses = []

    # 砂時計を準備
    for i in pattern:
        hourglasses += [Hourglass(i)]

    memo = {}
    ret = 0
    loop = True

    while loop:
        # 砂時計を一周する
        for i in range(len(pattern)):
            # 確認済みの状態か
            tpl = tuple([i] + [j.remain for j in hourglasses])

            if tpl in memo:
                loop = False
                break
            else:
                memo[tpl] = True

            # 1分経過
            cnt = 0

            for j in hourglasses:
                cnt += j.count_down()

            # すべての砂が同時に落ちた
            if cnt == len(hourglasses):
                ret = 1
                loop = False
                break

            # ひっくり返す
            for offset in range(hourglasses[i].minute):
                hourglasses[(i + offset) % len(hourglasses)].upset()

    return ret


if __name__ == '__main__':
    CNT = 0

    for ptn in itertools.permutations([i + 1 for i in range(N)]):
        CNT += check(ptn)

    print("result =", CNT)

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
        self.capacity = self.remain = minute

    def count_down(self):
        """
        1分経過 & 空になったら通知
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
        self.remain = self.capacity - self.remain


def check(pattern):
    """
    砂時計が同時に落ちるかチェック
    """
    hourglasses = [Hourglass(i) for i in pattern]
    memo = {}
    ret = 0
    loop = True

    while loop:
        # 砂時計を一周する
        for i in range(len(pattern)):
            tpl = tuple([i] + [j.remain for j in hourglasses])

            # 確認済みの状態か
            if tpl in memo:
                loop = False
                break
            else:
                # 今回のパターンを記憶する
                memo[tpl] = True

                # 1分経過
                cnt = sum([j.count_down() for j in hourglasses])

                # すべての砂が同時に落ちた
                if cnt == len(hourglasses):
                    ret = 1
                    loop = False
                    break
                else:
                    # ひっくり返す
                    for offset in range(hourglasses[i].capacity):
                        hourglasses[(i + offset) % len(hourglasses)].upset()

    return ret


if __name__ == '__main__':
    CNT = 0

    for ptn in itertools.permutations([i + 1 for i in range(N)]):
        CNT += check(ptn)

    print("result =", CNT)

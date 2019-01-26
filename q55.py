#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Q55
"""

import itertools


class Soroban:
    """
    そろばん
    """
    memo = {}

    def __init__(self, digit):
        self.go_tama = [0] * digit
        self.ichi_tama = [0] * digit
        self.digit = digit
        self.move = 0

    def add(self, num):
        """
        値を足す
        """
        go_tama_tpl = tuple(self.go_tama)
        ichi_tama_tpl = tuple(self.ichi_tama)
        memo_key = tuple([go_tama_tpl, ichi_tama_tpl, num])

        if memo_key in Soroban.memo:
            self.go_tama, self.ichi_tama, move = Soroban.memo[memo_key]
            self.move += move

        else:
            next_go_tama = self.go_tama[:]
            next_ichi_tama = self.ichi_tama[:]
            move = 0

            div_num, mod_num = divmod(num, 5)

            # 1の位から足していく
            for i in range(self.digit):
                # 1の玉
                next_ichi_tama[i] += mod_num
                div_num += next_ichi_tama[i] // 5
                next_ichi_tama[i] = next_ichi_tama[i] % 5

                # 5の玉
                next_go_tama[i] += div_num
                mod_num = next_go_tama[i] // 2
                next_go_tama[i] = next_go_tama[i] % 2

                # 移動数
                move += abs(self.go_tama[i] - next_go_tama[i])
                move += abs(self.ichi_tama[i] - next_ichi_tama[i])

                # 次の位の準備
                div_num = 0

            self.go_tama = next_go_tama[:]
            self.ichi_tama = next_ichi_tama[:]
            self.move += move

            Soroban.memo[memo_key] = [self.go_tama, self.ichi_tama, move]

    def add_list(self, num_list):
        """
        リストの値をすべて足す
        """
        for i in num_list:
            self.add(i)

        return self.move


CNT = 0
LIST = []

for ptn in itertools.permutations([i + 1 for i in range(10)]):
    soroban = Soroban(2)
    cnt = soroban.add_list(ptn)

    if CNT == 0 or cnt < CNT:
        CNT = cnt
        LIST = ptn

print("result =", CNT, LIST)

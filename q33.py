#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Q33
"""

import csv
import re


def dup(key, pattern):
    """
    重複チェック
    """
    count = 0

    for i in pattern:
        if re.match(key, i):
            count += 1

            if count > 1:
                return True

    return False


def countlen(array):
    """
    最小文字数のカウント
    """
    cnt = 0

    for i in array:
        index = 0
        check = i[index]

        while dup(check, array):
            index += 1
            check += i[index]

        print(check, " : ", i)
        cnt += len(check)

    return cnt


def main():
    """
    CSV読み込み
    """
    csvfile = open('./q33.csv', 'r', encoding='utf-8')
    reader = csv.reader(csvfile)
    _ = next(reader)  # ヘッダーを捨てる

    kaminoku, simonoku = [], []

    for row in reader:
        kaminoku += [row[3]]
        simonoku += [row[4]]

    print(countlen(kaminoku) + countlen(simonoku))


if __name__ == "__main__":
    main()

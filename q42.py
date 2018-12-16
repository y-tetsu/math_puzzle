#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Q42
"""

import itertools

N = 1234
E = ['+', '-', '*', '//']


def main():
    """
    全探索
    """
    length = 0
    loop = True

    while loop:
        length += 1

        for num in range(1, 10):
            ptn = [num for j in range(length)]

            for j in range(1, length):
                for index in itertools.combinations([l for l in range(1, length)], j):
                    for exp in itertools.product(E, repeat=len(index)):
                        form = formular(ptn, index, exp)
                        calc = eval(form)

                        if calc == N:
                            print("result =", length, ",", form, "=", calc)
                            loop = False


def formular(ptn, index, exp):
    """
    式を作る
    """
    form = str(ptn[0])
    for i in range(1, len(ptn)):
        if i in index:
            form += exp[index.index(i)] + str(ptn[i])
        else:
            form += str(ptn[i])
    return form


if __name__ == '__main__':
    main()

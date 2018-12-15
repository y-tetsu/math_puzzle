#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Q32
"""


def init_board(height, width):
    """
    盤面の初期化
    """
    print("h =", height, "w =", width)
    print()

    board = [[0 for i in range(width + 2)] for j in range(height + 2)]

    for i in range(width + 2):
        board[0][i] = board[height + 1][i] = -1

    for i in range(height + 2):
        board[i][0] = board[i][width + 1] = -1

    return board


def tatami(board, index):
    """
    畳の配置
    """
    # 畳がすべて敷き詰められた場合
    if sum(map(lambda x: x.count(0), board)) == 0:
        for i in range(1, len(board) - 1):
            string = ""

            for j in range(1, len(board[0]) - 1):
                # 横置き
                if board[i][j] == board[i][j + 1] or board[i][j] == board[i][j - 1]:
                    string += "-"

                # 縦置き
                if board[i][j] == board[i + 1][j] or board[i][j] == board[i - 1][j]:
                    string += "|"

            print(string)
        print()

        return 1

    cnt = 0
    for h_1 in range(1, len(board) - 1):
        for w_1 in range(1, len(board[0]) - 1):
            # 次の畳を置く
            flag = False

            for i in [[1, 0], [0, 1]]:
                w_2 = w_1 + i[0]
                h_2 = h_1 + i[1]

                if board[h_1][w_1] == 0 and board[h_2][w_2] == 0:
                    flag = True

                    cond1 = board[h_1 - 1][w_1 - 1] == board[h_1 - 1][w_1]
                    cond2 = board[h_1 - 1][w_1 - 1] == board[h_1][w_1 - 1]

                    if cond1 or cond2:
                        next_board = board[:]
                        next_board[h_1][w_1] = index
                        next_board[h_2][w_2] = index
                        cnt += tatami(next_board, index + 1)
                        next_board[h_1][w_1] = 0
                        next_board[h_2][w_2] = 0

            if flag:
                return cnt

    return cnt


print("Q1 result =", tatami(init_board(4, 7), 1), "\n")
print("Q2 result =", tatami(init_board(5, 6), 1), "\n")

#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Q34
"""

W = H = 9


def main():
    """
    探索
    """
    board = init_board(H, W)
    result = 0

    # 飛車の位置
    for h_h in range(1, H + 1):
        for h_w in range(1, W + 1):
            # 角の位置
            for k_h in range(1, H + 1):
                for k_w in range(1, W + 1):
                    if not(h_h == k_h and h_w == k_w):
                        result += kiki(board, h_h, h_w, k_h, k_w)
    print(result)


def init_board(height, width):
    """
    盤面の初期化
    """
    ret = [[0 for i in range(width + 2)] for j in range(height + 2)]

    for i in range(height + 2):
        ret[i][0] = ret[i][len(ret) - 1] = -1

    for i in range(width + 2):
        ret[0][i] = ret[len(ret) - 1][i] = -1

    return ret


def kiki(board, h_h, h_w, k_h, k_w):
    """
    利きのカウント
    """
    check = [i[:] for i in board]
    check[h_h][h_w] = -1
    check[k_h][k_w] = -1

    # 飛車
    for delta_h in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        next_h_h = h_h + delta_h[0]
        next_h_w = h_w + delta_h[1]

        while check[next_h_h][next_h_w] != -1:
            check[next_h_h][next_h_w] = 1
            next_h_h += delta_h[0]
            next_h_w += delta_h[1]

    # 角
    for delta_k in [[-1, -1], [-1, 1], [1, -1], [1, 1]]:
        next_k_h = k_h + delta_k[0]
        next_k_w = k_w + delta_k[1]

        while check[next_k_h][next_k_w] != -1:
            check[next_k_h][next_k_w] = 1
            next_k_h += delta_k[0]
            next_k_w += delta_k[1]

    return sum(map(lambda x: x.count(1), check))


if __name__ == '__main__':
    main()

"""Q24
"""
import itertools

BOARD = [1, 2, 3, 4, 5, 6, 7, 8, 9]
MEMO = {}


def solve():
    """解答
    """
    print('cnt =', strike(BOARD))


def strike(board):
    """ストラックアウト
    """
    if tuple(board) in MEMO:
        return MEMO[tuple(board)]
    if not board:
        return 1
    ptn = []
    for i in board:  # 1枚抜き
        ptn += [(i, 0)]
    for i in itertools.combinations(board, 2):  # 2枚抜き
        if i[0] == 5 or i[1] == 5:
            continue
        elif i[0] % 3 != 0 and i[0] + 1 == i[1] or i[0] + 3 == i[1]:
            ptn += [(i[0], i[1])]
    cnt = 0
    for i in ptn:  # ボールを投げる
        next_board = board[:]
        if i[0] in next_board:
            next_board.remove(i[0])
        if i[1] in next_board:
            next_board.remove(i[1])
        cnt += strike(next_board)
    MEMO[tuple(board)] = cnt
    return cnt


if __name__ == "__main__":
    solve()

"""Q67
"""
BLACK, WHITE, DUMMY = 1, 0, 2
W, H = 6, 5


def solve():
    """解答
    """
    puzzle = [WHITE] * W * H
    print('cnt =', search(puzzle, 0, 0))


def search(puzzle, x, y):
    """パズルの探索
    """
    # 次の探索マスをセット
    if x >= W:
        x, y = 0, y+1

    # 最後のマスまで来ていたら終了
    if y >= H:
        return 1

    # 現在のマスを白のままとして、次のマスを探索
    cnt = search(puzzle, x+1, y)

    # 現在のマスに黒をおいても縦横連続しない場合
    if not is_continuous(puzzle, x, y):

        puzzle[y*W+x] = BLACK  # 黒を置く

        # パズルが分断されていない場合、黒を置いて次のマスを探索
        if not is_separated(puzzle):
            cnt += search(puzzle, x+1, y)

        puzzle[y*W+x] = WHITE  # 白に戻す

    return cnt
def is_continuous(puzzle, x, y):
    """黒マス(1)が左か上に存在している
    """
    if x - 1 >= 0 and puzzle[y*W+(x-1)] == BLACK:
        return True
    if y - 1 >= 0 and puzzle[(y-1)*W+x] == BLACK:
        return True
    return False


def is_separated(puzzle):
    """黒マスが盤面を分断している
    """
    start = 0
    for i, value in enumerate(puzzle):
        if value == WHITE:
            start = i
            break
    else:
        return True
    # 白の数
    cnt1 = puzzle.count(WHITE)
    # 白の連続をDUMMYで埋めた数
    dummy = [i for i in puzzle]
    fill(puzzle, start, dummy, DUMMY)
    cnt2 = dummy.count(DUMMY)
    if cnt1 == cnt2:
        return False
    return True


def fill(puzzle, start, checked, value):
    """白の場合埋める
    """
    if checked[start] == WHITE:
        checked[start] = value
        y = start // W
        x = start % W
        # 上
        if y-1 >= 0:
            fill(puzzle, (y-1)*W+x, checked, value)
        # 下
        if y+1 < H:
            fill(puzzle, (y+1)*W+x, checked, value)
        # 左
        if x-1 >= 0:
            fill(puzzle, y*W+(x-1), checked, value)
        # 右
        if x+1 < W and checked[y*W+(x+1)] == WHITE:
            fill(puzzle, y*W+(x+1), checked, value)


if __name__ == '__main__':
    solve()

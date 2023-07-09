"""Q56
"""
M = 16
N = 12
MEMO = {}


def solve():
    """解答
    """
    print(cut_cake(1, M, N, 0, 0))


def cut_cake(turn, length, width, eat1, eat2):
    """ケーキを切る
    """
    key = tuple([turn, length, width, eat1, eat2])
    if key in MEMO:
        return MEMO[key]
    if length == 1 and width == 1:
        if turn:
            eat1 += 1
        else:
            eat2 += 1
        if eat1 == eat2:
            return 0
        return float('inf')
    tmp_cut_cnt = []
    if turn:
        # 縦に切る
        for i in range(1, length//2 + 1):
            tmp_cut_cnt += [width + cut_cake(0, length - i, width, eat1 + i * width, eat2)]
        # 横に切る
        for i in range(1, width//2 + 1):
            tmp_cut_cnt += [length + cut_cake(0, length, width - i, eat1 + i * length, eat2)]
    else:
        # 縦に切る
        for i in range(1, length//2 + 1):
            tmp_cut_cnt += [width + cut_cake(1, length - i, width, eat1, eat2 + i * width)]
        # 横に切る
        for i in range(1, width//2 + 1):
            tmp_cut_cnt += [length + cut_cake(1, length, width - i, eat1, eat2 + i * length)]
    MEMO[key] = min(tmp_cut_cnt)
    return MEMO[key]


if __name__ == '__main__':
    solve()

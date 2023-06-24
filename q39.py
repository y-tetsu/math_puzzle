"""Q39
"""
MEMO = {0: 0}

# 反転用マスク
MASK = [0 for i in range(16)]
for row in range(4):
    for col in range(4):
        MASK[row * 4 + col] = (0b1111 << (row * 4)) | (0b1000100010001 << col)


def solve():
    """解答
    """
    CNT = search([0], 0)
    print('cnt =', CNT)


def search(ptn, depth):
    """探索
    """
    # すべての初期状態が確認済み
    if len(MEMO) == 65536:
        return depth
    # 次のパターン
    next_ptn = []
    next_depth = depth + 1
    for i in ptn:
        for j in range(16):
            tmp = i ^ MASK[j]
            if tmp not in MEMO:
                MEMO[tmp] = next_depth
                next_ptn.append(tmp)
    return search(next_ptn, next_depth)


if __name__ == '__main__':
    solve()

"""Q27
"""
W, H = 6, 4
ROAD = [[0 for i in range(W + 3)] for j in range(H + 3)]


def solve():
    """解答
    """
    for w in range(W + 3):
        ROAD[0][w] = 9
        ROAD[H + 2][w] = 9
    for h in range(H + 3):
        ROAD[h][0] = 9
        ROAD[h][W + 2] = 9
    print("cnt =", search(0, 1, 1, {}))


def search(direc, width, height, memo):
    """探索
    """
    dirs = [[1, 0], [0, 1], [-1, 0], [0, -1]]
    # ゴールについた場合
    if (width, height) == (W + 1, H + 1):
        return 1
    # 次に進む場所
    cnt = 0
    for i in [direc, (direc + 1) % 4]:
        delta_w = width + dirs[i][0]
        delta_h = height + dirs[i][1]
        # 道から外れていない場合
        if ROAD[delta_h][delta_w] != 9:
            tmp = [(width, height), (delta_w, delta_h)]
            tmp.sort()
            # まだ通っていない場合
            if tuple(tmp) not in memo:
                memo[tuple(tmp)] = "Used"
                cnt += search(i, delta_w, delta_h, memo)
                memo.pop(tuple(tmp))
    return cnt


if __name__ == '__main__':
    solve()

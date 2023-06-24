"""Q50
"""
L = 5
W = 6


def max_route(pos_x, pos_y, horizontal, vertical):
    """
    全経路を探索し最長の移動距離を求める
    """
    length = len(horizontal) - 1
    width = len(vertical) - 1

    # 平行線上に3回以上移動
    if list(filter(lambda x: x >= 3, horizontal)):
        return 0

    # 垂直線上に3回以上移動
    if list(filter(lambda x: x >= 3, vertical)):
        return 0

    # ゴールに到着
    if pos_x == width and pos_y == length:
        total = sum(horizontal) + sum(vertical)
        return total

    # 次に進む
    max_total = 0
    if pos_x >= 0 and pos_y >= 0:
        if pos_x <= width and pos_y <= length:
            for delta_x, delta_y in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
                next_h = horizontal[:]
                next_v = vertical[:]

                if abs(delta_x) > 0:
                    next_h[pos_y] += 1
                if abs(delta_y) > 0:
                    next_v[pos_x] += 1

                next_x = pos_x + delta_x
                next_y = pos_y + delta_y
                total = max_route(next_x, next_y, next_h, next_v)

                if total > max_total:
                    max_total = total

    return max_total


def main(length, width):
    """
    最長の移動距離を求める
    """
    horizontal = [0 for i in range(length+1)]
    vertical = [0 for i in range(width+1)]

    ret = max_route(0, 0, horizontal, vertical)
    print("result =", ret, "cm")

    return ret


if __name__ == '__main__':
    main(L, W)

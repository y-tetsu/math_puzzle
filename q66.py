"""Q66
"""
H, W = 3, 4

PANNEL = [
          [
              [2, 2],
              [2, 2],
          ],
          [
              [3, 2],
              [2, 3],
          ],
          [
              [2, 3],
              [3, 2],
          ],
          [
              [3, 3],
              [3, 3],
          ],
      ]

def get_ptn(ary):
    if len(ary) < H*W:
        for i in range(len(PANNEL)):
            gen = get_ptn(ary + [i])

            for j in gen:
                if len(list(j)) == H*W:
                    yield j
    else:
        yield ary


def get_points(ptn):
    points = [[0 for _ in range(W+1)] for _ in range(H+1)]

    index = 0
    for h in range(H):
        for w in range(W):
            pannel = PANNEL[ptn[index]]
            for dh, dw in [(0, 0), (0, 1), (1, 0), (1, 1)]:
                points[h+dh][w+dw] += pannel[dh][dw]
            index += 1

    for h in range(H+1):
        for w in range(W+1):
            if 0 < h < H and 0 < w < W:
                points[h][w] -= 4
            elif 0 < h < H or 0 < w < W:
                points[h][w] -= 1

    return points

def is_onestroke(points):
    odd = 0
    for h in range(H+1):
        for w in range(W+1):
            if points[h][w] % 2:
                odd += 1
    if odd == 0 or odd == 2:
        return True
    return False

if __name__ == '__main__':
    CNT = 0
    for ptn in get_ptn([]):
        points = get_points(ptn)
        if is_onestroke(points):
            print("ptn", ptn)
            print("points", points)
            CNT += 1
    print("result =", CNT)

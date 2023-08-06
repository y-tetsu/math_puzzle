"""Q69
"""
import itertools

W, H = 6, 5
MAN, WOMAN = 0, 1


def solve():
    """解答
    """
    cnt = 0
    for ptn in itertools.combinations([i for i in range(W * H)], (W * H) // 2):
        seats = [MAN] * W * H

        for index in ptn:
            seats[index] = WOMAN

        if check(seats):
            cnt += 1

            if cnt % 10000 == 0:
                print(cnt)

    print("cnt =", cnt)


def check(seats):
    for index, value in enumerate(seats):
        w = index % W
        h = index // W

        for dw, dh in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            next_w = w + dw
            next_h = h + dh
            next_index = next_h * W + next_w

            if 0 <= next_w < W and 0 <= next_h < H:
                if seats[next_index] != value:
                    break
        else:
            return False

    return True


if __name__ == '__main__':
    solve()

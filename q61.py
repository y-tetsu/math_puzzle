"""Q61
"""
import itertools

M = 5
N = 4
TABLE = [i for i in range(M * N)]
COUNT = 0


def check(color, delete):
    """
    つながっているか
    """
    color.remove(delete)

    left, right, up, down = delete - 1, delete + 1, delete - M, delete + M

    if delete % M > 0 and left in color:
        check(color, left)
    if delete % M != M - 1 and right in color:
        check(color, right)
    if delete / M > 0 and up in color:
        check(color, up)
    if delete / M != N - 1 and down in color:
        check(color, down)


for i in itertools.combinations(TABLE, M * N // 2):
    BLUE = list(i)

    if 0 in BLUE:
        WHITE = list(set(TABLE) - set(BLUE))
        check(BLUE, BLUE[0])

        if not BLUE:
            check(WHITE, WHITE[0])

        if not WHITE:
            COUNT += 1

print("result =", COUNT)

"""Q68
"""
from functools import lru_cache

N = 12
EMPTY, OCCUPIED, WALL = 0, 1, 2
SEATS = [WALL] + [EMPTY] * (N//2) + [WALL] + [EMPTY] * (N//2) + [WALL]


def solve():
    """解答
    """
    print("cnt =", search(tuple(SEATS)))


@lru_cache(maxsize=None)
def search(tseats):
    seats = list(tseats)

    if seats.count(OCCUPIED) == N:
        return 1

    cnt = 0

    for index, value in enumerate(seats):
        if value == EMPTY:
            if seats[index-1] != OCCUPIED and seats[index+1] != OCCUPIED:
                seats[index] = OCCUPIED
                cnt += search(tuple(seats))
                seats[index] = EMPTY

    if not cnt:
        for index, value in enumerate(seats):
            if value == EMPTY:
                seats[index] = OCCUPIED
                cnt += search(tuple(seats))
                seats[index] = EMPTY

    return cnt


if __name__ == '__main__':
    solve()

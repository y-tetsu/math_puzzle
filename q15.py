"""Q15
"""

MAX_STEP = 10
MAX_MOVE = 3 + 1
A = 0
B = 1


def updown(pos_a, pos_b, route_a, route_b, person):
    """Aさんが階段を上り、Bさんが階段を下りる"""
    if person == A and pos_b - pos_a == 0:
        print("> A =", route_a, " B =", route_b)
        return 1
    if pos_b - pos_a < 0:
        return 0
    next_move = min(pos_b - pos_a, MAX_MOVE)
    cnt = 0
    for i in range(1, next_move+1):
        if person == A:
            next_pos = pos_a + i
            cnt += updown(next_pos, pos_b, route_a + [next_pos], route_b, B)
        else:
            next_pos = pos_b - i
            cnt += updown(pos_a, next_pos, route_a, route_b + [next_pos], A)
    return cnt


print("cnt =", updown(0, MAX_STEP, [0], [MAX_STEP], A))

"""Q49
"""
N = 8
S = int("1" * N + "0" * N, 2)
G1 = int("".join([str("10") for i in range(N)]), 2)
G2 = int("".join([str("01") for i in range(N)]), 2)


def check_s(num, starts, goals, memo, depth):
    """
    スタート状態を反転させる
    """
    if list(filter(lambda x: x in goals, starts)):
        return depth

    next_tables = []
    mask = (1 << (num*2)) - 1

    for table in starts:
        swap_mask = 0b111

        for _ in range(num*2):
            next_table = table ^ swap_mask

            if next_table not in memo[0]:
                memo[0][next_table] = True
                next_tables += [next_table]

            swap_mask = ((swap_mask << 1) | (swap_mask << 1) >> (num*2)) & mask

    return check_g(num, next_tables, goals, memo, depth + 1)


def check_g(num, starts, goals, memo, depth):
    """
    ゴール状態を反転させる
    """
    if list(filter(lambda x: x in goals, starts)):
        return depth

    next_goals = []
    mask = (1 << (num*2)) - 1

    for goal in goals:
        swap_mask = 0b111

        for _ in range(num*2):
            next_goal = goal ^ swap_mask

            if next_goal not in memo[1]:
                memo[1][next_goal] = True
                next_goals += [next_goal]

            swap_mask = ((swap_mask << 1) | (swap_mask << 1) >> (num*2)) & mask

    return check_s(num, starts, next_goals, memo, depth + 1)


if __name__ == '__main__':
    print("result =", check_s(N, [S], [G1, G2], [{}, {}], 0))

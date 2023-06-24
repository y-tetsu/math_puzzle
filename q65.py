"""Q65
"""
N = 12

START = [i for i in range(1, N)] + [0]
GOAL = [0] + [i for i in range(2, N)] + [1]
MEMO_S = {}
MEMO_G = {}


def throw_ball(person):
    """
    ボールを投げる
    """
    ret = []
    for num, _ in enumerate(person):
        if num < len(person)//2:
            for i in range(3):
                target = num + (len(person)//2-1) + i
                if len(person)//2 <= target < len(person):
                    if person[target] == 0:
                        tmp = [i for i in person]
                        tmp[num], tmp[target] = tmp[target], tmp[num]
                        ret.append(tmp)
        else:
            for i in range(3):
                target = num - (len(person)//2+1) + i
                if 0 <= target < len(person)//2:
                    if person[target] == 0:
                        tmp = [i for i in person]
                        tmp[num], tmp[target] = tmp[target], tmp[num]
                        ret.append(tmp)
    return ret


def search(start, goal, count):
    """
    探索
    """
    ret_start = []
    ret_goal = []

    # スタート側からの探索
    count += 1
    for i in start:
        for j in throw_ball(i):
            if j not in ret_start:
                if tuple(j) not in MEMO_S:
                    MEMO_S[tuple(j)] = 1
                    ret_start.append(j)

    for i in ret_start:
        if i in goal:
            return count

    # ゴール側からの探索
    count += 1
    for i in goal:
        for j in throw_ball(i):
            if j not in ret_goal:
                if tuple(j) not in MEMO_G:
                    MEMO_G[tuple(j)] = 1
                    ret_goal.append(j)

    for i in ret_start:
        if i in ret_goal:
            return count

    return search(ret_start, ret_goal, count)


if __name__ == '__main__':
    print("result =", search([START], [GOAL], 0))

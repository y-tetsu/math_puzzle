"""Q19
"""
MAX_STEP = 6
RESULT = []


def solve():
    """解答
    """
    n = 10
    while True:
        step = check(gen_group(n))
        if step >= MAX_STEP:
            print(n)
            # print("MAX_STEP =", step)
            # print()
            # print("[steps]")
            # for number in RESULT:
            #     print(number)
            # print("-----")
            break
        n += 1


def check(group):
    """最大何段階ですべて選べるか
    """
    ret = 0
    for i in group:
        tmp = friends(i, [], group, [i], 1)
        if tmp > ret:
            ret = tmp
    return ret


def friends(member, mlist, group, flist, depth):
    """何段階で選べるか
    """
    global RESULT
    # 約数を探す
    yakusuu = []
    for i in range(2, member):
        if member % i == 0:
            yakusuu += [i]
    # 同じ約数の友達を探す
    same = []
    kouho = list(set(group) - set(flist))
    for i in kouho:
        for j in yakusuu:
            if (i % j) == 0:
                same += [i]
                break
    if set(flist + same) == set(group):
        if depth == MAX_STEP:
            RESULT += [mlist[:]]
        return depth
    cnt = 0
    ret = 0
    for i in same:
        cnt = friends(i, mlist + [member], group, flist + same, depth + 1)
        if cnt > ret:
            ret = cnt
    return ret


def gen_group(num):
    """合成数を探す
    """
    ret = []
    for i in range(4, num + 1):
        for j in range(2, i):
            if i % j == 0:
                ret += [i]
                break
    return ret


if __name__ == '__main__':
    solve()

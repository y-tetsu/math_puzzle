"""Q45
"""
N = 3
T = [[-1 for i in range(N)] for j in range(N)]


def solve():
    """解答
    """
    print('cnt =', pattern(N, prime(N), [], T, 0))


def prime(digit):
    """N桁の素数
    """
    tmp = []
    for i in range(10**(digit-1), 10**digit):
        flg = True
        for j in range(2, i):
            if i % j == 0:
                flg = False
        if flg:
            tmp += [i]
    ret = {}
    for i in range(digit):
        for j in tmp:
            if i == 0:
                key = str(-1)
                if key not in ret:
                    ret[key] = [j]
                else:
                    ret[key] += [j]
            key = str(j//10**i)
            for _ in range(len(key) - (digit - i)):
                key = "0" + key
            if key not in ret:
                ret[key] = [j]
            else:
                ret[key] += [j]
    return ret


def pattern(digit, primes, used, table, depth):
    """パターンを作る
    """
    check = True
    for i in table:
        if -1 in i:
            check = False
    if check:
        value = ""
        for i in range(digit):
            value += str(table[i][digit-1])
        key = tuple([tuple(i) for i in table])
        if value in primes and int(value) not in used:
            return 1
        return 0
    cnt = 0
    if depth % 2 == 0:
        if table[depth//2][depth//2] == -1:
            key = ""
            for i in range(depth//2):
                key += str(table[depth//2][i])
            if key == "":
                key = str(-1)
            if key in primes:
                for i in primes[key]:
                    if i not in used:
                        next_table = [j[:] for j in table]
                        for k in range(digit):
                            next_table[depth//2][k] = str(i)[k]
                        next_used = used[:]
                        next_used += [i]
                        cnt += pattern(digit, primes, next_used, next_table, depth + 1)
    else:
        if table[depth//2+1][depth//2] == -1:
            key = ""
            for i in range(depth//2+1):
                key += str(table[i][depth//2])
            if key in primes:
                for i in primes[key]:
                    if i not in used:
                        next_table = [j[:] for j in table]
                        for k in range(digit):
                            next_table[k][depth//2] = str(i)[k]
                        next_used = used[:]
                        next_used += [i]
                        cnt += pattern(digit, primes, next_used, next_table, depth + 1)
    return cnt


if __name__ == '__main__':
    solve()

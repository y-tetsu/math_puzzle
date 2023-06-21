"""Q13
"""
import itertools


def solve():
    """解答
    """
    cnt = 0
    for (r, e, a, d, w, i, t, l, k, s) in itertools.permutations(range(10)):
        if r == 0 or w == 0 or t == 0 or s == 0:
            continue
        read = r * 1000 + e * 100 + a * 10 + d
        write = w * 10000 + r * 1000 + i * 100 + t * 10 + e
        talk = t * 1000 + a * 100 + l * 10 + k
        skill = s * 10000 + k * 1000 + i * 100 + l * 10 + l
        if read + write + talk == skill:
            cnt += 1
            print(f'({cnt})')
            print(f'read  = {read}')
            print(f'write = {write}')
            print(f'talk  = {talk}')
            print(f'skill = {skill}\n')
    print(f'cnt = {cnt}')


if __name__ == '__main__':
    solve()

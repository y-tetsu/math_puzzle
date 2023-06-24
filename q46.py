"""Q46
"""
import itertools

N = 7
C = 0

for i in itertools.permutations([i + 1 for i in range(N)]):
    ptn = list(i)
    cnt = 0

    for j in range(len(ptn)):
        k = ptn.index(j + 1)

        if j != k:
            ptn[j], ptn[k] = ptn[k], ptn[j]
            cnt += 1

    C += cnt

print("result =", C)

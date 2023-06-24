"""Q47
"""
import itertools

N = 4
MEMO = {}

for pattern in itertools.product([1, 0], repeat=N*N):
    count = []

    for col in range(N):
        count_row, count_col = 0, 0

        for row in range(N):
            count_row += pattern[col+row*N]
            count_col += pattern[col*N+row]

        count += [count_row, count_col]

    MEMO[tuple(count)] = 1 if tuple(count) not in MEMO else MEMO[tuple(count)] + 1

print(sum(filter(lambda x: x == 1, map(lambda x: MEMO[x], MEMO))))

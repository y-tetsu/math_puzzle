"""Q58
"""
N = 14
STATUS = [[N, 0, 0, 0]]
STEP = 0


while not [s for s in STATUS if s[1] == N]:
    NEXT_STATUS = []

    for s in STATUS:
        for b in range(s[1] + 1):
            for c in range(s[2] + 1):
                if s[2] > 0:
                    if s[0] - b - c + 1 >= 0:
                        NEXT_STATUS += [[s[0] - b - c + 1, s[1] + c, s[2] + b - 1, s[3] + 1]]

                if s[0] - b - c >= 0:
                    NEXT_STATUS += [[s[0] - b - c, s[1] + c, s[2] + b, s[3]]]

                if s[0] - b - c - 1 >= 0:
                    NEXT_STATUS += [[s[0] - b - c - 1, s[1] + c + 1, s[2] + b, s[3] + 1]]

    STATUS = [j for i, j in enumerate(NEXT_STATUS) if j not in STATUS and i == NEXT_STATUS.index(j)]
    STEP += 1

print(STEP)
print(min([i[3] for i in STATUS if i[1] == N]))

"""Q70
"""
W, H = 6, 4

GOAL = [
    0b000000000000111111111111,
    0b111111111111000000000000,
    0b000111000111000111000111,
    0b111000111000111000111000,
]

MEMO = {}


def check(patterns, depth):
    next_patterns = []

    for ptn in patterns:
        if ptn not in MEMO:
            MEMO[ptn] = depth

            # 横入替
            for h in range(H):
                for w in range(W - 1):
                    mask_bit1 = 0b1 << (h * W) + w
                    mask_bit2 = 0b1 << (h * W) + w + 1
                    mask_clear = ~(mask_bit1 | mask_bit2)

                    bit1_value = (ptn & mask_bit1) << 1
                    bit2_value = (ptn & mask_bit2) >> 1

                    next_ptn = (ptn & mask_clear) | bit1_value | bit2_value

                    if next_ptn not in MEMO:
                        next_patterns.append(next_ptn)

            # 縦入替
            for w in range(W):
                for h in range(H - 1):
                    mask_bit1 = 0b1 << (h * W) + w
                    mask_bit2 = 0b1 << ((h + 1) * W) + w
                    mask_clear = ~(mask_bit1 | mask_bit2)

                    bit1_value = (ptn & mask_bit1) << W
                    bit2_value = (ptn & mask_bit2) >> W

                    next_ptn = (ptn & mask_clear) | bit1_value | bit2_value

                    if next_ptn not in MEMO:
                        next_patterns.append(next_ptn)

    return next_patterns


if __name__ == '__main__':
    next_patterns = GOAL
    depth = 0

    while True:
        if next_patterns:
            next_patterns = check(next_patterns, depth)
            depth += 1
        else:
            break

    print("ptn = ", sum([1 for value in MEMO.values() if value == depth - 1]))
    print("max move =", depth - 1)

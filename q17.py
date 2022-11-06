"""Q17
"""
N = 30
BOY = 0
GIRL = 1


def lineup(seq):
    if len(seq) >= N:
        return 1
    cnt = lineup(seq + [BOY])
    if seq[-1] == BOY:
        cnt += lineup(seq + [GIRL])
    return cnt


if __name__ == '__main__':
    print("cnt =", lineup([BOY]) + lineup([GIRL]))

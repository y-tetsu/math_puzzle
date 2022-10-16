"""Q08
"""
N = 12


def move(num, log):
    """ロボット移動"""
    if len(log) == num + 1:
        return 1
    cnt = 0
    for delta in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
        next_pos = [log[-1][0] + delta[0], log[-1][1] + delta[1]]
        cnt += move(num, log + [next_pos]) if not (next_pos in log) else 0
    return cnt


if __name__ == '__main__':
    cnt = move(N, [[0, 0]])
    print(f'cnt = {cnt}')

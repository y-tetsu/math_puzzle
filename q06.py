"""Q05
"""


def is_loop(num):
    """ループしているかチェック"""
    val = num * 3 + 1
    while val not in (1, num):
        val = val // 2 if val % 2 == 0 else val * 3 + 1
    if val == num:
        print(f'{num} is loop')
        return 1
    return 0


if __name__ == '__main__':
    c = 0
    for i in range(2, 10001, 2):
        c += is_loop(i)
    print(f'result = {c}')

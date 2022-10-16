"""Q03
"""
N = 100  # カード枚数


if __name__ == '__main__':
    card = [False for i in range(N)]
    # カードを裏返す
    for i in range(1, N):
        for j in range(i, N, i+1):
            card[j] = not card[j]
    # 結果表示
    for i in range(0, N):
        if not card[i]:
            print(f'{i+1}')

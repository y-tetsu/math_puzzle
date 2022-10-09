"""Q01
"""
if __name__ == '__main__':
    n = 11
    while True:
        d, o, b = f'{n}', f'{n:o}', f'{n:b}'
        if d == d[::-1] and o == o[::-1] and b == b[::-1]:
            print(n)
            break
        n += 2

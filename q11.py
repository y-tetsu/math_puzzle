"""Q11
"""
if __name__ == '__main__':
    a = b = 1
    cnt = 0
    while cnt < 11:
        c = a + b
        if c % sum([int(i) for i in str(c)]) == 0:
            if cnt > 5:
                print(c)
            cnt += 1
        a, b = b, c

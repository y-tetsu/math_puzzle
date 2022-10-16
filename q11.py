"""Q11
"""
if __name__ == '__main__':
    a = b = 1
    count = 0
    while count < 11:
        c = a + b
        if c % sum([int(i) for i in str(c)]) == 0:
            if count > 5:
                print(c)
            count += 1
        a, b = b, c

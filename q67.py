"""Q67
"""
import itertools

W, H = 6, 5

def is_adjacent(ptn):
    for col in range(H):
        for row in range(W):
            if ptn[col * W + row] == "1":
                if col - 1 >= 0 and ptn[(col - 1) * W + row] == "1":
                    return True
                if col + 1 < H  and ptn[(col + 1) * W + row] == "1":
                    return True
                if row - 1 >= 0 and ptn[col * W + (row - 1)] == "1":
                    return True
                if row + 1 < W  and ptn[col * W + (row + 1)] == "1":
                    return True

def is_separated(ptn):
    start = 0
    for index, value in enumerate(ptn):
        if value == "0":
            start = index
            break
    else:
        return True

    cnt1 = ptn.count("0")
    cnt2 = check(ptn, start, [i for i in ptn])

    if cnt1 == cnt2:
        return False

    return True

def check(ptn, start, checked):
    checked[start] = "2"

    col = start // W
    row = start % W

    cnt1, cnt2, cnt3, cnt4 = 0, 0, 0, 0

    if col - 1 >= 0 and checked[(col - 1) * W + row] == "0":
        cnt1 = check(ptn, (col - 1) * W + row, checked)
    if col + 1 < H  and checked[(col + 1) * W + row] == "0":
        cnt2 = check(ptn, (col + 1) * W + row, checked)
    if row - 1 >= 0 and checked[col * W + (row - 1)] == "0":
        cnt3 = check(ptn, col * W + (row - 1), checked)
    if row + 1 < W  and checked[col * W + (row + 1)] == "0":
        cnt4 = check(ptn, col * W + (row + 1), checked)

    return checked.count("2")

if __name__ == '__main__':
    CNT = 0
    for ptn in itertools.product("01", repeat=W*H):
        if not is_adjacent(ptn):
            if not is_separated(ptn):
                CNT += 1
                print(CNT)
    print("result =", CNT)

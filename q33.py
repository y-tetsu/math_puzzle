"""Q33
"""
import re
import csv


def solve():
    """解答
    """
    csvfile = open('./q33.csv', 'r', encoding='utf-8')
    reader = csv.reader(csvfile)
    _ = next(reader)  # ヘッダーを捨てる
    kaminoku, simonoku = [], []
    for row in reader:
        kaminoku += [row[3]]
        simonoku += [row[4]]
    print(countlen(kaminoku) + countlen(simonoku))


def dup(key, pattern):
    """重複チェック
    """
    count = 0
    for i in pattern:
        if re.match(key, i):
            count += 1
            if count > 1:
                return True
    return False


def countlen(array):
    """最小文字数のカウント
    """
    cnt = 0
    for i in array:
        index = 0
        check = i[index]
        while dup(check, array):
            index += 1
            check += i[index]
        print(check, " : ", i)
        cnt += len(check)
    return cnt


if __name__ == "__main__":
    solve()

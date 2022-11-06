"""Q16
"""
import itertools


if __name__ == '__main__':
    n = 500
    ret = []
    for i in range(1, int(n/4) + 1):
        edge = list(map(lambda x: x*(2*i-x), [j for j in range(1, i)]))
        for k in itertools.combinations(edge, 2):
            if k[0] + k[1] == pow(i, 2):
                ret.append(str(float(k[1]/k[0])) + "," + str(float(i*i/k[0])))
    print("cnt =", len(set(ret)))  # 重複を削除し要素数を返す

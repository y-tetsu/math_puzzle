"""Q29
"""
N = 10
RESISTERS = [i for i in range(1, N + 1)]  # 使う抵抗のリスト(1～N)
GOAL = 1.6180339887
CIRCUIT = {}  # 抵抗接続のリスト、接続先がないものは終端に接続と判断する


def solve():
    """解答
    """
    print("{0:.10f}".format(connect(0, CIRCUIT, RESISTERS)))  # num=0は開始点とする


def connect(num, circuit, usable):
    """抵抗の接続パターン
    """
    ret = 0
    # 現在の抵抗に対して何個並列の抵抗を直列につなぐか
    for i in range(1, len(usable) + 1):
        circuit[num] = usable[0:i]
        # すべての抵抗接続済み
        if not usable[i:]:
            # 抵抗値を計算し誤差最小を記憶
            res = calc(circuit, 0)
            ret = res if abs(GOAL - res) < abs(GOAL - ret) else ret
        # 並列抵抗それぞれの次の接続
        else:
            for j in usable[0:i]:
                res = connect(j, circuit, usable[i:])
                ret = res if abs(GOAL - res) < abs(GOAL - ret) else ret
        circuit.pop(num)
    return ret


def calc(circuit, num):
    """抵抗値の計算
    """
    parallel = [1 for i in circuit[num]]
    # 直列の計算
    cnt = 0
    for i in circuit[num]:
        # 接続先が存在する場合は加算
        parallel[cnt] += calc(circuit, i) if i in circuit else 0
        cnt += 1
    # 並列の計算
    ret = 1 / sum(map(lambda x: float(1 / x), parallel)) if len(parallel) > 1 else parallel[0]
    return ret


if __name__ == '__main__':
    solve()

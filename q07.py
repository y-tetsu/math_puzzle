"""Q07
"""
import datetime


def solve():
    """解答
    """
    date1 = '19641010'  # 開始年月日
    date2 = '20200724'  # 終了年月日
    datet1 = datetime.datetime.strptime(date1, '%Y%m%d')
    while True:
        d1_text = datet1.strftime('%Y%m%d')
        d1_dec = int(d1_text)            # 文字列を10進数に変換
        d1_bin = format(d1_dec, '025b')  # 10進数を2進数に変換
        d1_binr = d1_bin[::-1]           # 並び替える
        d1_decr = int(d1_binr, 2)        # 2進数を10進数に変換
        if d1_dec == d1_decr:
            print(f'{d1_text} : {d1_bin}')
        if d1_text == date2:
            break
        datet1 += datetime.timedelta(days=1)


if __name__ == '__main__':
    solve()

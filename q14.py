"""Q14
"""
COUNTRIES = [
    'Brazil', 'Cameroon', 'Chile', 'Greece', 'Uruguay',
    'Italy', 'France', 'Bosnia and Heregovina', 'Gernany', 'USA',
    'Russia', 'Croatia', 'Spain', 'Australia', "Cote d'lvoire",
    'Costa Rica', 'Switzerland', 'Honduras', 'Iran', 'Portugal',
    'Belgium', 'Korea Republic', 'Mexico', 'Netherlands', 'Colombia',
    'Japan', 'England', 'Ecuador', 'Agentina', 'Nigeria',
    'Ghana', 'Algeria',
]


def search(key, keys, buf):
    """最大しりとりを取得"""
    max_shiritori = [i for i in buf]
    for next_key in keys:
        if not key or key[-1].upper() == next_key[0].upper():
            buf.append(next_key)
            s = search(next_key, [i for i in keys if i != next_key], buf)
            buf.pop()
            if len(s) > len(max_shiritori):
                max_shiritori = [i for i in s]
    return max_shiritori


if __name__ == '__main__':
    s = search('', COUNTRIES, [])
    print(f'cnt = {len(s)} : {s}')

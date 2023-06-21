# math_puzzle
「プログラマ脳を鍛える数学パズル シンプルで高速なコードが書けるようになる70問」をPythonで解く

## 目標
- Pythonらしいシンプルで読みやすい**Pythonic**なコードを目指す
- 標準ライブラリを活用してなるべく楽をする
- flake8準拠とする

## 動作確認バージョン
Python 3.7.6

## 使用する標準ライブラリ
| 名称 | 用途 | 使用箇所 |
|---|---|---|
|re |[正規表現操作](https://docs.python.org/ja/3/library/re.html) | [Q02](https://github.com/y-tetsu/math_puzzle/blob/master/q02.py), [Q12](https://github.com/y-tetsu/math_puzzle/blob/master/q12.py), [Q33](https://github.com/y-tetsu/math_puzzle/blob/master/q33.py) |
|itertools |[効率的なループ実行のためのイテレータ生成関数](https://docs.python.org/ja/3/library/itertools.html) | [Q02](https://github.com/y-tetsu/math_puzzle/blob/master/q02.py), [Q05](https://github.com/y-tetsu/math_puzzle/blob/master/q05.py), [Q13](https://github.com/y-tetsu/math_puzzle/blob/master/q13.py), [Q16](https://github.com/y-tetsu/math_puzzle/blob/master/q16.py), [Q20](https://github.com/y-tetsu/math_puzzle/blob/master/q20.py), [Q24](https://github.com/y-tetsu/math_puzzle/blob/master/q24.py), [Q28](https://github.com/y-tetsu/math_puzzle/blob/master/q28.py) |
|datetime |[基本的な日付型および時間型](https://docs.python.org/ja/3/library/datetime.html) | [Q07](https://github.com/y-tetsu/math_puzzle/blob/master/q07.py) |
|decimal |[十進固定及び浮動小数点数の算術演算](https://docs.python.org/ja/3/library/decimal.html) | [Q12](https://github.com/y-tetsu/math_puzzle/blob/master/q12.py) |
|math |[数学関数](https://docs.python.org/ja/3/library/math.html) | [Q18](https://github.com/y-tetsu/math_puzzle/blob/master/q18.py) |
|pprint |[データ出力の整然化](https://docs.python.org/ja/3/library/pprint.html) | [Q18](https://github.com/y-tetsu/math_puzzle/blob/master/q18.py) |
|csv |[CSV ファイルの読み書き](https://docs.python.org/ja/3/library/csv.html) | [Q33](https://github.com/y-tetsu/math_puzzle/blob/master/q33.py) |
|functools |[高階関数と呼び出し可能オブジェクトの操作](https://docs.python.org/ja/3/library/functools.html) | |

※サードパーティー製のライブラリは使用していません

## 参考書籍
- 「プログラマ脳を鍛える数学パズル シンプルで高速なコードが書けるようになる70問」 増井 敏克著 株式会社翔泳社 [ISBN978-4-7981-4245-6](https://books.google.co.jp/books?id=dnzCCgAAQBAJ&pg=PA312&lpg=PA312&dq=ISBN978-4-7981-4245-6&source=bl&ots=AQYxdf9F9_&sig=ACfU3U0SOUkmrUcqSzOTBvrRH-gMlJ1wnA&hl=ja&sa=X&ved=2ahUKEwjXifW54eLpAhWTEqYKHQ9CBogQ6AEwAXoECAkQAQ#v=onepage&q=ISBN978-4-7981-4245-6&f=false)

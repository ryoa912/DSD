# @title ch10-ex01
# 現在の日付をtoday.txtというテキストファイルに文字列の形で書き込もう。
import datetime
import os
with open(os.path.dirname(__file__) + os.sep + 'today.txt', 'wt') as fout:
    print(datetime.date.today().isoformat(), file=fout)

# result:
# 2019-10-30

# memo:
# ・実行しているファイルが格納されているディレクトリのパスを取得したい
# ⇒参考：https://qiita.com/neko_the_shadow/items/09ff3a423954a2adfe18
# ・ディレクトリ区切り文字は/で良いのか...
# ⇒os.sepを使えば良い
# 　参考：https://python-izm.com/advanced/separator/

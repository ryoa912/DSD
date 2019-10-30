# @title ch10-ex01
# 現在の日付をtoday.txtというテキストファイルに文字列の形で書き込もう。
import datetime
import os.path
fout = open(os.path.dirname(__file__) + '/' + 'today.txt', 'wt')
print(datetime.date.today(), file=fout)
fout.close()

# result:
# 2019-10-30

# memo:
# ディレクトリ区切り文字は/で良いのか...

# @title ch10-ex02
# テキストファイルtoday.txtの内容をtoday_stringという文字列変数に読み込もう。
import os
with open(os.path.dirname(__file__) + os.sep + 'today.txt', 'rt') as fin:
    today_string = fin.read()
print('today_string: ' + today_string)

# result:
# today_string: 2019-10-30

# memo:
# 巨大なファイルをチャンクを使わずにread()したらどうなるのか

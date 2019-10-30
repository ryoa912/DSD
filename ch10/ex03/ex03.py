# @title ch10-ex03
# today_stringから日付を解析して取り出そう。
import time
import os
with open(os.path.dirname(__file__) + os.sep + 'today.txt', 'rt') as fin:
    today_string = fin.read()
print(time.strptime(today_string, '%Y-%m-%d\n'))

# result:
# time.struct_time(tm_year=2019, tm_mon=10, tm_mday=30, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=303, tm_isdst=-1)

# memo:
# ・読み込んだファイルに改行が含まれているため、フォーマットにも改行文字を入れないとエラーになる
# ・today_stringがwith節の中で定義されているのに、外で使えるのが違和感。
# ⇒外で同じ名前の変数が定義されていたら、そちらが優先される。

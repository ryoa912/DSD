# @title ch10-ex04
# カレントディレクトリのファイルのリストを作ろう。
import os
files = []
path = os.path.dirname(__file__)
for ｆ in os.listdir(path):
    if os.path.isfile(path + os.sep + f):
        files.append(f)

print(files)

# result:
# ['01.txt', '02.txt', '03.txt', 'ex04.py']

# memo:
# ・os.listdir('フォルダパス')だと、ファイルに加えてフォルダもリストに含まれてしまう
# ⇒ファイルかどうか判定してやる必要がある
# https://qiita.com/Morio/items/f34dab8825c9d76664f5

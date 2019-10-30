# @title ch10-ex05
# 親ディレクトリのファイルのリストを作ろう。
import os
files = []
path = os.path.dirname(__file__) + os.sep + '..'
for ｆ in os.listdir(path):
    if os.path.isfile(path + os.sep + f):
        files.append(f)

print(files)

# result:
# ['file_for_ex05.txt']

# memo:
# '..' を使うことで、親ディレクトリにさかのぼれる
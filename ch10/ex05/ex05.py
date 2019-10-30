# @title ch10-ex05
# 親ディレクトリのファイルのリストを作ろう。
import os
path = os.path.dirname(__file__) + os.sep + '..'
files = [file for file in os.listdir(path)
         if os.path.isfile(path + os.sep + file)]

print(files)

# result:
# ['file_for_ex05.txt']

# memo:
# '..' を使うことで、親ディレクトリにさかのぼれる

# @title ch10-ex06
# multiprocessingを使って3個の別々のプロセスを作ろう。
# それぞれを1秒から5秒のランダムな秒数だけ眠らせよう。
import multiprocessing


def timer(seconds):
    import datetime
    import time
    time.sleep(seconds)
    print('alerm! now:', datetime.datetime.utcnow())


if __name__ == '__main__':
    import random
    for n in range(3):
        seconds = random.randint(1, 5)
        proc = multiprocessing.Process(target=timer, args=(seconds,))
        proc.start()
# result:
# alerm! now: 2019-10-30 02:09:26.917144
# alerm! now: 2019-10-30 02:09:28.909699
# alerm! now: 2019-10-30 02:09:28.920056

# memo:
# ・python3 + VSC でデバッグ実行
# ⇒https://www.atmarkit.co.jp/ait/articles/1806/05/news023.html
# ・ランダムな整数を範囲指定で取得する方法
# ⇒https://note.nkmk.me/python-random-randrange-randint/
# ・args=([引数],)と記載しているのは、タプルであることを明示するため
# 　タプル、リストを渡せばOK.単一のintなどを渡すとエラー. (引数)だけだとタプルと見なされない

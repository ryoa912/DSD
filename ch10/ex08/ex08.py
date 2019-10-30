# @title ch10-ex08
# あなたの誕生日は何曜日だったか
import datetime
birthday = datetime.date(1988, 9, 12)
print(birthday.isoweekday())

# result:
# 1(月曜日)

# memo:
# isoweekday()では、1が月曜日、7が日曜日になる

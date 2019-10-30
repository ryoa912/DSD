# @title ch10-ex09
# 生まれてから10,000日になるのはいつか（あるいはいつだったか）
import datetime
day_after_10000 = datetime.date(1988, 9, 12) + datetime.timedelta(days=10000)
print(day_after_10000)
print(day_after_10000.isoweekday())

# result:
# 2016-01-29
# 5(金曜日)

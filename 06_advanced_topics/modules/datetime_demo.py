import datetime as dt
from datetime import datetime, date, time, timedelta

"""
datetime 模块演示
"""

print('\n----------- 日期的构造 -----------')

today = date.today()
print(today)

d = dt.date(1992, 12, 1)
print(d)

print('\n----------- 单独获取年月日 -----------')
print(today.year)
print(today.month)
print(today.day)

print('\n----------- 返回星期几 -----------')
print(f'{d.weekday()} ---- 注意：0 表示星期一')
print(f'{d.isoweekday()} ---- 注意：1 表示星期一')

print('\n----------- 日期格式化 -----------')
print('以 yyyy-MM-dd 格式显示：')
print(d.isoformat())
print(d.strftime('%Y-%m-%d'))

print('\n----------- 其他日期格式 -----------')
print(d.isocalendar())  # 一个元组
print(d.ctime())

print('\n----------- 替换年份、月份、日期生成一个新日期 -----------')
e = d.replace(year=2023, month=9)
print(e)

print('\n----------- 指定时、分、秒、微秒 -----------')
t = time(18, 50, 12, 2)
print(t)
print(f'时：{t.hour}')
print(f'分：{t.minute}')
print(f'秒：{t.second}')
print(f'微妙：{t.microsecond}')

print('\n----------- 时间的格式化输出 -----------')
print(t.isoformat())
print(t.strftime('%H:%M:%S:%f'))

print('\n----------- 替换小时、分钟、秒生成一个新时间 -----------')
print(t.replace(7, 7, 7))

print('\n----------- 构造日期和时间 -----------')

now = datetime.now()
print(now)

date_and_time = dt.datetime(2023, 9, 16, 18, 56, 22, 346812)
print(date_and_time)

print('\n----------- 单独构造日期和时间，再结合成 datetime -----------')
d = date(2023, 9, 16)
t = time(6, 6, 6, 6)
d_and_t = datetime.combine(d, t)
print(d_and_t)

print('\n----------- datetime 的格式化输出 -----------')
print(d_and_t.isoformat())
print(d_and_t.strftime("%Y-%m-%d %H:%M:%S:%f"))

print('\n----------- 替换年、月、日、小时、分钟、秒生成一个新时间 -----------')
print(d_and_t.replace(year=2030, month=1))

print('\n----------- 时间差 - timedelta -----------')
delta = timedelta(days=1, hours=4)
yesterday = datetime.now() - delta
print(yesterday)

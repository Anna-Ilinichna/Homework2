from datetime import datetime, timedelta

dt_now = datetime.now()
print(dt_now)

delta = timedelta(days=1)
yesterday= dt_now - delta
print(yesterday)

delta_2 = timedelta(days=30)
month_before = dt_now - delta_2
print(month_before)

date_string = '01/01/17 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%m/%d/%y %H:%M:%S.%f')
print(date_dt)
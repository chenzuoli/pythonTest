from croniter import croniter, croniter_range
from datetime import datetime, timedelta, timezone, date
import time

schedule_interval = '0 8 * * * '
cron = croniter(schedule_interval, datetime.now())
print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(cron.get_prev())))
print(type(cron.get_current()))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(cron.get_current())))
print(time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(cron.get_next())))
print("--------")
print(cron.get_prev())
print(cron.get_current())
print(cron.get_next())
print(datetime.fromtimestamp(cron.get_prev(), tz=timezone.utc))
print(datetime.fromtimestamp(cron.get_current(), tz=timezone.utc))
print(datetime.fromtimestamp(cron.get_next(), tz=timezone.utc))
print(datetime.fromtimestamp(cron.get_prev(), tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.fromtimestamp(cron.get_current(), tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.fromtimestamp(cron.get_next(), tz=timezone.utc).strftime('%Y-%m-%d %H:%M:%S'))
print("=====")
dt = datetime.fromtimestamp(cron.get_current(), tz=timezone.utc) - timedelta(days=2)
print(dt)

print(date.today() + timedelta(days=-1))
print(datetime.now() + timedelta(days=-1))

print("=========croniter_range========")
# tomorrow = datetime.strptime((datetime.now() + timedelta(days=2)).strftime('%Y-%m-%d %H:%M:%S'),
#                              "%Y-%m-%d %H:%M:%S")
# for run_time in croniter_range(datetime.now(), tomorrow, "01 */2 * * *"):
#     print(type(run_time))
#     print(run_time)


yesterday = datetime.strptime((datetime.now() + timedelta(days=-1)).strftime('%Y-%m-%d %H:%M:%S'),
                              "%Y-%m-%d %H:%M:%S")
for run_time in croniter_range(datetime.now(), yesterday, "01 */2 * * *"):
    print(type(run_time))
    print(run_time)

print("=========")
schedule_interval = '0 8 * * * '
cron = croniter(schedule_interval, datetime.now())
import pytz

for i in range(10):
    get_prev = cron.get_prev()
    tz = pytz.timezone('Asia/Shanghai')
    print(get_prev)
    print(datetime.fromtimestamp(get_prev, tz=timezone.utc))


import time
import datetime, pytz

print(datetime.datetime.now(pytz.timezone('US/Central')).strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.datetime.now(pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S'))
print(datetime.datetime.now(pytz.timezone('UTC')).strftime('%Y-%m-%d %H:%M:%S'))

print(datetime.datetime.fromtimestamp(1632833354110/1000, pytz.timezone('Asia/Shanghai')).strftime('%Y-%m-%d %H:%M:%S'))

tz = pytz.timezone('Asia/Shanghai')
print(datetime.datetime.fromtimestamp(1632833354110/1000, tz).strftime('%Y-%m-%d %H:%M:%S'))

# date = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1632833354110/1000))
# print(date)
# print(time.localtime())


# datetime.datetime.fromtimestamp(un_time)



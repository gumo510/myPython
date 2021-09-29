# -- coding: utf-8 --

import time

import schedule

print("Starting")


def job():
    print("working...")


schedule.every(10).seconds.do(job)  # 每10秒执行一次
# schedule.every(10).minutes.do(job)  # 每10分钟执行一次
# schedule.every().hour.do(job)  # 每小时执行一次
# schedule.every().day.at("10:30").do(job)  # 每天十点半执行
# schedule.every(5).to(10).minutes.do(job)  # 不理解
# schedule.every().monday.do(job)  # 每周一执行
# schedule.every().wednesday.at("13:15").do(job)  # 每周三13点15执行
# schedule.every().minute.at(":17").do(job)  # 不理解

while True:
    schedule.run_pending()  # 运行所有可运行的任务
    time.sleep(1)

# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""参考https://pypi.org/project/schedule/
python提供标准库sched也可以用，没看"""
import schedule,os,time,datetime

def jobwarn():
    t=time.now = datetime.datetime.now()
    print t,"注意时间，早点休息。"

def job1s():
    print "1秒后关机"
    os.system("shutdown -s -t 1")
def job5s():
        print "5s后关机"
        os.system("shutdown -s -t 5")
def job60s():
    print "60s后关机"
    os.system("shutdown -s -t 60")
def job120s():
    print "120s后关机"
    os.system("shutdown -s -t 120")

def job_goon():
    print "再续一会"
    os.system("shutdown -a")
def job1_goon(info):
    print info,"再续一会"
    os.system("shutdown -a")

info="这是使用带参数的schedule方法；"

schedule.every().day.at("23:30").do(jobwarn)
schedule.every().day.at("23:58").do(job120s)
schedule.every().day.at("00:30").do(job5s)
schedule.every().day.at("00:45").do(job5s)
schedule.every().day.at("01:00").do(job5s)
schedule.every().day.at("01:15").do(job5s)
schedule.every().day.at("01:28").do(job120s)
schedule.every().day.at("01:45").do(job5s)
schedule.every().day.at("02:00").do(job1s)
schedule.every().day.at("02:15").do(job1s)
schedule.every().day.at("02:30").do(job1s)
schedule.every().day.at("02:45").do(job1s)

# schedule.every(5).seconds.do(jobwarn)

while True:
    schedule.run_pending()
    time.sleep(1)



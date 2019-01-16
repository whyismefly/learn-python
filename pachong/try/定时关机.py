# !/usr/bin/python
# -*- coding: UTF-8 -*-
"""参考https://pypi.org/project/schedule/
python提供标准库sched也可以用，没看"""

"""多线程参考https://www.cnblogs.com/znicy/p/6279930.html
http://www.cnblogs.com/math98/p/8980916.html
多进程multiprocessing这个复杂一些，https://www.cnblogs.com/kaituorensheng/p/4445418.html"""


import schedule,os,time,datetime,sys,multiprocessing
reload(sys)
sys.setdefaultencoding('utf-8')

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
def job1_goon():
    print "11111111111111111111111111111111"
    while True:
        info=raw_input("more:")
        if info == "s":
            print info, "再续一会"
            os.system("shutdown -a")
        else:
            print "as plan"
def my_list():
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
    print "222222222222222222222222222"
    while True:
        schedule.run_pending()
        time.sleep(1)



if __name__ == "__main__":
    # p1 = multiprocessing.Process(target = my_list(), args = (2,))
    # p2 = multiprocessing.Process(target = job1_goon(), args = (3,))
    # p1.start()
    # p2.start()
    #进程只能运行args其那面的那个...
    processes = list()
    for i in range(5):
        p = multiprocessing.Process(target=my_list, args=('test',))
        p = multiprocessing.Process(target=my_list, args=('test',))
        print 'Process will start.'
        p.start()
        processes.append(p)

    print "OK"


#!usr/bin/python
# encoding:utf-8

#1.字符串转码
#参考https://blog.csdn.net/weixin_39701039/article/details/79576549
# encode#字符串转为二进制
# y= bytes(x,encoding='utf-8')
# # decode#二进制解码为特定编码
# x.decode('utf-8')
# x.decode('unicode_escape')

#2.读取方式
#参考https://blog.csdn.net/weixin_39701039/article/details/79576549
# f=open("常用点.py",'rb')#rb是用二进制的方式读取
# f=open("常用点.py",'wb')#wb是用二进制的方式读取

#3.简单的计划任务参考https://pypi.org/project/schedule/
# import schedule,
# def jobwarn():
#     t=time.now = datetime.datetime.now()
#     print t,"注意时间，早点休息。"
# def job1_goon(info):
#     print info,"再续一会"
#     os.system("shutdown -a")
# info = "这是使用带参数的schedule方法；"
# schedule.every().day.at("23:30").do(jobwarn)
# schedule.every(5).seconds.do(jobwarn)
# while True:
#     schedule.run_pending()
#     time.sleep(1)
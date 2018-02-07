#!/usr/bin/python
#encoding:utf-8

import time
while True:
        t = time.localtime()

        time.sleep(0.4)
        t1=time.localtime()
        if t!=t1:
            print("\r现在时刻: %d 年 %2d 月 %2d日 %2d 时 %2d 分 %2d 秒 星期 %d") \
                 % (t.tm_year, t.tm_mon, t.tm_mday, t.tm_hour, t.tm_min, t.tm_sec, t.tm_wday + 1),


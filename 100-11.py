#!/usr/bin/python
#encoding:utf-8
#  Python练习题要求如下：
#简述：话说有一对可爱的兔子，出生后的第三个月开始，每一月都会生一对小兔子。当小兔子长到第三
# 个月后，也会每个月再生一对小小兔子.
# 问题：假设条件，兔子都不死的情况下，问每个月的兔子总数为多少？

# month=int(raw_input("pls input time"))
# birth=month/3
#
# for i in range(birth):
#     rabit=

a1 = 1
b2 = 1
for i in range(1, 10):
        print '%12ld %12ld' % (a1, b2),
        if (i % 3) == 0:
            print ''
        a1 = a1 + b2
        b2 = a1 + b2
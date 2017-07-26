#!/usr/bin/python
#encoding:utf-8

#python3无需#encoding:utf-8，本就是Unicode可以使用#!/usr/bin/python3

# 题目：判断101-200之间有多少个素数，并输出所有素数。
# 程序分析：判断素数的方法：用一个数分别去除2到sqrt(这个数)，如果能被整除，则表明此数不是素数，反之是素数。


h = 0
leap = 1#管控打印
import math
# 直接使用import math调用sqrt出现无法识别sqrt的情况,可以用math.sqrt()处理掉，也可以用from math import sqrt
#%4d比%d长
for m in range(101,201):
    k = int(math.sqrt(m + 1))
    for i in range(2,k + 1):
        if m % i == 0:
            leap = 0
            break
    if leap == 1:
        print ('%4d' % m)
        h += 1
        if h % 10 == 0:
            print ('')
    leap = 1#重置leap
print( 'The total is %d' % h)


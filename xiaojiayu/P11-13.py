#!/usr/bin/python
# encoding:utf-8

member=['fbwifhb','frejihg','frhoiuhrfe','feuhgghuiwthgrkpogrkj']
print member
#末尾添加一个元素
member.append("hncfjkelwv fev heh w")
print member
#添加多个
member.extend(["hncfjkelwv fev heh w","feruiowrhjgopr"])
print member
print len(member)
#插入
member.insert(0,11111111111)
print member,len(member)
#删除的几种方式
member.remove(11111111111)
print member,len(member)
del member[0]
print member,len(member)
member.pop()
print member,len(member)
member.pop(0)
print member,len(member)
#切片从第一个开始，到第三个之前结束
print member[1:3]
#切片
print member[:]
#切片
print member[:3]


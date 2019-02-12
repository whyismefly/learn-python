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
list1=[123]
list2=[1234]
print list1>list2
list1=[123,465]
list2=[1234,111]
list3=[123,465]
print (list1<list2)and(list1==list3)
list4=list1+list2
print list4
list4 *= 4
print list4
print "dfwgfiuofrwefrgrhtyjgh" not in list4
print "123" not in list4
list5=[123,["nfiewufhehopi","hferhfgioehrg"],16516]
print 123 not in list5
print 123 not in list5[1]
print list5[1][1]
print list4.count(123)
print list4.count("123")
print list4.index(123)
#设置查询范围
print list4.index(123,3,7)
print list4
list4.reverse()
print list4
list4.sort()
print list4
list4.sort(reverse=True)
print list4
#切片拷贝的区别
list5=list4[:]
list6=list4
list4.sort()
print list5
print list6
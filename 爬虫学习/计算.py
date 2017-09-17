#!/usr/bin/python
# encoding:utf-8

#本金
benjin=60000
#年利率
yinhanglilv=0
#月化利率
yueyinhanglilv=(1+yinhanglilv)**(1./12)-1
print "月化利率",yueyinhanglilv
print (1+yueyinhanglilv)**12

#时间年
yinhangnianshu=3
#年收益利率
shouyililv=0.08
#月收益利率
yueshouyililv=(1+shouyililv)**(1./12)-1
print "月收益利率",yueshouyililv
print (1+yueshouyililv)**12

#分期数
fenqishu=24
#
yuebenjin=benjin/fenqishu

yinhangzong=benjin*((1+yinhanglilv)**yinhangnianshu)
print "总金额",yinhangzong

yinhangmeiyue=yinhangzong/fenqishu
print "每月",yinhangmeiyue
print "-" * 20

print benjin*yueshouyililv,"-------"

zonglirun=0
for i in range(fenqishu):
    lirun=benjin*yueshouyililv
    zonglirun+=lirun
    benjin=benjin-yinhangmeiyue+lirun
    print "第%s月 "%(i+1)
    print "利润   ",lirun
    print "利润总  ",zonglirun
    print "本金   ",benjin
    print "-"*20
    if (i+1)%12==0:
        print "-"*20,"第%s年   "%((i+1)/12),"-"*20

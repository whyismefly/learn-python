#!/usr/bin/python
# encoding:utf-8

#本金
benjin=120000

#年利率
yinhanglilv=0.03
#月化利率
yueyinhanglilv=(1+yinhanglilv)**(1./12)-1
print "月化利率",yueyinhanglilv

#时间年
yinhangnianshu=3
#年收益利率
shouyililv=0.08
#月收益利率
yueshouyililv=(1+shouyililv)**(1./12)-1
print "月收益利率",yueshouyililv




#分期数
fenqishu=35
#
yuebenjin=benjin/fenqishu

yinhangzong=benjin*((1+yinhanglilv)**yinhangnianshu)
print "总金额",yinhangzong

yinhangmeiyue=yinhangzong/fenqishu
print "每月",yinhangmeiyue
print "-" * 20

zonglirun=0
for i in range(35):
    lirun=benjin*yueshouyililv
    zonglirun+=lirun
    benjin=benjin-yinhangmeiyue+lirun
    # print "第%s月"%(i+1)
    # print "利润",lirun
    # print "利润总",zonglirun
    # print "本金 ",benjin
    print benjin
    # print "-"*20

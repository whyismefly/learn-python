#!/usr/bin/python
# encoding:utf-8

import tushare as ts
import matplotlib.pyplot as plt

#	https://blog.csdn.net/u010435562/article/details/76498613

# 读取Tushare的版本
vs = ts.__version__

print vs

# 获取个股历史交易数据：get_k_data
df1 = ts.get_k_data('600167', ktype='D', start='2017-03-06', end='2019-04-03')

print df1

# 获取历史复权数据：get_stock_basics
df2 = ts.get_stock_basics()

# 公开上市首日：timeToMarket
fd = df2.ix['600167']['timeToMarket']

print fd

# 获取个股以往交易历史的分笔数据明细
df3 = ts.get_tick_data('600167', date='2019-03-04')

# 显示最近的30笔交易数据
# print df3.head(30)

# 获取大单交易数据，默认为大于等于400手，数据来源于新浪财经：get_sina_dd
df4 = ts.get_sina_dd('600167', date='2019-03-04', vol=500)

print df4

# 开启一个双图例的窗口，定义为211和212
plt.figure(2, figsize=(12, 8), dpi=80)
ax1 = plt.subplot(211)
ax2 = plt.subplot(212)

# ax1（211窗口）显示最高价和最低价曲线
plt.sca(ax1)

# 显示网格：grid='on'
df1.high.plot(color='red', grid='on')
df1.low.plot(color='blue', grid='on')

# ax2（212窗口）显示成交量曲线
plt.sca(ax2)

df1.volume.plot(color='orange', grid='on')

plt.show()

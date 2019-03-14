#!/usr/bin/pytho
# encoding:utf-8

import tushare as ts
import pandas as pd
from pandas import Series,DataFrame
import lxml
from sqlalchemy import create_engine#这个不好用，一堆报错，还是用下面的官方工具吧
import mysql.connector
#matplotlib和seaborn都是比较常用的绘图工具，前者更加官方，后者好看更适合新手
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

#参考https://www.cnblogs.com/onemorepoint/p/7210789.html

# print ts.get_hist_data('600848') #一次性获取全部日k线数据
# df = ts.get_hist_data('000001',start='2017-01-01',end='2019-02-28')
# print df.head(10)
# print type(df)

# stock_info=ts.get_stock_basics()#大盘当日所有股票数据
# print stock_info
# stock_info.to_csv('1.csv')#在win7-32下正常，win10-64下乱码
# stock_info.to_csv("..\\data\\2.csv",index=False, header=False, encoding='utf_8_sig')#encoding='utf-8'无法解决问题,依然乱码...
# stock_info.to_csv(path_or_buf="..\\data\\1.csv",index=False, header=False, encoding='utf_8_sig')#encoding='utf-8'无法解决问题,依然乱码...#path_or_buf=可以省略不写

# list=list(stock_info)
# print list

# def get_all_stock_id():
#     #获取所有股票代码 forstock_info.index:
#     for i in stock_info.index:
#         print i
# print get_all_stock_id()

# today=ts.get_today_all()#当天所有股票
# print today
# today.to_csv("..\\data\\test01.csv",encoding='utf_8_sig')

# df = ts.get_index()
# print(df)

# data=ts.get_tick_data('300032','2019-02-01')
# print data

# data1=ts.get_today_ticks('300032')
# print(data1)

#mysql连接 以下两种方法都可以，方法一更实用

#尝试一 sqlalchemy
# # df = ts.get_hist_data('600300').iloc[:,:4]
# df = ts.get_hist_data('000001')
# engine = create_engine('mysql://root:root@localhost:3306/stock_test?charset=utf8')
# # engine = create_engine('mysql://root:root@localhost:3306/stock_test')
# # df.to_sql('tick_data600300',engine,if_exists='append')
# df.to_sql('tick_data000001',engine,if_exists='append')
# df1 = pd.read_sql('tick_data000001',engine)
# print df1

# engine = create_engine('mysql://root:root@localhost:3306/stock_test')
# sql = '''select * from stock_test_tbl; '''
# # read_sql_query的两个参数: sql语句， 数据库连接
# df = pd.read_sql_query(sql, engine)
# # 输出employee表的查询结果
# print(df)
# #第一次执行仍报错，但是数据能导入，需要改进

"""
# 新建pandas中的DataFrame, 只有id,num两列
df = pd.DataFrame({'id': [1, 2, 3, 4], 'name': ['zhangsan', 'lisi', 'wangwu', 'zhuliu']})
# 将新建的DataFrame储存为MySQL中的数据表，储存index列
df.to_sql('mydf', engine, index=True)
print('Read from and write to Mysql table successfully!')
"""

#尝试二  官方工具mysql-connector-python
# mydb = mysql.connector.connect(
#     host="localhost",  # 数据库主机地址
#     user="root",  # 数据库用户名
#     passwd="root"  # 数据库密码
# )
# mycursor = mydb.cursor()
# mycursor.execute("SHOW databases")  # 0 为 第一条，1 为第二条，以此类推
# myresult = mycursor.fetchall()
# print myresult


# !/usr/bin/python2.7


#绘图

#通过matplotlib标准库绘图

# fig = plt.gcf()
# df = ts.get_hist_data('000001', start='2018-11-01')
# with pd.plotting.plot_params.use('x_compat', True):
#     df.high.plot(color='r', figsize=(10, 4), grid=True)
#     df.low.plot(color='b', figsize=(10, 4), grid=True)
#     fig.savefig('..\\data\\graph000001.png')


"""
# 绘图第一步是创建绘图窗口fig。
fig1 = plt.figure()
# 在窗口上添加AxesSubplot类型的子绘图区域，一个窗口可以添加多个子绘图区。
ax1 = fig1.add_subplot(2,2,1)
ax4 = fig1.add_subplot(2,2,4)
# 调用子绘图区的方法，可以绘制点线图、频数图、散点图等常用图形。
# 注意：在同一个subplot中多次调用plot()，所得到的图形是相互覆盖的。
ax1.plot(np.random.randn(50).cumsum(),'k--')
ax4.hist(np.random.randn(30))
# 主要关注以下几种方法：set_xlims设置坐标轴的上下限、set_ticks设置坐标刻度、set_ticklabel设置坐标标注。
ax1.set_xlim(-10,60)
ax1.set_xticks([0,20,40,60])
ax1.set_xticklabels(['a','b','c','d'])
# 用subplot的clear()方法可以清除现有的图形，用figure的savefig()保存图形到指定路径。
ax1.clear()
#windows下的路径
fig1.savefig('.\\test.png')
"""

#通过pandas绘图
# 1）plot方法及参数
# 对于Series和DataFrame类型的数据，可以直接调用两种类型对应的plot方法，绘图时自动采用索引值绘制横坐标，采用每一列数据绘
# 制纵坐标。这里分别以两类数据为例。
se1 = Series(np.random.randn(30).cumsum())
df = DataFrame({'a': np.random.randn(30), 'b': np.random.randn(30)})
# 2）频数图、散点图
# 频数图采用hist绘制即可，单幅的散点图还得依靠matplotlib库，但pandas提供多幅散点图矩阵的快速绘图方法。
se1.plot(kind = 'bar', color = 'g')
#对角线上图形设置为核密度图
pd.plotting.scatter_matrix(df, diagonal='kde')
# 3）清除和保存图形
# 有时候，我们希望清除掉当前图形或者干脆关闭绘图窗口。可以采用figure的clear()方法清除图形，采用matplotlib.pylab的
# close（）方法则能够直接关闭图形窗口。
# df.plot().get_figure().clear()
#清除绘图
#关闭窗口
# plt.close()

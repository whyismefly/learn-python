#!/usr/bin/python
# encoding:utf-8

import tushare as ts
import pandas as pd
import lxml
from sqlalchemy import create_engine#这个不好用，一堆报错，还是用下面的官方工具吧
import mysql.connector

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


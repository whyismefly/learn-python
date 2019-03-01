#!/usr/bin/python
# encoding:utf-8

import tushare as ts
import pandas
import lxml

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

today=ts.get_today_all()
print today

# df = ts.get_index()
# print(df)
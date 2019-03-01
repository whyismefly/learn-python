#!/usr/bin/python
# encoding:utf-8

import tushare as ts
import pandas
import lxml
# print ts.get_hist_data('600848') #一次性获取全部日k线数据
#
# df = ts.get_hist_data('000001',start='2017-01-01',end='2019-02-28')
# print df.head(10)
# print type(df)

stock_info=ts.get_stock_basics()
print stock_info
stock_info.to_csv('1.csv',index=False, header=False)
# list=list(stock_info)
# print list
# text = open( "stock.txt", "wb")
# text.write(list)
# text.close()
# def get_all_stock_id():
#     #获取所有股票代码 forstock_info.index:
#     for i in stock_info.index:
#         print i
# print get_all_stock_id()

# today=ts.get_today_all()
# print today

# df = ts.get_index()
# print(df)
#!/usr/bin/python
# encoding:utf-8

import tushare as ts
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import lxml
import sqlalchemy
from sqlalchemy import create_engine
import datetime
"""
Warning: Incorrect string value: '\xD6\xD0\xB9\xFA\xB1\xEA...' for column 'VARIABLE_VALUE' at row 475
  cursor.execute(statement, parameters)
python中使用sqlalchemy出现这个警告是因为mysql设置的默认字符是GBK，而导入的数据是UTF-
"""


stockid="000001"
stock_info=ts.get_stock_basics()
print stock_info
stock_hist_data = ts.get_hist_data(stockid)
print(stock_hist_data)

today=datetime.datetime.today()
engine = create_engine('mysql://root:root@localhost:3306/stock_test?charset=utf8')
# stock_info.to_sql(stockid+"_hist_data"+str(now),engine,if_exists='append')
"""这样会出现错误
   sqlalchemy.exc.OperationalError: (_mysql_exceptions.OperationalError) (1170, "BLOB/TEXT column 'code' used in key specification without a key length")
[SQL: CREATE INDEX `ix_000001_hist_data2019-03-29 00:50:54.318000_code` ON `000001_hist_data2019-03-29 00:50:54.318000` (code)]
(Background on this error at: http://sqlalche.me/e/e3q8)

https://blog.csdn.net/helloxiaozhe/article/details/83018347
error1170 也会出现，这个问题出现在当你设置一个VARCHAR字段为主键，但是却错误的设置了长度或者字符数，事实上，VARCHAR只能接受最大为256个字符串，但是你错误的设置成VARCHAR(512)等一些错误的设置，这些错误的设置会强制MySQL自动将VARCHAR(512)等转换成SMALLINT类型，同时这个字段被设置成primary key ，unique限制或者index索引等，然后执行操作就出现error 1170错误，解决问题的方法，为VARCHAR域指定小于256的长度。
"""
# stock_hist_data.to_sql(stockid+"_hist_data"+str(today),engine,if_exists='append',dtype={'code':sqlalchemy.types.VARCHAR(length=6)})
# #自己设定的VARCHAR长度，可修改，建议使用下行这种形式
stock_hist_data.to_sql(stockid+"_hist_data"+str(today),engine,if_exists='append',dtype={'code':sqlalchemy.types.VARCHAR(stock_hist_data.index.get_level_values("date").str.len().max())})


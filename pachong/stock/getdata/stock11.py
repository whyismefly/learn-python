#!/usr/bin/python
# encoding:utf-8

#分析山鹰
import tushare as ts
import pandas as pd
from pandas import Series,DataFrame
import numpy as np
import lxml
import sqlalchemy
from sqlalchemy import create_engine
import datetime

shanying_stockid="600567"
stock_hist_data=ts.get_hist_data(shanying_stockid)
# print stock_hist_data

# engine = create_engine('mysql://root:root@localhost:3306/stock_test?charset=utf8')
# # stock_info.to_sql(shanying_stockid+"_hist_data"+str(now),engine,if_exists='append')
# stock_hist_data.to_sql(shanying_stockid+"_hist",engine,if_exists='append',dtype={'date':sqlalchemy.types.VARCHAR(stock_hist_data.index.get_level_values("date").str.len().max())})
# shanying_data = pd.read_sql('600567_hist', engine)
# for i in shanying_data.index:
#     # print shanying_data.loc[1]
#     print shanying_data.loc[i]['close']

df = ts.get_sina_dd(shanying_stockid, date='2019-04-04')
print df
#!/usr/bin/python3
# encoding:utf-8

import tushare as ts
import pandas as pd
from pandas import Series,DataFrame
# from sqlalchemy import create_engine
# from sqlalchemy import VARCHAR
from sqlalchemy import *



def get_stocks_hist(stock_list):
    stock_hist = ts.get_hists(stock_list,start="2019-01-01",end="2020-03-17")
    print(stock_hist)
    engine = create_engine('mysql://root:root@localhost:3306/stock_info?charset=utf8')
    stock_hist.to_sql('stockhistinfo', engine, if_exists='append')
    # stock_hist.to_sql('stockhistinfo', engine, if_exists='append',dtype={"date":Date()})
    # stock_hist.to_sql('stockhistinfo', engine, if_exists='append', dtype={'date': VARCHAR(stock_hist.index.get_level_values('date').str.len().max())})
    df1 = pd.read_sql('stockhistinfo', engine)
    print(df1)

def get_basic_stockinfo_to_mysql():
    stock_info = ts.get_stock_basics()  # 大盘当日所有股票数据
    print(stock_info)
    engine = create_engine('mysql://root:root@localhost:3306/stock_info?charset=utf8')
    stock_info.to_sql('stockinfo',engine,if_exists='append',dtype={'code':VARCHAR(length=6)})
    df1 = pd.read_sql('stockinfo',engine)
    print (df1)

stock_list=["603019","002456","300232","600216","300296","002252"]
get_stocks_hist(stock_list)
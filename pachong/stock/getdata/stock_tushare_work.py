#!/usr/bin/python
# encoding:utf-8

import tushare as ts
import pandas as pd
import lxml
from sqlalchemy import create_engine#这个不好用，一堆报错，还是用下面的官方工具吧

def get_basic_stockinfo():
    stock_info = ts.get_stock_basics()  # 大盘当日所有股票数据
    print stock_info

def get_basic_stockinfo_to_mysql():
    stock_info = ts.get_stock_basics()  # 大盘当日所有股票数据
    # print stock_info
    engine = create_engine('mysql://root:root@localhost:3306/stock_test?charset=utf8')
    stock_info.to_sql('stockinfo',engine,if_exists='append')
    df1 = pd.read_sql('stockinfo',engine)
    print df1

def get_basic_stockinfo_to_mysql_choose(host,port,database):
    stock_info = ts.get_stock_basics()  # 大盘当日所有股票数据
    # print stock_info
    engine = create_engine('mysql://root:root@'+host+':'+port+'/'+database+'?charset=utf8')

    stock_info.to_sql('stockinfo',engine,if_exists='append')
    df1 = pd.read_sql('stockinfo',engine)
    print df1


get_basic_stockinfo_to_mysql_choose("localhost","3306","stock_test")
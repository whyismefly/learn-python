#!/usr/bin/python3
# encoding:utf-8

import tushare as ts
import pandas as pd
from pandas import Series,DataFrame
from sqlalchemy import *
import time

def get_stocks_hist(stock_list):
    for stock_code in stock_list:
        stock_hist = ts.get_hist_data(stock_code)
        stock_hist["code"] = stock_code
        # print(stock_hist)
        engine = create_engine('mysql://root:root@localhost:3306/stock_info?charset=utf8')
        stock_hist.to_sql('stockhistinfo', engine, if_exists='append',
                          dtype={'date': VARCHAR(stock_hist.index.get_level_values('date').str.len().max()),'code':VARCHAR(length=6)})
        # df1 = pd.read_sql('stockhistinfo', engine)
        # print(df1)

def get_basic_stockinfo_to_mysql():
    stock_info = ts.get_stock_basics()  # 大盘当日所有股票数据
    print(stock_info)
    engine = create_engine('mysql://root:root@localhost:3306/stock_info?charset=utf8')
    stock_info.to_sql('stockinfo',engine,if_exists='append',dtype={'name':NVARCHAR(length=32),'code':VARCHAR(length=6)})
    df1 = pd.read_sql('stockinfo',engine)
    print (df1)

def open_list(doc_path_name):
    with open(doc_path_name,mode='r',encoding="utf-8") as f:
        info = f.read()
        code_list=[]
        for line in info.split():
            if line.isdigit():
                code_list.append(line)
        print(code_list)
        return code_list

# stock_list=["603019","002456","300232","600216","300296","002252"]
# stock_list="603019"
# doc_path_name="G:/Desktop/code.txt"
# stock_list=open_list(doc_path_name)
# get_stocks_hist(stock_list)

get_basic_stockinfo_to_mysql()

# now=time.strftime('%Y-%m-%d',time.localtime(time.time()))
# print(now)
# get_basic_stockinfo_to_mysql
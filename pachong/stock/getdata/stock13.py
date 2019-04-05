#!/usr/bin/python
# encoding:utf-8

from sqlalchemy import *

from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.dialects.mysql import DOUBLE
# from sqlalchemy.dialects.mysql import \
#         BIGINT, BINARY, BIT, BLOB, BOOLEAN, CHAR, DATE, \
#         DATETIME, DECIMAL, DECIMAL, DOUBLE, ENUM, FLOAT, INTEGER, \
#         LONGBLOB, LONGTEXT, MEDIUMBLOB, MEDIUMINT, MEDIUMTEXT, NCHAR, \
#         NUMERIC, NVARCHAR, REAL, SET, SMALLINT, TEXT, TIME, TIMESTAMP, \
#         TINYBLOB, TINYINT, TINYTEXT, VARBINARY, VARCHAR, YEAR

# from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData, ForeignKey
# metadata = MetaData()

# https://blog.csdn.net/huangzhang_123/article/details/78616948
Base = declarative_base()
engine = create_engine('mysql://root:root@localhost:3306/stock_test?charset=utf8',echo=True,max_overflow=5)
# engine = create_engine("mysql+pymysql://root:root@127.0.0.1/test",encoding="utf-8",echo=True,max_overflow=5)
# engine = create_engine('mysql+pymysql://root:1234@localhost/test?charset=utf8', echo=False)
#echo=True显示生成sql，max_overflow是在初始线程数量的基础上，还能最多建立几个进程
# engine.execute("INSERT INTO ts_test (a, b) VALUES ('2', 'v1')")可以用这种方式直接执行sql

DBSession = sessionmaker(bind=engine)
session = DBSession()

# 定义类
class stock_hist_class(Base):
    __tablename__ = 'stock_hist_data'
    id = Column(BigInteger, primary_key=True)
    stockid=Column(String(10),index=True)
    date = Column(DateTime)
    open=Column(DOUBLE)
    high=Column(DOUBLE)
    close=Column(DOUBLE)
    low=Column(DOUBLE)
    volume=Column(DOUBLE)
    price_change=Column(DOUBLE)
    p_change=Column(DOUBLE)
    ma5=Column(DOUBLE)
    ma10=Column(DOUBLE)
    ma20=Column(DOUBLE)
    v_ma5=Column(DOUBLE)
    v_ma10=Column(DOUBLE)
    v_ma20=Column(DOUBLE)

Base.metadata.create_all(engine)

# # 动态添加字段
# # for i in range(3):
# #     setattr(stock_hist_class, 'Col' + str(i), (Column('Col' + str(i), String(50), comment='Col' + str(i))))
#
# Base.metadata.create_all(engine)
#
# # 添加数据
# dt = stock_hist_class(Col1='aaa', Col2="aaa")
# session.add(dt)
# session.commit()

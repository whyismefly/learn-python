#!/usr/bin/python
#encoding:utf-8

# 题目：输出指定格式的日期。
# 程序分析：使用 datetime 模块。

import time
import datetime

if __name__ == '__main__':
    #如果我们是直接执行某个.py文件的时候，该文件中那么”__name__ == '__main__'“是True,但是我们如果从另外
    # 一个.py文件通过import导入该文件的时候，这时__name__的值就是我们这个py文件的名字而不是__main__。

    # % y
    # 两位数的年份表示（00 - 99）
    # % Y
    # 四位数的年份表示（000 - 9999）
    # % m
    # 月份（01 - 12）
    # % d
    # 月内中的一天（0 - 31）
    # % H
    # 24
    # 小时制小时数（0 - 23）
    # % I
    # 12
    # 小时制小时数（01 - 12）
    # % M
    # 分钟数（00 = 59）
    # % S
    # 秒（00 - 59）
    #
    # % a
    # 本地简化星期名称
    # % A
    # 本地完整星期名称
    # % b
    # 本地简化的月份名称
    # % B
    # 本地完整的月份名称
    # % c
    # 本地相应的日期表示和时间表示
    # % j
    # 年内的一天（001 - 366）
    # % p
    # 本地A.M.或P.M.的等价符
    # % U
    # 一年中的星期数（00 - 53）星期天为星期的开始
    # % w
    # 星期（0 - 6），星期天为星期的开始
    # % W
    # 一年中的星期数（00 - 53）星期一为星期的开始
    # % x
    # 本地相应的日期表示
    # % X
    # 本地相应的时间表示
    # % Z
    # 当前时区的名称
    # % % % 号本身
    print time.time()
    print time.localtime(time.time())
    print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    print(datetime.date.today())
    print(datetime.date.today().strftime('%d/%m/%Y'))


    miyazakiBirthDate = datetime.date(1941, 1, 5)
    print(miyazakiBirthDate.strftime('%d/%m/%Y'))
    # 日期算术运算
    miyazakiBirthNextDay = miyazakiBirthDate + datetime.timedelta(days=1)
    print(miyazakiBirthNextDay.strftime('%d/%m/%Y'))

    # 日期替换
    miyazakiFirstBirthday = miyazakiBirthDate.replace(year=miyazakiBirthDate.year + 1)
    print(miyazakiFirstBirthday.strftime('%d/%m/%Y'))
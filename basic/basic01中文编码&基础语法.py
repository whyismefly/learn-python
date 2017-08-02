#!/usr/bin/python
#encoding:utf-8
#python2的学习 有时候用的是家里的python3环境

#!/usr/bin/python3

# print "Hello!"

print ("Hello!")

if True:
	print ("True")
else:
	print ("False")

# 多行语句
#
# Python语句中一般以新行作为为语句的结束符。
#
# 但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：
# total = item_one + \
#         item_two + \
#         item_three

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']

# Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """ ) 来表示字符串，引号的开始与结束必须的相同类型的。
#
# 其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。

word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""

# python中单行注释采用 # 开头。

# 等待用户输入
# 下面的程序执行后就会等待用户输入，按回车键后就会退出：

# raw_input("\n\nPress the enter key to exit.")

# 同一行显示多条语句
# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：

import sys; x = 'runoob'; sys.stdout.write(x + '\n')

# Print 输出
# print 默认输出是换行的，如果要实现不换行需要在变量末尾加上逗号：
#
# x="a"
# y="b"
# # 换行输出
# print x
# print y
#
# print '---------'
# # 不换行输出
# print x,
# print y,
#
# if expression :
#    suite
# elif expression :
#    suite
# else :
#    suite

# import 与# from ... import# 在# python
# 用import 或者from ... import 来导入相应的模块。 将整个模块(somemodule)导入，格式为： import somemodule




#
# 从某个模块中导入某个函数, 格式为： from somemodule import somefunction
#
# 从某个模块中导入多个函数, 格式为： from somemodule import firstfunc, secondfunc, thirdfunc
#
# 将某个模块中的全部函数导入，格式为： from somemodule import *
#
# 导入sys

import sys

print('================Python import mode==========================');
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)
# 导入 sys 模块的 argv, path 成员
from sys import argv, path  # 导入特定的成员

print('================python from import===================================')
print('path:', path)  # 因为已经导入path成员，所以此处引用时不需要加sys.path

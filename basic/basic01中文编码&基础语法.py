#!/usr/bin/python
# encoding:utf-8
#python2的学习 有时候用的是家里的python3环境

#!/usr/bin/python3

# print "Hello!"



"""Python中默认的编码格式是 ASCII 格式，在没修改编码格式时无法正确打印汉字，所以在读取中文时会报错。
解决方法为只要在文件开头加入 # -*- coding: UTF-8 -*- 或者 #coding=utf-8 就行了。"""

"""Python 标识符
在 Python 里，标识符由字母、数字、下划线组成。
在 Python 中，所有标识符可以包括英文、数字以及下划线(_)，但不能以数字开头。
Python 中的标识符是区分大小写的。
以下划线开头的标识符是有特殊意义的。以单下划线开头 _foo 的代表不能直接访问的类属性，需通过类提
供的接口进行访问，不能用 from xxx import * 而导入；
以双下划线开头的 __foo 代表类的私有成员；以双下划线开头和结尾的 __foo__ 代表 Python 里特殊方法专用的标
识，如 __init__() 代表类的构造函数。"""


"""Python 保留字符
下面的列表显示了在Python中的保留字。这些保留字不能用作常数或变数，或任何其他标识符名称。
所有 Python 的关键字只包含小写字母。
and	exec	not
assert	finally	or
break	for	pass
class	from	print
continue	global	raise
def	if	return
del	import	try
elif	in	while
else	is	with
except	lambda	yield"""

"""行和缩进
学习 Python 与其他语言最大的区别就是，Python 的代码块不使用大括号 {} 来控制类，函数以及其他逻辑判断。python 最具特色的就是用缩进来写模块。
缩进的空白数量是可变的，但是所有代码块语句必须包含相同的缩进空白数量，这个必须严格执行。"""


"""Python 引号
# Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """
# 来表示字符串，引号的开始与结束必须的相同类型的。
# 其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。
# word = 'word'
# sentence = "这是一个句子。"
# paragraph = """这是一个段落。
# 包含了多个语句""""""

print ("Hello!")

if True:
	print ("True")
else:
	print ("False")


""" 多行语句
#
# Python语句中一般以新行作为为语句的结束符。
#
# 但是我们可以使用斜杠（ \）将一行的语句分为多行显示，如下所示：
# total = item_one + \
#         item_two + \
#         item_three

days = ['Monday', 'Tuesday', 'Wednesday',
        'Thursday', 'Friday']
        
"""

"""Python 引号
# Python 可以使用引号( ' )、双引号( " )、三引号( ''' 或 """
""")来表示字符串，引号的开始与结束必须的相同类型的。
#
# 其中三引号可以由多行组成，编写多行文本的快捷语法，常用于文档字符串，在文件的特定地点，被当做注释。"""

word = 'word'
sentence = "这是一个句子。"
paragraph = """这是一个段落。
包含了多个语句"""




"""Python注释
# python中单行注释采用 # 开头。"""

"""# 等待用户输入
# 下面的程序执行后就会等待用户输入，按回车键后就会退出：

# raw_input("\n\nPress the enter key to exit.")"""

"""# 同一行显示多条语句
# Python可以在同一行中使用多条语句，语句之间使用分号(;)分割，以下是一个简单的实例：

import sys; x = 'runoob'; sys.stdout.write(x + '\n')"""

"""# Print 输出
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

"""


"""多个语句构成代码组
缩进相同的一组语句构成一个代码块，我们称之代码组。
像if、while、def和class这样的复合语句，首行以关键字开始，以冒号( : )结束，该行之后的一行或多行代码构成代码组。
我们将首行及后面的代码组称为一个子句(clause)。"""
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

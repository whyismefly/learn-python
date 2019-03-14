#!usr/bin/python
# encoding:utf-8

#1.字符串转码
#参考https://blog.csdn.net/weixin_39701039/article/details/79576549
# encode#字符串转为二进制
# y= bytes(x,encoding='utf-8')
# # decode#二进制解码为特定编码
# x.decode('utf-8')
# x.decode('unicode_escape')

#2.读取方式
#参考https://blog.csdn.net/weixin_39701039/article/details/79576549
# f=open("常用点.py",'rb')#rb是用二进制的方式读取
# f=open("常用点.py",'wb')#wb是用二进制的方式读取

#3.简单的计划任务参考https://pypi.org/project/schedule/
# import schedule,
# def jobwarn():
#     t=time.now = datetime.datetime.now()
#     print t,"注意时间，早点休息。"
# def job1_goon(info):
#     print info,"再续一会"
#     os.system("shutdown -a")
# info = "这是使用带参数的schedule方法；"
# schedule.every().day.at("23:30").do(jobwarn)
# schedule.every(5).seconds.do(jobwarn)
# while True:
#     schedule.run_pending()
#     time.sleep(1)

#4.Anaconda、conda、numpy、SciPy、matplotlib
# 参考https://www.jianshu.com/p/62f155eb6ac5
# Anaconda指的是一个开源的Python发行版本，其包含了conda、Python等180多个科学包及其依赖项。 [1]  因为包含了大量的科学包，
# Anaconda 的下载文件比较大（约 531 MB），如果只需要某些包，或者需要节省带宽或存储空间，也可以使用Miniconda这个较小的发
# 行版（仅包含conda和 Python）。Anaconda包括Conda、Python以及一大堆安装好的工具包，比如：numpy、pandas等
# Anaconda是一个科学计算环境，当在电脑上安装好Anaconda3以后，就相当于安装好了Python，还有一些常用的库，
# 如numpy，scrip，matplotlib等库。
# (如果你这里没有安装anaconda的话，直接安装了Python，装完Python 想要使用这些库的话 还要在cmd中运行 pip install …
# anaconda可以看做Python的一个集成安装，安装它后就默认安装了python、IPython、集成开发环境Spyder和众多的包和模块。非常方便。
# conda是包及其依赖项和环境的管理工具。适用语言：Python, R, Ruby, Lua, Scala, Java, JavaScript, C/C++, FORTRAN。跨平台。
# ⑤ pip 与 conda 比较
# → 依赖项检查
# pip：
# 不一定会展示所需其他依赖包。
# 安装包时或许会直接忽略依赖项而安装，仅在结果中提示错误。
# conda：
# 列出所需其他依赖包。
# 安装包时自动安装其依赖项。
# 可以便捷地在包的不同版本中自由切换。
# → 环境管理
# pip：维护多个环境难度较大。
# conda：比较方便地在不同环境之间进行切换，环境管理较为简单。
# → 对系统自带Python的影响
# pip：在系统自带Python中包的**更新/回退版本/卸载将影响其他程序。
# conda：不会影响系统自带Python。
# → 适用语言
# pip：仅适用于Python。
# conda：适用于Python, R, Ruby, Lua, Scala, Java, JavaScript, C/C++, FORTRAN。
# ⑥ conda与pip、virtualenv的关系
# conda结合了pip和virtualenv的功能。
# python在科学计算领域有三个非常受欢迎库，numpy、SciPy、matplotlib。numpy是一个高性能的多维数组的计算库，SciPy是构建在
# numpy的基础之上的，它提供了许多的操作numpy的数组的函数。SciPy是一款方便、易于使用、专为科学和工程设计的python工具包，
# 它包括了统计、优化、整合以及线性代数模块、傅里叶变换、信号和图像图例，常微分方差的求解等，SciPy完整的教程
# https://docs.scipy.org/doc/scipy/reference/index.html。下面就简单的介绍一下SciPy在图像处理方面的应用，如果专业做图像
# 处理当然还是建议使用opencv。本系列教程参考http://cs231n.github.io/python-numpy-tutorial/#scipy
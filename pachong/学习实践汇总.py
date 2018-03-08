# -*- coding: utf-8 -*-


"""实践中学习"""

"""开发环境"""
"""
1.安装python2.7（实际上我python2.7与python3.5混用），配置Python27和Python27\Scripts路径到系统环境变量
2.安装java1.8（java1.8以上才可以安装pycharm）
3.安装pycharm
4.安装firefox
5.上python挂网安装pip
6.通过pip安装以下自动化测试包
[
beautifulsoup4 (4.6.0)
distribute (0.6.35)
lpthw.web (1.1)
nose (1.3.7)
pip (9.0.1)
selenium (3.8.0)
setuptools (36.2.7)
virtualenv (15.1.0)
]
7.下载geckodriver（如果用chrome得另外下载对应的driver）
"""



"""记录python使用中的错误"""
"""
2017.12.17
在使用selenium+firefox进行自动化运维操作的期间遇到了两个问题，第一个：
selenium.common.exceptions.WebDriverException: Message: 'geckodriver' executable needs to be in PATH.
需要下载geckodriver，后面到https://github.com/mozilla/geckodriver/releases下载对应的版本后放到环境变量下的
目录中（python.exe位置那）即可解决。
后来下载后又出现：
selenium.common.exceptions.WebDriverException: Message: Unable to find a matching set of capabilities.
期初以为是selenium与firefox版本不对应，后来更换了两个版本还是不行，折腾了半天发现需要把firefox的安装目录（
家里电脑不是默认安装路径）添加到环境变量中，最终解决了。累计前后折腾了4小时，大部分时间都花在龟速下载
geckodriver和错误路径的配置上，真是要命...
"""
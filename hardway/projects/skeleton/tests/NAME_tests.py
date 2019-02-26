# encoding:utf-8

from nose.tools import *
import sys
# sys.path.append("E:\\learn\\GitHub\\learn-python\\hardway\\projects\\skeleton")
#直接添加实际目录
sys.path.append("..\\")
# sys.path.append("../")
#上面两种种写法都行，都是返回当前目录的上一层目录
import NAME
#import NAME 不能放在import sys和sys.path.append("E:\\learn\\GitHub\\learn-python\\hardway\\projects\\skeleton")前面，否则在pycharm中执行失败，在powershell中则无需这两句话

def setup():
    print "SETUP!"

def teardown():
    print "TEAR DOWN!"

def test_basic():
    print "I RAN!"


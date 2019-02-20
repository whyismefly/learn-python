#!usr/bin/python
# encoding:utf-8
a=list()
print a
b="fwhfjerqwofk'erkfpoerw"
b=list(b)
print b
print len(b)
print max(b)
b.append(1)
print b
print min(b)
print sorted(b)
print list(reversed(sorted(b)))
def function1(a,b):
    "dfwifuoheroigioer"
    return a+b
print function1(3,5)
print function1.__doc__#打印方法注释

def function2(*num1):
    "可变参数，类似形参"
    print len(num1)
    print "第一个参数",num1[0],"第二个参数",num1[1]
    print sum(num1)
    print num1
    print "_"*20
function2(123,312432435,342345)
#函数中的局部变量如果与全局变量名字相同在外部调用依然是全局变量，二者只是名字相同，地址不同。
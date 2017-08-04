#!/usr/bin/python
#encoding:utf-8

#这里argument是指实参
def print_two(*args):
    argv1,argv2=args
    print "argv1:%r,argv2:%r"%(argv1,argv2)

def print_two_again(argv1,argv2):
    print "argv1:%r,argv2:%r"%(argv1,argv2)

def print_one(argv1):
    print "argv1:%r"%(argv1)

def print_none():
    print "nothing"

print_two("zed","shaw")
print_two_again("zed","SHAW")
print_one("first")
print_none()

# Then we tell it we want *args (asterisk args), which is a lot like your argv parameter but
# for functions. This has to go inside () parentheses to work.
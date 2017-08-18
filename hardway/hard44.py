#!/usr/bin/python
# encoding:utf-8

"""
class Parent(object):
    def override(self):
        print "parent override()"
class Child(Parent):
    def override(self):
        print "child override()"

dad=Parent()
son=Child()

dad.override()
son.override()
"""
"""
class Parent(object):
    def altered(self):
        print "parent altered()"

class Child(Parent):
    def altered(self):
        print "child,before"
        super(Child,self).altered()
        print "child,after"

dad=Parent()
son=Child()

dad.altered()
son.altered()
"""

"""
class Parent(object):

    def override(self):
        print "parent override"

    def implicit(self):
        print "parent implicit"

    def altered(self):
        print "parent altered"

class Child(Parent):

    def override(self):
        print "child override"

    def altered(self):
        # print "child before altered"
        super(Child,self).altered()
        print "child after altered"

dad=Parent()
son=Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
print '-'*20
son.altered()

class Child(Parent):
    def __init__(self,stuff):
        self.stuff=stuff
        super(Child,self).__init__()
        
"""

class Other(object):

    def override(self):
        print "other override"

    def implicit(self):
        print "other implicit"

    def altered(self):
        print "other altered"

class  Child(object):
    def __init__(self):
        self.other=Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "child override"

    def altered(self):
        print "child,before"
        self.other.altered()
        print "child,after"

son=Child()

son.implicit()
son.override()
son.altered()
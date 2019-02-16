# !/usr/bin/python
# -*- coding: UTF-8 -*-

class Rectangle():
    def getPeri(self, a, b):
        return (a + b) * 2
    def getArea(self, a, b):
        return a * b

rect = Rectangle()
print(rect.getPeri(3, 4))
print(rect.getArea(3, 4))
print(rect.__dict__)


class Rectangle1():
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def getPeri(self):
        return (self.a + self.b) * 2
    def getArea(self):
        return self.a * self.b

rect = Rectangle1(3,4)
print(rect.getPeri())
print(rect.getArea())
print(rect.__dict__)

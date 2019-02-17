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

class Bird(object):
    def __init__(self):
          self.hungry = True
    def eat(self):
          if self.hungry:
               print 'Ahahahah'
          else:
               print 'No thanks!'

class SongBird(Bird):
     def __init__(self):
          # Bird.__init__(self)
          super(SongBird,self).__init__()
          self.sound = 'Squawk'
     def sing(self):
          print "gefkl;gjr;t"
sb = SongBird()
sb.sing()   #能正常输出
sb.eat()     #报错，因为songgird中没有hungry特性

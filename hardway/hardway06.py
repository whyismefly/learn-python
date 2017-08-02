#!/usr/bin/python
# -*- coding: utf-8 -*-

x="there are %d types of people"%10
binary="binary"
do_not="do_not"
y="those who know %s and those who %s"%(binary,do_not)

print x
#print默认换行
print y

print "i say:%s"%x
print "i say:%r"%x
print "i also say:'%s'"%y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"
print joke_evaluation % hilarious
print joke_evaluation % hilarious
print joke_evaluation % y

w = "This is the left side of..."
e = "a string with a right side."

print w + e
print w , e#比上面多了一个空格

# What is the difference between %r and %s?
#     Use the %r for debugging, since it displays the "raw" data of the variable, but the others
# are used for displaying to users.
# What's the point of %s and %d when you can just use %r?
#     The %r is best for debugging, and the other formats are for actually displaying variables to users.
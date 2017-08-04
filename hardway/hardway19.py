#!/usr/bin/python
#encoding:utf-8

def cheese_and_crakers(cheese_count,boxes_of_crakers):
    print "you have %d cheeses!"%cheese_count
    print "you have %d boxes of crakers!"%boxes_of_crakers
    print "man that's enouhg!"
    print "get a blanket.\n"

print "we can just give the function numbers directly:"
cheese_and_crakers(20,30)

print "or use variables from script:"
amount_of_cheese=10
amount_of_crakers=50

cheese_and_crakers(amount_of_cheese,amount_of_crakers)

print "do math:"
cheese_and_crakers(10+20,5+6)


print "combinne the variables and math:"
cheese_and_crakers(amount_of_cheese+100,amount_of_crakers+1000)

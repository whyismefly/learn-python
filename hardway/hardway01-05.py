#!/usr/bin/python
# -*- coding: utf-8 -*-
#encoding:utf-8

#02
print "hello"

#03
print "helloq", 25 + 30 / 6
print "helloqq", 100 - 25 * 3 % 4
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6
print 3 + 2 < 5 - 7
print "helloqq1", 3 + 2
print "helloqq11", 5 - 7
print "helloqq11?", 5 > -2
print "helloqq111", 5 >= -2
print "helloqq1111", 5 <= -2

#04
cars=100
space_in_a_car=4.0
drivers=30
passengers=90
cars_not_driven=cars-drivers
cars_driven=drivers
carpool_capacity=cars_driven*space_in_a_car
average_passengers_per_car=passengers/cars_driven
print "cars",cars
print "drivers",drivers
print "empty cars",cars_not_driven,"emptyempty"
print "passengers",passengers,"passengers"
print average_passengers_per_car,"average_passengers_per_car"

#05
my_name = 'Zed A. Shaw'
my_age = 35 # not a lie
my_height = 74 # inches
my_weight = 180 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'
print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)


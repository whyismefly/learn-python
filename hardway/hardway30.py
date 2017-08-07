#!/usr/bin/python
# encoding:utf-8

people=30
cars=40
buses=15

if cars>people:
    print "take cars."
elif cars<people:
    print "not take cars."
else:
    print "can't decide."

if buses>cars:
    print "too many buses."
elif buses<cars:
    print "take cars."
else:
    print "still can't decide."

if people>buses:
    print "take buses"
else:
    print "stay home."
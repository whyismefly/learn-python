#!/usr/bin/python
# encoding:utf-8

ten_things = "Apples Oranges Crows Telephone Light Sugar"
print "Wait there's not 10 things in that list, let's fix that."

stuff=ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

print stuff
while len(stuff)!=10:
    next_one=more_stuff.pop()
    print "add:",next_one
    stuff.append(next_one)
    print "%d items now"%len(stuff)

print "go:",stuff

print stuff[1]
print stuff[-1]
print stuff.pop()
print ' '.join(stuff)
print '#'.join(stuff[3:8])
print stuff

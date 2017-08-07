#!/usr/bin/python
# encoding:utf-8

print "#1 or #2?"
door=raw_input("> ")

if door=="1":
    print "bear eating cake."
    print "1.take cake."
    print "2.scream bear."

    bear=raw_input("> ")

    if bear=="1":
        print "bear eat ur face"
    elif bear=="2":
        print "bear eat ur leg"
    else:
        print "%s bear run"%bear

elif door=="2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity=raw_input("> ")
    if insanity=="1"or insanity=="2":
        print "Your body survives powered by a mind of jello. Good job!"
    else:
        print "The insanity rots your eyes into a pool of muck. Good job!"

else:
    print "You stumble around and fall on a knife and die. Good job!"
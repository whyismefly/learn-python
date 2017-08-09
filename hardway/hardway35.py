#!/usr/bin/python
# encoding:utf-8

from sys import exit

def gold_room():
    print "how much gold do you take?"

    next=raw_input("> ")
    if "0" in next or "1" in next:
        how_much=int(next)
    else:
       dead("Man, learn to type a number.")

    if how_much<50:
        print "you win!"
        exit(0)
    else:
        dead("greedy")

def bear_room():
    print "a bear here"
    print "the bear rich"
    print "it's in front of a door"
    print "how to move?"
    bear_moved=False

    while True:
        next=raw_input("> ")

        if next=="take money":
            dead("bear slaps you")
        elif next=="taunt bear"and not bear_moved:
            print "bear moved"
            bear_moved=True
        elif next=="taunt bear"and  bear_moved:
           dead("bear chew your leg")

        elif next=="open door" and bear_moved:
            gold_room()
        else:
            print "no idea."

def cthulhu_room():
    print "here's evil cthulhu_room"
    print "whatever stares at you and you go insane."
    print "Do you flee for your life or eat your head?"

    next=raw_input("> ")

    if "flee" in next:
        start()
    elif"head"in next:
        dead("tasty!")
    else:
        cthulhu_room()

def dead(why):
    print why,"good job!"
    exit(0)

def start():
    print "dark room"
    print "left door and ringht door"
    print "which do you take?"

    next=raw_input("> ")
    if next=="left":
        bear_room()
    elif next=="right":
        cthulhu_room()
    else:
        dead("stuble until strarve")

start()
#!/usr/bin/python
# encoding:utf-8

class MyStuff(object):
    def __init__(self):
        self.tangerine="And now a thousand years between"

    def apple(self):
        print "classy apples"

thing=MyStuff()
thing.apple()
print thing.tangerine
print "\n"

class Song(object):
    def __init__(self,lyrics):
        self.lyrics=lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line

happy_bday=Song(["Happy birthday to you",
"I don't want to get sued",
"So I'll stop right there"])

bulls_on_parade=Song(["They rally around the family",
"With pockets full of shells"])

happy_bday.sing_me_a_song()
print '-'*20

bulls_on_parade.sing_me_a_song()
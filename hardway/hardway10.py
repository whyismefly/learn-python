#!/usr/bin/python
# encoding:utf-8

print "i am 6'2\" tall."
# print "i am 6\'2" tall."

tabby_car="\ti'm tabbed in."
persian_cat="i'm split\non a line."
backslash_cat="i'm\\a\\cat"

fat_cat="""
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_car
print persian_cat
print backslash_cat
print "\\"+fat_cat
print "\'"+tabby_car
print "\""+tabby_car
print "\a"+tabby_car
print "\N"+tabby_car
print "\r"+tabby_car
print "\t"+tabby_car
print "\uxxxx"+tabby_car
print "\Uxxxxxxxx"+tabby_car
print "\v"+tabby_car
print "\ooo"+tabby_car
# print "\xhh"+tabby_car
#注意有几个Unicode only

# Here’s a tiny piece of fun code to try out:
while True:
    # for i in ["/","- ","|","\\","|"]:
    #     print "%s\r" % i,
    for i in [1,25,30]:
        print "%s\r" % i
#不加,这个符号则是累计输出，加了是单独输出
""" Always
        remember
        this: % r is
        for debugging;
        % s is
        for displaying."""
# Escape What it does.
# \\ Backslash (\)
# \' Single- quote (')
# \" Double- quote (")
# \a ASCII bell (BEL)
# \b ASCII backspace (BS)
# \f ASCII formfeed (FF)
# \n ASCII linefeed (LF)
# \N{name} Character named name in the Unicode database (Unicode only)
# \r ASCII carriage return (CR)
# \t ASCII horizontal tab (TAB)
# \uxxxx Character with 16- bit hex value xxxx (Unicode only)
# \Uxxxxxxxx Character with 32- bit hex value xxxxxxxx (Unicode only)
# \v ASCII vertical tab (VT)
# \ooo Character with octal value oo
# \xhh Character with hex value hh
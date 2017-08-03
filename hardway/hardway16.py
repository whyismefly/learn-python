#!/usr/bin/python
# encoding:utf-8
# close—Closes the fi le. Like File- >Save.. in your editor.
# read—Reads the contents of the fi le. You can assign the result to a variable.
# readline—Reads just one line of a text fi le.
# truncate—Empties the file. Watch out if you care about the file.
# write(stuff)—Writes stuff to the fi le.

from sys import argv
script,filename=argv

print "erade %r."%filename
print "stop to hit control+c"
print "hit return to go on "

raw_input("?")

print "open file..."
target=open(filename,'w')

print "truncating the file,bye"
target.truncate()

print "questions for 3 lines."

line1=raw_input("line1")
line2=raw_input("line2")
line3=raw_input("line3")

print "i'm going to write these to the file."

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "final"
target.close()

"""
Microsoft Windows [版本 6.1.7601]
版权所有 (c) 2009 Microsoft Corporation。保留所有权利。

C:\Users\Administrator>cd E:/GITHUBWORK/learn-python/hardway

C:\Users\Administrator>e:

E:\GITHUBWORK\learn-python\hardway>python hardway16.py test.txt
erade 'test.txt'.
stop to hit control+c
hit return to go on
?
open file...
truncating the file,bye
questions for 3 lines.
line1fbwuioefherio
line2reiughopergr
line3tioiopjghotjhtjph[ktp
i'm going to write these to the file.
final
"""
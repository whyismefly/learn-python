#!/usr/bin/python
#encoding:utf-8

print "practice."
print 'you\d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem="""
\tThe lovely world 
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "-------------"
print poem
print "-------------"

five=10-2+3-6
print "five=%s"%five

def sectet_fomula(started):
    jelley_beans=started*500
    jars=jelley_beans/1000
    crates=jars/100
    return jelley_beans,jars,crates

start_point=10000
beans,jars,crates=sectet_fomula(start_point)

print "start point:%d"%start_point
print "we have %d beans,%d jars,%d crates."%(beans,jars,crates)

start_point=start_point/10

print "another way:"
print "we have %d beans,%d jars,%d crates."%sectet_fomula(start_point)


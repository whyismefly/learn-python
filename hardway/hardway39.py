#!/usr/bin/python
# encoding:utf-8

"""
#list 只能调下标
things=['a','b','c','d']

print things
print things[1]
things[1]='z'
print things[1]
print things

#dict用{}

#词典插入方式是怎么样的
stuff={'name':'zed','age':36,'height':6*12+2}
print stuff['name']
print stuff['age']
print stuff["height"]
print stuff

stuff['city']='san francisco'
print stuff['city']
print stuff
print '\n'
stuff[1]='wow'
print stuff
stuff[2]='neato'
print stuff
print stuff[1]
print stuff[2]
print stuff

stuff['dis']='discuss'
print stuff
stuff[3]='hero'
print stuff
print '\n'


del stuff['city']
del stuff[1]
del stuff[2]
print stuff

"""

# create a mapping of state to abbreviation
states={
    'pregon':'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '- ' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '- ' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# do it by using the state then cities dict
print '- ' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '- ' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '- ' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '- ' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" %(state, abbrev, cities[abbrev])

print '- ' * 10
# safely get an abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Not Exist 334213')
print "The city for the state 'TX' is: %s" % city

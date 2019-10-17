# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex39.py
# Topic:       字典，可爱的字典
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# create a basic set of state and some cities in them
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# print some states
print '-' * 10
print "Michigan's abbreviation is :", states['Michigan']
print "Florida's abbreviation is :", states['Florida']

# do it by using the state then cities dict
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# print every state abbreviation
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# print every city in state
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# now do both at the same time
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])

print '-' * 10
# safely get a abbreviation by state that might not be there
state = states.get('Texas', None)

if not state:
    print "Sorry, no Texas."

# get a city with a default value
city = cities.get('TX', 'Does Note Exist')
print "The city for the state 'TX' is: %s" % city

# Q1:列表和字典有何不同？
# A:列表是有序排列的一些物件，而字典是将一些物件（键）对应到另外一些物件（值）的数据结构。

# Q2:字典能用在哪里？
# A:各种需要通过某个值去查看另一个值的场合。事实上，可以把字典当做“查询表”。

# Q3:列表能用在哪里？
# A:列表是专供有序排列的数据使用的。只要知道索引就能查到对应的值了。

# Q4:有没有办法弄一个可以排序的字典？
# A:看看Python里的collections.OrderedDict数据结构。上网搜索一下文档和用法。
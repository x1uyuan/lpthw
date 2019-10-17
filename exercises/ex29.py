# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex29.py
# Topic:       if语句
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------

people = 20
cats = 30
dogs = 15

if people < cats:
    print "Too many cats! The world is doomed!"

if people > cats:
    print "Not many cats! The world is saved!"

if people < dogs:
    print "The world is drooled on!"

if people > dogs:
    print "The world is dry!"

dogs += 5

if people >= dogs:
    print "People are greater than or equal to dogs."

if people <= dogs:
    print "People are less than or equal to dogs."

if people == dogs:
    print "People are dogs."

# Q1:+=是什么意思？
# A:x += 1和x = x + 1一样，只不过可以少打几个字母。你可以把它叫做“递增”运算符。你后面还会学到-=以及很多别的表达式。

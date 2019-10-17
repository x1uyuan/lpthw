# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex31.py
# Topic:       作出决定
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------

print "You enter a dark room with two doors.  Do you go through door #1 or door #2?"

door = raw_input("> ")

if door == "1":
    print "There's a giant bear here eating a cheese cake. What do you do?"
    print "1.Take the cake."
    print "2.Scream at the bear."

    bear = raw_input("> ")

    if bear == "1":
        print "The bear eats your face off. God job!"
    elif bear == "2":
        print "The bear eats your legs off. God job!"
    else:
        print "Well, doing %s is probably better. Bear runs away." % bear

elif door == "2":
    print "You stare into the endless abyss at Cthulhu's retina."
    print "1. Blueberries."
    print "2. Yellow jacket clothespins."
    print "3. Understanding revolvers yelling melodies."

    insanity = raw_input("> ")

    if insanity == "1" or insanity == "2":
        print "Your body survives powered by a mind of jello. God job."
    else:
        print "The insanity rots your eyes into a pool of muck. God job."

else:
    print "You stumble around and fall on a knife and die. God job."

# Q1:可以用多个if/else来取代elif吗？
# A:有时候可以，不过这也取决于if/else是怎样写的，而且这样一来Python就需要去检查每一处if/else，
#   而不是像if/elif/else一样，只要检查到第一个True就可以停下来了。试着写些代码看两者有何不同。

# Q2:怎样判断一个数处于某个值域中？
# A:两种办法：经典语法是使用1 < x < 10，用x in range(1, 10)也可以。

# Q3:怎样用if/elif/else块实现4个以上的条件判断？
# A:简单，多写几个elif块就可以了。

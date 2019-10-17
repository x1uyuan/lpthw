# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex30.py
# Topic:       else和if
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------

people = 30
cars = 40
buses = 15

if cars > people:
    print "We should take the cars."
elif cars < people:
    print "We should not take the cars."
else:
    print "We can't decide."

if buses > cars:
    print "That's too many buses."
elif buses < cars:
    print "Maybe we could take the buses."
else:
    print "We still can't decide."

if people > buses:
    print "Alright,let's just take the buses."
else:
    print "Fine ,let's stay home then."

# Q1:如果多个elif块都是True，Python会如何处理？
# A:Python只会运行它遇到的是True的第一个块，所以只有第一个为True的块会运行。
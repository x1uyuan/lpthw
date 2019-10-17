# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex44a.py
# Topic:       隐式继承
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------


class Parent(object):

    def implicit(self):
        print "PARENT implicit()"


class Child(Parent):
    pass


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

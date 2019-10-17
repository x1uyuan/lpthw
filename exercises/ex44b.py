# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex44b.py
# Topic:       显式覆盖
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------


class Parent(object):

    def override(self):
        print "PARENT override()"


class Child(Parent):

    def override(self):
        print "CHILD override()"


dad = Parent()
son = Child()

dad.override()
son.override()

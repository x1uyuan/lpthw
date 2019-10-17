# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex44c.py
# Topic:       在运行前或运行后替换
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------


class Parent(object):

    def altered(self):
        print "PARENT altered()"


class Child(Parent):

    def altered(self):
        print "CHILD, BEFORE PARENT altered()"
        super(Child, self).altered()
        print "CHILD, AFTER PARENT altered()"


dad = Parent()
son = Child()

dad.altered()
son.altered()

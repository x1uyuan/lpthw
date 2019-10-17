# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex24.py
# Topic:       更多练习
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------

print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print "------------"
print poem
print "------------"

five = 10 - 2 + 3 - 6
print "This should be five: %s" % five


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)

print "With a starting point of : %d" % start_point
print "We'd have %d beans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We 'd have %d beans, %d jars, and %d crates." % secret_formula(start_point)

# Q1:为什么你在后面把jelly_beans这个变量名又叫成了beans？
# A:这是函数的工作原理。记住函数内部的变量都是临时的，当你的函数返回以后，返回值可以被赋予一个变量。
#   我这里是创建了一个新变量，用来存放函数的返回值。

# Q2:倒着读代码是什么意思？
# A:从最后一行开始，把你写的代码和我写的代码进行比较。如果这一行完全一样，就接着比较上一行，直到全部比较完为止。

# Q3:这首诗是谁写的？
# A:我写的。我的诗也还可以吧。

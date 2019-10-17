# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex44e.py
# Topic:       合成
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------


class Other(object):

    def override(self):
        print "OTHER override()"

    def implicit(self):
        print "OTHER implicit()"

    def altered(self):
        print "OTHER altered()"


class Child(object):

    def __init__(self):
        self.other = Other()  # 主要理解这里——类的合成

    def implicit(self):
        self.other.implicit()

    def override(self):
        print "CHILD override()"

    def altered(self):
        print "CHILD, BEFORE OTHER altered()"
        self.other.altered()
        print "CHILD, AFTER OTHER altered()"


son = Child()

son.implicit()
son.override()
son.altered()

# Q1:怎样更好地自己解决在前面已经提到的新问题？
# A:提高解决问题能力的唯一方法就是自己去努力解决尽可能多的问题。很多时候人们遇到难题就会跑去找人给出答案。
#   当你手头的事情非要完成不可的时候，这样做是没有问题的，不过如果你有时间自己解决的话，那就花时间去解决吧。
#   停下手上的活，专注于你的问题，试着用所有可能的方法去解决，不管最后解决与否都要试到山穷水尽为止。
#   经过这样的过程，找到的答案会让你更为满意，而你解决问题的能力也会提高。

# Q2:对象是不是就是类的副本？
# A:有的语言里是这样的，如JavaScript。这样的语言叫做原型（prototype）语言，这种语言里的类和对象除了用法以外没多少不同。
#   不过在Python里类其实像是用来创建对象的模板，就跟制作硬币用到的模具一样。

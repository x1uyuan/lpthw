# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex28.py
# Topic:       布尔表达式练习
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------

print True and True
print False and True
print 1 == 1 and 2 == 1
print "test" == "test"
print 1 == 1 or 2 != 1
print True and 1 == 1
print False and 0 != 0
print True or 1 == 1
print "test" == "testing"
print 1 != 0 and 2 == 1
print "test" != "testing"
print "test" == 1
print not (True and False)
print not (1 == 1 and 0 != 1)
print not (10 == 1 or 1000 == 1000)
print not (1 != 10 or 3 == 4)
print not ("testing" == "testing" and "Zed" == "Cool Guy")
print 1 == 1 and not ("testing" == 1 or 1 == 0)
print "chunky" == "bacon" and not (3 == 4 or 3 == 3)
print 3 == 3 and not ("testing" == "testing" or "Python" == "Fun")

# Q1:为什么"test" and "test"返回"test"，1 and 1返回1，而不是返回True呢？
# A:Python和很多语言一样，都是返回两个被操作对象中的一个，而非它们的布尔表达式True或 False。
#   这意味着，如果你写了 False and 1，得到的是第一个操作数（False），而非第二个操作数（1）。多做几个实验。

# Q2:!=和<>有何不同？
# A:Python中!=是主流用法，<>将被逐渐废弃，除此以外没什么不同。

# Q3:有没有短路逻辑？
# A:有的。任何以False开头的and语句都会直接处理成False，不会继续检查后面语句。
#   任何包含True的or语句，只要处理到True，就不会继续向下推算，而是直接返回True了。
#   不过，还是要确保整个语句都能正常处理，以方便日后理解和使用代码。

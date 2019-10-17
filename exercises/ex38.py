# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex38.py
# Topic:       列表的操作
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------

ten_things = "Apples Oranges Crows Telephone Light Sugar"

print "Wait there's not 10 things in that list, let's fix that."

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print "Adding: ", next_one
    stuff.append(next_one)
    print "There's %d items now." % len(stuff)

print "There we go: ", stuff

print "Let's do some things with stuff."

print stuff[1]
print stuff[-1]
print stuff.pop()
print " ".join(stuff)
print len(stuff)
print '#'.join(stuff[3:5])

# Q1:你不是说别用while循环吗?
# A:是的。要记住，有时候如果你有很好的理由，那么规则也是可以打破的。死守着规则不放时不明智的。

# Q2:stuff[3:5]实现了什么功能？
# A:这是一个列表“切片”动作，它会从stuff列表的第3个元素开始取值，直到第5个元素。
#   注意，这里并不包含第5个元素，这跟range(3,5)的情况是一样的。

# Q3:为什么join(' ', stuff)不灵？
# A:join的文档写得有问题。其实它不是这么工作的，它是你要插入的字符串的一个方法函数，
#   函数的参数是你要连接的字符串构成的数组，所以应该写作' '.join(stuff)。

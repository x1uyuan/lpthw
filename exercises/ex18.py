# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex18.py
# Topic:       命名、变量、代码和函数
# Author:      dk-joker
# Created:     10-15-2019
# -------------------------------------------------------------------------------


# this one is like your scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)


# ok,that *args is actually pointless,we can just do this
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)


# this just takes one argument(参数)
def print_one(arg1):
    print "arg1: %r" % arg1


# this one takes no arguments
def print_none():
    print "I got nothin'."


print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()

# Q1:函数命名有什么规则？
# A:和变量名一样，只要以字母、数字以及下划线组成，而且不是数字开始，就可以了。

# Q2:*args里的*是什么意思？
# A:它的功能是告诉Python把函数的所有参数都接收进来，然后放到名叫args的列表中去。
#   和一直在用的 argv 差不多，只不过前者是用在函数上。如果没什么特殊情况，我们一般不会经常用到这个东西。

# Q3:这些任务好枯燥、好无聊啊。
# A:你这么感觉就对了，说明你有了进步。你能明白代码的功用，而且写错代码的情况在你身上很少发生了。
#   为了让任务不那么无聊，可以试着故意写错一些东西，看看会发生什么事情。

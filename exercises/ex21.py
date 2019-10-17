# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex21.py
# Topic:       函数可以返回某些东西
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------


def add(a, b):
    print "ADDING %d +%d" % (a, b)
    return a + b


def subtract(a, b):
    print "SUBTRACTING %d - %d" % (a, b)
    return a - b


def multiply(a, b):
    print "MULTIPLY %d * %d" % (a, b)
    return a * b


def divide(a, b):
    print "DIVIDE %d / %d" % (a, b)
    return a / b


print "Let's do some math with just functions!"

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d " % (age, height, weight, iq)

# A puzzle for the extra credit, type it in anyway.
print "Here is a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"

# Q1:为什么Python会把函数或公式倒着打印出来？
# A:其实不是倒着打印，而是自内而外打印。如果你把函数内容逐句看下去，你会发现其中的规律。试着搞清楚为什么说它是“自内而外”而不是“倒着”。

# Q2:怎样使用raw_input()输入自定义值？
# A:记得 int(raw_input())吧？不过这样也有一个问题，那就是无法输入浮点数，所以可以试着使用float(raw_input())。

# Q3:你说的“写一个公式”是什么意思？
# A:来个简单的例子：24 + 34 / 100 - 1023——把它转换成函数的形式。然后自己想一些数学式子，像公式一样用变量写出来。

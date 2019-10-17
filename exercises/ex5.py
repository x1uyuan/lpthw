# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex5.py
# Topic:       更多的变量和打印
# Author:      dk-joker
# Created:     10-14-2019
# -------------------------------------------------------------------------------

my_name = 'Zed A.Shaw'
my_age = 35  # not a lie
my_height = 74  # inches
my_weight = 180  # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Brown'

print "Let's talk about %s." % my_name
print "He's %d inches tall." % my_height
print "He's %d pounds heavy." % my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (my_eyes, my_hair)
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height, my_weight, my_age + my_height + my_weight)

# Q1:这样定义变量行不行：1 = 'Zed Shaw'？
# A:不行。1不是一个有效的变量名称。变量名要以字母开头，所以a1可以，但1不行。

# Q2:%s、%r和%d是做什么的？
# A:后面你会学到更多，现在可以告诉你的是，它们是一种“格式控制工具”。它们告诉Python把右边的变量带到字符串中，并且把变量的值放到%s所在的位置上。

# Q3:还是不懂，“格式控制工具”到底是什么？
# A:教你学编程的一个问题就是，你需要先学会编程，才能读懂我的一些描述。我解决这个问题的方法是让你先去做一些事情，后面我再解释。
#   当你碰到类似的问题时，把它们记录下来，看我是不是会在后面解释它们。

# Q4:如何将浮点数四舍五入？
# A:你可以使用round()函数，如round(1.7333)。

# Q5:我遇到了错误TypeError: 'str' object is not callable。
# A:很有可能你是漏写了字符串和变量之间的%。

# Q6:为什么我还是不明白？
# A:试着将脚本里的数字看成是你自己测量出来的数据，这样会很奇怪，但是多少会让你有身临其境的感觉，从而帮助你理解一些东西。

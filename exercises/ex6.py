# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex6.py
# Topic:       字符串和文本
# Author:      dk-joker
# Created:     10-14-2019
# -------------------------------------------------------------------------------

x = "there are %d types of people." % 10
binary = "binary"
do_not = "don't"
y = "those who know %s and those who %s." % (binary, do_not)

print x
print y

print "I said: %r." % x
print "I also said: '%s'." % y

hilarious = False
joke_evaluation = "Isn't that joke so funny?! %r"

print joke_evaluation % hilarious

w = "this is the left side of..."
e = "a string with a right side."

print w + e

# Q1:%r和%s有什么不同？
# A:%r用来做调试（debug）比较好，因为它会显示变量的原始数据（raw data），而%s和其他的符号则是用来向用户显示输出的。

# Q2:既然有%r了，为什么还要用%s和%d？
# A:%r用来调试最好，而其他格式符则是用来向用户显示变量的。

# Q3:如果你觉得很好笑，可不可以写一句hilarious = True？
# A:可以。在习题27中你会学到关于布尔函数的更多知识。

# Q4:为什么你在有些字符串上用单引号而在别的字符串上没有用？
# A:很大程度上只是个风格问题，我的风格就是在双引号的字符串中使用单引号，比如代码的第10行就是这样做的。

# Q5:我遇到了错误 TypeError: not all arguments converted during string formatting。
# A:确定每一行代码都完全正确。发生这种错误是因为你的字符串里的%格式化字符数量比后面给的变量多，仔细检查一下哪里写错了。

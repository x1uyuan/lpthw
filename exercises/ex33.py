# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex33.py
# Topic:       while循环
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------

i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    i = i + 1
    print "Numbers now :", numbers
    print "At the bottom i is %d" % i

print "The numbers: "

for num in numbers:
    print num

# Q1:“for循环和while循环有何不同？
# A:for循环只能对一些东西的集合进行循环，while循环可以对任何对象进行驯化。
#   然而，while循环比起来更难弄对，而一般的任务用for循环更容易一些。

# Q2:循环好难理解啊，我该怎样理解？
# 觉得循环不好理解，很大程度上是因为不会顺着代码的运行方式去理解代码。当循环开始时，它会运行整个代码块，代码块结束后回到开始的循环语句。
#   如果想把整个过程视觉化，可以在循环的各处塞入print语句，用来追踪变量的变化过程。
#   你可以在循环之“前、循环的第一句、循环中间及循环结尾都放一些print语句，研究最后的输出，并试着理解循环的工作过程。
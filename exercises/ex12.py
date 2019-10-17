# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex12.py
# Topic:       提示别人
# Author:      dk-joker
# Created:     10-14-2019
# -------------------------------------------------------------------------------

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weight? ")

print "So, you are %r old, %r tall and %r heavy." % (
    age, height, weight)

# Q1:运行pydoc时我怎么遇到SyntaxError: invalid syntax？
# A:你没有从命令行运行pydoc，很可能是从python里运行的。退出python试试。

# Q2:我的pydoc为什么不像你的那样会暂停？
# A:有时文档很短，一屏就显示完了，这时pydoc就不会暂停。

# Q3:运行pydoc看到more is not recognized。
# A:Windows的有些版本中没有这个命令，也就是说你没法用pydoc了。跳过这些附加练习，上网去搜索Python文档吧。

# Q4:%r和%s该用哪个？”
# A:记住%r是调试专用，它显示的是“原始表示”出来的字符，而%s是为了给用户显示。这个问题以后我就不再回答了，你要牢牢记住。
#   这个问题是人们重复问的最多的，如果同一个问题要问很多遍，那说明你没记住你该记住的东西。别问了，现在要你必须记住。

# Q5:写成print "How old are you?" , raw_input()为什么不行？
# A:你觉得可以，但Python不这么认为。我唯一能给你的答案是：不行就是不行。

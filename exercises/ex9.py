# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex9.py
# Topic:       打印，打印，打印
# Author:      dk-joker
# Created:     10-14-2019
# -------------------------------------------------------------------------------

# Here's some new strange stuff,remember type it exactly.

days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days:", days
print "Here are the months:", months

print """
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""

# Q1:怎样将每个月份显示在新的一行？
# A:字符串以\n 开始就可以了，像这样："\nJan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"。

# Q2:为什么使用%r时\n换行就不灵了？
# A:%r就是这个样子，它打印出的是你写出来的方式（或近似方式）。它是用来调试的“原始“格式。

# Q3:为什么在三引号之间加入空格就会出错？
# A:你必须写成"""而不是" " "，引号之间不能有空格。

# Q4:我的大部分错误都是拼写错误，是不是我太笨了？
# A:对于初学者甚至进阶学员来说，大部分编程中的错误都是拼写错误、录入错误或者没把别的一些简单东西弄对。


# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex8.py
# Topic:       打印，打印
# Author:      dk-joker
# Created:     10-14-2019
# -------------------------------------------------------------------------------

formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)

# Q1:我应该用%s还是用%r？
# A:你应该用%s，只有在想要获取某些东西的调试信息时才能用到%r。%r给你的是变量的“程序员原始版本”，又被称作“原始表示”（raw representation）。

# Q2:为什么“one”要用引号，而True和False不需要？
# A:因为True和False是Python的关键字，用来表示真和假的概念。如果加了引号，它们就变成了字符串，也就无法实现它们本来的功能了。
# 习题27中会有详细说明。

# Q3:我在字符中包含了中文（或者其他非ASCII字符），可是%r打印出的是乱码？
# A:使用%s打印就行了。

# Q4:为什么%r有时打印出来的是单引号，而我实际用的是双引号？
# A:Python会用最有效的方式打印出字符串，而不是完全按照你写的方式来打印。这样做对于%r来说是可以接受的，因为它是用于调试和排错的，没必要非打印出多好看的格式。

# Q5:为什么Python 3里这些都不灵？
# A:别使用Python 3。使用Python 2.7或更新的版本，尽管Python 2.6应该也没问题。

# Q6:可不可以使用IDLE运行这段代码？
# A:不行。你应该学习使用命令行。命令行对学习编程很重要，而且是学习编程的绝佳初始环境。IDLE在本书后面会让你失望的。
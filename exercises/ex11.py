# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex11.py
# Topic:       提问
# Author:      dk-joker
# Created:     10-14-2019
# -------------------------------------------------------------------------------

print "How old are you?",
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weight?",
weight = raw_input()

print "So,you're %r old, %r tall and %r heavy." % (
    age, height, weight)

# Q1:如何读取用户输入的数进行计算？
# A:这个有点算高级话题了。试试 x = int(raw_input())，它会把用户输入的字符串用int()转换成整数。

# Q2:我把身高写到原始输入raw_input("6'2")怎么不灵？
# A:不应该写成这样，只有从命令行输入才可以。首先回去把代码写成和我的一模一样，然后运行脚本，
#   当脚本暂停下来的时候，用键盘输入你的身高。这样做就可以了。

# Q3:为什么第8行要新写一行而不是放在一整行里边？
# A:这样是为了保持每行不多于 80 个字符，Python 程序员喜欢这样的风格。放在一整行里也不是不行。

# Q4:input()和raw_input()有何不同？
# A:input()函数会把你输入的东西当做 Python 代码进行处理，这么做会有安全问题，你应该避开这个函数。

# Q5:打印出来后我的字符串前面有个u，像u'35'这样。
# A:它表示Python告诉你你的字符串是Unicode。使用%s就一切正常了。
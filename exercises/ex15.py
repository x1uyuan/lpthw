# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex15.py
# Topic:       读取文件
# Author:      dk-joker
# Created:     10-15-2019
# -------------------------------------------------------------------------------

from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

print "Type the  filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

# Q1:txt = open(filename)返回的是文件的内容吗？
# A:不是，它返回的是一个叫做“file object”的东西，你可以把它想象成20世纪50年代的大型计算机上可以见到的古老的磁带机或者现代的 DVD 机。
#   你可以随意访问内容的任意位置，然后读取这些内容，不过这个文件本身并不是它的内容。

# Q2:我没法像你在附加练习7中说的那样在我的Terminal/PowerShell命令行下输入Python代码。
# A:首先，在命令行输入python然后按回车键。现在你就在python环境中了。接下来你就可以输入并运行一句一句的代码。
#   试着玩玩，如果想退出就输入quit()再敲回车。

# Q3:from sys import argv是什么意思？
# A:现在能告诉你的是，sys是一个软件包，这句话的意思是从该软件包中取出argv这个特性来，供我使用。后面你会学到更多相关的知识。

# Q4:我把文件名写进去，写成script, ex15_sample.txt = argv，不过这样不灵。
# A:这么做是错的。把代码写成和我一模一样的，然后照着我的方式从命令行运行。
#   你不需要把文件名放到代码中，而是让Python把文件名当做参数接纳进去。

# Q5:为什么文件打开了两次没有报错？
# A:Python 不会限制你打开文件的次数，事实上，有时候多次打开同一个文件是一件必须的事情。”

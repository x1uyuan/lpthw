# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex13.py
# Topic:       参数、解包和变量
# Author:      dk-joker
# Created:     10-14-2019
# -------------------------------------------------------------------------------

from sys import argv

script, first, second, third = argv

print "The script is called :", script
print "Your first variable is :", first
print "Your second variable is :", second
print "Your third variable is :", third

# Q1:运行时我遇到了ValueError: need more than 1 value to unpack。
# A:记住，有一个很重要的技能是注重细节。如果你仔细阅读并且完整重复了“应该看到的结果”部分的命令参数，你就不会看到这样的错误信息了。

# Q2:argv和raw_input()有什么不同？
# A:不同点在于用户输入的时机。如果参数是在用户执行命令时就要输入，那就是 argv，如果是在脚本运行过程中需要用户输入，那就使用raw_input()。

# Q3:命令行参数是字符串吗？
# A:是的，就算你在命令行输入数字，你也需要用int()把它先转成数字，和在raw_input()里一样。

# Q4:命令行该怎么使用？
# A:这个你应该已经学会了才对。如果你还没学会，就去读读附录的“命令行快速入门”吧。

# Q5:argv和raw_input()怎么不能合起来用。
# A:别想太多了。在脚本结尾加两行raw_input()随便读取点用户输入然后打印出来就行了，然后再慢慢在同一脚本中用各种方法玩玩这两样东西。

# Q6:为什么raw_input('? ') = x不灵？
# A:因为你写反了。照着我的写就没问题了。

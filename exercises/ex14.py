# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex14.py
# Topic:       提示和传递
# Author:      dk-joker
# Created:     10-14-2019
# -------------------------------------------------------------------------------

from sys import argv

script, user_name = argv
prompt = '>'

print "Hi %s, I'm the %s script." % (user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me, %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, computer)

# Q1:运行这段脚本时出现SyntaxError: invalid syntax。
# A:再次说明，你应该在命令行上而不是在Python环境中运行脚本。如果你先键入了python然后试图键入python ex14.py Zed，
#   就会出现这个错误，你这是在Python里运行Python。关掉窗口，重新键入python ex14.py Zed。

# Q2:修改提示符是什么意思？
# A:看变量定义prompt = '> '，将它改成一个不同的值。这个应该难不倒你，只是修改一个字符串而已，前面的13个习题都是围绕字符串的，自己花时间搞定。

# Q3:发生错误ValueError: need more than 1 value to unpack。
# A:记得上次我说过，你应该到“应该看到的结果”部分重复我的动作。把精力集中到我的输入，以及为什么我提供了一个命令行参数。

# Q4:我可以用双引号定义prompt变量的值吗？
# A:当然可以，试试看就知道了。

# Q5:你有台Tandy计算机？
# A:我小时候有过。运行时这段脚本时出现NameError: name 'prompt' is not defined。
#   要么拼错了 prompt，要么漏写了这一行。回去比较你写的和我写的，从最后一行开始直至第一行。

# Q6:怎样从IDLE中运行？
# A:不要使用IDLE。”

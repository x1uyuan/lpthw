# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex17.py
# Topic:       更多文件操作
# Author:      dk-joker
# Created:     10-15-2019
# -------------------------------------------------------------------------------

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % (from_file, to_file)

# we could do these two on one line too, how?
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready , hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close()

# Q1:为什么'w'要放在括号中？
# A:因为这是一个字符串，你已经学过一阵子字符串了，确定自己真的学会了。

# Q2:不可能把这写在一行里！
# A:取决于你的行是怎么定义的，例如，这样That ; depends ; on ; how ; you ; define ;one ; line ; of ; code。

# Q3:len()函数的功能是什么？
# A:它会以数的形式返回你传递的字符串的长度。试试吧。

# Q4:在我试图把代码写短时，我在最后关闭该文件时出现一个错误。
# A:很可能是你写了 indata = open(from_file).read()，这意味着你无需再运行in_file.close()了，因为read()一旦运行，文件就会被Python关掉。

# Q5:我觉得这个习题很难，这个是正常现象吗？
# A:是的，再正常不过了。也许在你看到习题 36 之前，甚至读完整本书，编程对你来说都还是一件很难理解的事情。
# 每个人的情况都不一样，坚持读书做练习，有问题的地方多研究，总会弄明白的。慢工出细活。

# Q6:我遇到了Syntax:EOL while scanning string literal错误。
# A:字符串结尾忘记加引号了。仔细检查那行看看。

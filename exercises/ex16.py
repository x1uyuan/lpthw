# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex16.py
# Topic:       读写文件
# Author:      dk-joker
# Created:     10-15-2019
# -------------------------------------------------------------------------------

from sys import argv

script, filename = argv

print "We're going to erase %r." % filename
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename, 'w+')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now I'm going to ask you for three lines."

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

target.write(line1 + "\n" + line2 + "\n" + line3)
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print "And finally, we close it."
target.close()

# Q1:如果用了'w'参数，truncate()是必需的吗？
# A:看看附加练习5。

# Q2:“w'是什么意思？
# A:它只是一个只有一个字符的特殊字符串，用来表示文件的访问模式。如果你用了'w'，那么你的文件就是“写入”（write）模式。
#   除了'w'以外，我们还有'r'表示“读取”（read），'a'表示“追加”（append）。

# Q3:还有哪些修饰符可以用来控制文件访问？
# A:当前最重要的一个是+修饰符，你可以用它来实现 'w+'、'r+'和'a+'。这样可以把文件用同时读写的方法打开，
#   每个符号会以不一样的方式实现文件内部的定位。

# Q4:如果只写open(filename)，那就使用'r'模式打开吗？
# A:是的，这是open()函数的默认模式。

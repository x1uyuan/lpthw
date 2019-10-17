# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex20.py
# Topic:       函数和文件
# Author:      dk-joker
# Created:     10-15-2019
# -------------------------------------------------------------------------------

from sys import argv

script, input_file = argv


def print_all(f):
    print f.read()


def rewind(f):
    f.seek(0)


def print_a_line(line_count, f):
    print line_count, f.readline(),


current_file = open(input_file)

print "First let's print the whole file:\n"

print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# Q1:print_all和其他函数里的f是什么？
# A:和习题18里的一样，f只是一个变量而已，不过在这里它指的是一个文件。Python里的文件就和老式磁带机或者DVD播放机差不多。
#   它有一个用来读取数据的“磁头”，你可以通过这个“磁头”来操作文件。每次运行f.seek(0)就回到了文件的开始，
#   而运行f.readline()则会读取文件的一行，然后将“磁头”移动到\n后面。后面会有更详细的解释。

# Q2:为什么文件里会有间隔空行？
# A:readline()函数返回的内容中包含文件本来就有的\n，而 print 在打印时又会添加一个\n，这样一来就会多出一个空行了。
#   解决方法是在 print 语句结尾加一个逗号（,），这样print就不会把它自己的\n打印出来了。

# Q3:为什么seek(0)没有把current_line设为0？
# A:首先seek()函数的处理对象是字节而非行，所以seek(0)只是转到文件的0 byte（也就是第一个字节）的位置。
#   其次，current_line只是一个独立变量，和文件本身没有任何关系，我们只能手动为其增值。

# Q4:+=是什么？
# A:英语里边it is可以写成it’s，you are可以写成you’re，这叫做简写。而+=这个操作符是把=和+简写到一起了。
#   x += y的意思和x = x + y是一样的。

# Q5:readline()是怎么知道每一行在哪里的？
# A:readline()里边的代码会扫描文件的每一个字节，直到找到一个\n为止，然后它停止读取文件，并且返回此前的文件内容。
#   文件f会记录每次调用readline()后的读取位置，这样它就可以在下次被调用时读取接下来的一行了。

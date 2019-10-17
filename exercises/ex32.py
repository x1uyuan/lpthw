# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex32.py
# Topic:       循环和列表
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'orange', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this first kind of for-loop goes through a list
for number in the_count:
    print "This is count %d" % number

# same as above
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# also we can go through mixed lists too
# notice we have to use %r since we don't know what's in it
for i in change:
    print "I got %r" % i

# we can also build lists, first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# now we can print them out too
for i in elements:
    print "Element was: %d" % i

# Q1:如何创建二维列表？
# A:就是在列表中包含列表，如[[1,2,3],[4,5,6]]。

# Q2:列表和数组不是一样的吗？
# A:取决于语言和实现方式。从经典意义上理解的话，列表和数组是很不同的，因为它们的实现方式不同。
#   在Ruby语言中列表和数组都被叫做数组，而在Python中又都叫做列表。现在我们就把它叫列表吧，因为Python里就是这么叫的。

# Q3:为什么for循环可以使用未定义的变量？
# A:循环开始时这个变量就被定义了，当然每次循环它都会被重新定义一次。

# Q4:“为什么for i in range(1, 3):只循环2次而非3次？
# A:range()函数会从第一个数到最后一个数，但不包含最后一个数。所以，它到2的时候就停止了，而不会到3。
#   这种含首不含尾的方式是循环中极其常见的一种用法。

# Q5:elements.append()是什么功能？
# A:它的功能是在列表的尾部追加元素。打开Python命令行，创建几个列表试验一下。
#   以后每次遇到自己不明白的东西，你都可以在Python shell中的交互地试验一下。
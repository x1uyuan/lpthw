# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex2.py
# Topic:       注释和#号
# Author:      dk-joker
# Created:     10-14-2019
# -------------------------------------------------------------------------------

# A comment, this is so you can read your program later.
# Anything after the # is ignored by python.

print "I could have code like this."  # and the comment after is ignored

# You can also use a comment to "disable" or comment out a piece of code:
# print "This won't run."

print "This will run."

# Q1:你确定#字符的名称是pound character？
# A:我叫它 octothorpe，这个名字没有哪个国家用作别的意思，而且所有的人都能看懂它的意思。

# Q2:如果#是注释的意思，那么为什么# -*- coding: utf-8 -*-能起作用呢？”
# A:Python其实还是没把这行当做代码处理，这种用法只是让字符编码格式被识别的一个取巧的方案，或者说是一个没办法的办法吧。
#   在编辑器设置里你还能看到一种类似的注释。

# Q3:为什么print "Hi # there."里的#没被忽略掉？
# A:这行代码里的#处于字符串内部，所以它就是引号结束前的字符串中的一部分，这时它只是一个普通字符，而不代表注释的意思。

# Q4:怎样做多行注释？
# A:每行前面放一个#就可以了。

# Q5:我们国家的键盘上找不到#字符，怎么办？
# A:有的国家要通过Alt键组合才能输入这个字符。你可以用搜索引擎找一下解决方案。

# Q6:为什么要让我倒着阅读代码？
# A:这样可以避免让你的大脑跟着每一段代码内容的意思走，这样可以让你精确处理每个片段，从而让你更容易发现代码中的错误。
#   这是一个很好使的查错技巧。

# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex7.py
# Topic:       更多打印
# Author:      dk-joker
# Created:     10-14-2019
# -------------------------------------------------------------------------------

print "Mary had a little lamb"
print "Its fleece was white as %s." % 'snow'
print "And everywhere that Mary went."
print "." * 10  # what 'd that do?

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma(逗号) at the end. try removing it to see what happens
print end1 + end2 + end3 + end4 + end5 + end6,
print end7 + end8 + end9 + end10 + end11 + end12

# Q1:“end”语句是什么原理？
# A:没有什么“end语句”，只是变量名里带了个“end”而已。

# Q2:为什么要用一个叫'snow'的变量？
# A:其实不是变量，而是一个内容为单词snow的字符串而已。变量名是不会带引号的。

# Q3:你在附加练习1里说在每一行代码的上面写一条注释，一定要这样做吗？
# A:不是。一般情况下加注释只是为了解释难懂的代码，或者注明为什么代码要这么写。一般来说后者更为重要。
#   遇到代码的确每一行都很难懂的特殊情况，加注释是正确的选择。在这里，我主要是为了让你逐渐学会将代码翻译成日常语言。

# Q4:创建字符串时是不是单引号和双引号都可以，它们有什么不同用途吗？
# A:Python里边两种都是可以的，不过一般单引号会被用来创建简短的字符串，如'a'、'snow'这样的。

# Q5:可以不用逗号，将最后两行写成一行输出吗？
# A:当然可以，不过这样一来这行的长度就超过80个字符了，从Python代码风格方面来讲这样做是不好的。
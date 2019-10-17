# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex3.py
# Topic:       数字和数学计算
# Author:      dk-joker
# Created:     10-14-2019
# -------------------------------------------------------------------------------

print "I will now count my chickens:"

print "Hens", 25 + 30 / 6

print "Roosters", 100 - 25 * 3 % 4

print "Now I will count the eggs:"

print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

print "Is it true that 3 + 2 < 5 - 7?"

print 3 + 2 < 5 - 7

print "What is 3 + 2?", 3 + 2
print "What is 5 - 7?", 5 - 7

print "Oh, that's why it's False."

print "How about some more."

print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

# Q1:为什么%是求余数符号，而不是百分号？
# A:很大程度上只是因为设计人员选择了这个符号而已。正常写作时它是百分号没错，在编程中除法我们用了/，而求余数又恰恰选择了%这个符号，仅此而已。

# Q2:%是怎么工作的？
# A:换个说法就是“X除以Y还剩余J”，例如“100除以16还剩4”。%运算的结果就是J这部分。

# Q3:运算优先级是怎样的？
# A:在美国，我们用 PEMDAS 这个简称来辅助记忆，它的意思是“括号（Parentheses）、指数（Exponents）、
#   乘（Multiplication）、除（Division）、加（Addition）、减（Subtraction）”，这也是Python里的运算优先级。

# Q4:为什么/（除法）算出来的比实际小？
# A:其实不是没算对，而是它将小数部分丢弃了，试试7.0 / 4.0和7 / 4比较一下，你就看出不同了。

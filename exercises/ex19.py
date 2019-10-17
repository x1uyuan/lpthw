# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex19.py
# Topic:       函数和变量
# Author:      dk-joker
# Created:     10-15-2019
# -------------------------------------------------------------------------------


def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheeses!" % cheese_count
    print "You have %d boxes_of_crackers!" % boxes_of_crackers
    print "Man that's enough for a party!"
    print "Get a blanket.\n"


print "We can just give the function numbers directly:"
cheese_and_crackers(20, 30)

print "OR, we can use variables from our script:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can even do math inside too:"
cheese_and_crackers(10 + 20, 5 + 6)

print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

# Q1:怎么能有10种不同的方式运行一个函数呢？
# A:信不信由你，理论上有无穷多种方式运行一个函数。在这里，试着按我在第8～12行给出的方式运行，当然你可以随意创新。

# Q2:有没有办法可以分析这个函数的功能，以便我能理解？
# A:有很多办法，最简单的一个办法是在每一行代码上面添加注释，另外一个办法是大声朗读代码，
#   还有一个办法就是把代码打印出来，用笔画一些图示，并写一些注释说明。

# Q3:怎样处理用户输入的数字，例如我想让用户输入cracker和cheese的数量？
# A:记住，使用int()把raw_input()的值转换为整数。

# Q4:第13行和第14行创建的变量会不会改变函数中的变量？
# A:不会。这些变量是在函数之外的，当它们被传递到函数中以后，函数会为这些变量创建一些临时的版本，当函数运行结束后，
#   这些临时变量就会被丢弃了，一切又回到了之前。继续阅读本书，后面你会更清楚这些概念。

# Q5:把全局变量（如第13行和第14行）的名称和函数变量的名称取成一样的，这样做是不是不好？
# A:是的，因为这样的话你就无法确定哪个是哪个了。有时候你可能会必须使用同一个变量名，
#   有时候你会不小心使用了一样的变量名，不论如何，只要有可能，还是尽量避免变量的名称相同。

# Q6:第12～19行是不是覆盖了函数cheese_and_crackers?
# A:没有，完全没有。这只是函数调用而已。基本上就是这里会跳转到函数的第一行，然后等函数运行完后再回到先前的位置，并没有用任何东西替换该函数。

# Q7:函数的参数个数有限制吗？
# A:取决于Python的版本和所用的操作系统，不过就算有限制，限值也是很大的。实际应用中，5个参数就不少了，再多就会让人头疼了。

# Q8:可以在函数中调用函数吗？
# A:可以。后面的习题中会用这一技巧写一个游戏。

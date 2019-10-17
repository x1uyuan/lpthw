# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex4.py
# Topic:       变量和命名
# Author:      dk-joker
# Created:     10-14-2019
# -------------------------------------------------------------------------------

cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# Q1:=（单等号）和==（双等号）有什么不同？
# A:=的作用是将右边的值赋给左边的变量名。==的作用是检查左右两边是否相等。习题27中你会学到==的用法。

# Q2:写成x=100而非x = 100也没关系吧？
# A:是可以这样写，但这种写法不好。操作符两边加上空格会让代码更容易阅读。

# Q3:词语间的空格有没有办法不让print打印出来？
# A:你可以通过这样的方法实现：print "Hey %s there." % "you"，后面马上就会讲到。

# Q4:怎样倒着读代码？
# A:很简单，假如说你的代码有16行，你就从第16行开始，和我的第16行比对，接着比对第15行，依此类推，直到全部检查完。

# Q5:为什么space用了4.0？
# A:这个主要就是为了让你见识一下浮点数，并且提出这个问题。看看附加练习吧

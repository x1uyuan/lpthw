# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex41.py
# Topic:       对象、类及从属关系
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------

## ??
class Animal(object):
    pass


## ??
class Dog(Animal):

    def __init__(self, name):
        ## ??
        self.name = name


## ??
class Cat(Animal):

    def __init__(self, name):
        ## ??
        self.name = name


## ??
class Person(object):

    def __init__(self, name):
        ## ??
        self.name = name
        ## ??
        self.pet = None


## ??
class Employee(Person):

    def __init__(self, name, salary):
        ## ??
        super(Employee, self).__init__(name)
        # ??
        self.salary = salary


## ??
class Fish(object):
    pass


## ??
class Salmon(Fish):
    pass


## ??
class Halibut(Fish):
    pass


## ??
rover = Dog("Rover")

## ??
satan = Cat("Satan")

## ??
mary = Person("Mary")

##  ??
mary.pet = satan

## ??
frank = Employee("Frank", 120000)

## ??
frank.pet = rover

## ??
flipper = Fish()

## ??
crouse = Salmon()

## ??
harry = Halibut()

# Q1:这些## ??注释是干嘛用的？
# A:这些注释是供你填空的。你应该在对应的位置填入is-a、has-a的概念。重读这个习题，看看其他的注释，仔细理解一下我的意思。

# Q2:这句self.pet = None有什么用？
# A:确保类的self.pet属性被设置为None。

# Q3:super(Employee, self).__init__(name)是做什么用的？
# A:这样你可以可靠地将父类的__init__方法运行起来。搜索“python super”，看看它的优缺点。
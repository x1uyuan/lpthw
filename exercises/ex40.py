# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex40.py
# Topic:       模块、类和对象
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------


class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_me_a_song(self):
        for line in self.lyrics:
            print line


happy_bday = Song(["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"])

bulls_on_parade = Song(["They rally around the family",
                        "With pockets full of shells"])

happy_bday.sing_me_a_song()

bulls_on_parade.sing_me_a_song()

# Q1:为什么创建__init__或者别的类函数时需要多加一个self变量？
# A:如果不加self，cheese = 'Frank'这样的代码意义就不明确了，它指的既可能是实例的cheese属性，也可能是一个叫做cheese的局部变量。
#   有了self.cheese = 'Frank'就清楚地知道这指的是实例的属性self.cheese。

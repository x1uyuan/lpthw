# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex35.py
# Topic:       分支和函数
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------

from sys import exit


def gold_room():
    print "This room is full of gold. How much do you take?"

    next = raw_input("> ")
    if "0" in next or "1" in next:
        how_much = int(next)
    else:
        dead("Man, learn to type a number")

    if how_much < 50:
        print "Nice, you're not greedy, you win!"
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print "There is a bear here."
    print "The bear has a bunch of honey."
    print "The fat bear is in front of another door."
    print "How are you going to move the bear?"
    bear_moved = False

    while True:
        next = raw_input("> ")

        if next == "take honey":
            dead("The bear looks at you then slaps your face off。")
        elif next == "taunt bear" and not bear_moved:
            print "The bear has moved from the door. You can go through it now."
            bear_moved = True
        elif next == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif next == "open door" and bear_moved:
            gold_room()
        else:
            print "I got no idea what that means."


def cthulhu_room():
    print "Here you see the great evil Cthulhu."
    print "He,it ,whatever stares at you and you go insane."
    print "Do you flee your life or eat your head?"

    next = raw_input("> ")

    if "flee" in next:
        start()
    elif "head" in next:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print why, "God job!"
    exit(0)


def start():
    print "You are in a dark room."
    print "There is a door to your right and left."
    print "Which one do you take ?"

    next = raw_input("> ")

    if next == "left":
        bear_room()
    elif next == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


start()

# Q1:救命啊！太难了，我搞不懂！
# A:当你搞不懂的时候，就在每一行代码的上方写下注释，向自己解释这一行的功能。在这个过程中如果有了新的理解，就随时修正自己前面的注释。
#   注释完后，就画一个工作原理的示意图，或者写一段文字表述一下。这样你就能弄懂了。

# Q2:为什么是while True:？
# A:这样可以创建一个无限循环。

# Q3:exit(0)有什么功能？
# A:在很多类型的操作系统里，exit(0)可以中断某个程序，而其中的数字参数则用来表示程序是否是遇到错误而中断的。
#   exit(1)表示发生了错误，而 exit(0)则表示程序是正常退出的。这和我们学的布尔逻辑0==False正好相反，不过你可以用不一样的数字表示不同的错误结果。
#   比如，你可以用exit(100)来表示另一种和exit(2)或exit(1)不同的错误。

# Q4:为什么raw_input()有时写成raw_input('> ')？
# A:raw_input的参数是一个会被打印出来的字符串，这个字符串一般用来提示用户输入。

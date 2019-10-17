# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex26.py
# Topic:       恭喜你，现在可以考试了
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------

import ex25


def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    """Sorts the words."""
    return sorted(words)


def print_first_word(words):  # 这里少了个：
    """Prints the first word after popping it off."""
    word = words.pop(0)  # 这里应该是pop而不是poop
    print word


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)  # 这里少了个）
    print word


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sort_words(words)


def print_first_and_last(sentence):
    """Prints the first and last words of the sentence."""
    words = break_words(sentence)
    print_first_word(words)
    print_last_word(words)


def print_first_and_last_sorted(sentence):
    """Sorts the words then prints the first and last one."""
    words = sort_sentence(sentence)
    print_first_word(words)
    print_last_word(words)


print "Let's practice everything."
print 'You\'d need to know \'bout escapes with \\ that do \n newlines and \t tabs.'

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explantion
\n\t\twhere there is none.
"""

print "--------------"
print poem
print "--------------"

five = 10 - 2 + 3 - 6  # 这里计算出错了 应该-6
print "This should be five: %d" % five  # 这里%s应该改成%d


def secret_formula(started):
    jelly_beans = started * 500
    jars = jelly_beans / 1000  # 这里除号写错了
    crates = jars / 100
    return jelly_beans, jars, crates


start_point = 10000
beans, jars, crates = secret_formula(start_point)  # 这里的==因该改成= 参数名写错了应该是下划线

print "With a starting point of: %d" % start_point
print "We'd have %d jeans, %d jars, and %d crates." % (beans, jars, crates)

start_point = start_point / 10

print "We can also do that this way:"
print "We'd have %d beans, %d jars, and %d crabapples." % secret_formula(start_point)  # 这里少了个）而且point少了个i

sentence = "All god\tthings come to those who weight."

words = ex25.break_words(sentence)
sorted_words = ex25.sort_words(words)

print_first_word(words)
print_last_word(words)
print_first_word(sorted_words)  # 这里多了个.
print_last_word(sorted_words)
sorted_words = ex25.sort_sentence(sentence)
print sorted_words  # 这里print少了个t

print_first_and_last(sentence)  # 这里函数名写错了

print_first_and_last_sorted(sentence)  # 这里函数名写错了而且参数也写错了

# Q1:一定要import ex25.py吗？移除对它的引用也可以吧？
# A:怎样都可以。不过这个文件里会用到ex25中的函数，你可以试着移除引用看看会怎样。

# Q2:我可以边修正代码边运行吗？
# A:当然可以。这样的事情就是要计算机帮忙，多多益善。

# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex25.py
# Topic:       更多更多的实践
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------


def break_words(stuff):
    """This function will break up words for us."""
    words = stuff.split(' ')
    return words


def sort_words(words):
    u"""Sorts(分类) the words."""
    return sorted(words)


def print_first_word(words):
    """Prints the first word after popping it off."""
    word = words.pop(0)
    print word


def print_last_word(words):
    """Prints the last word after popping it off."""
    word = words.pop(-1)
    print word


def sort_sentence(sentence):
    """Takes in a full sentence and returns the sorted words."""
    words = break_words(sentence)
    return sorted(words)


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

# Python 2.7.16 (default, Aug 24 2019, 18:37:03)
# [GCC 4.2.1 Compatible Apple LLVM 11.0.0 (clang-1100.0.32.4) (-macos10.15-objc-s on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> import ex25
# >>> sentence = "Everything is gonna be okay"
# >>> words = ex25.break_words(sentence)
# >>> words
# ['Everything', 'is', 'gonna', 'be', 'okay']

# Q1:有的函数打印出来的结果是None。
# A:也许你的函数漏写了最后的return语句。回到代码中检查一下是不是每一行都写对了。

# Q2:输入import ex15时显示-bash: import: command not found。
# A:注意看“应该看到的结果”部分。我是在Python中写的这句，不是在终端直接写的。你要先运行python再输入代码。

# Q3:输入import ex25.py时显示ImportError: No module named ex25.py。
# A:.py是不需要的。Python知道文件是.py结尾，所以只要输入import ex25即可。

# Q4:运行时提示SyntaxError: invalid syntax。
# A:这说明你在提示的那行有一个语法错误，可能是漏了半个括号或者引号，也可能是别的。一旦看到这种错误，
#   应该去对应的行检查代码，如果那一行没问题，就倒着继续往上检查每一行，直到发现问题为止。

# Q5:函数里的代码不是只在函数里有效吗？为什么words.pop(0)这个函数会改变words的内容？
# A:这个问题有点儿复杂，不过在这里 words 是一个列表，可以对它进行操作，操作结果也可以被保存下来。
#   这和操作文件f.readline()时的工作原理差不多。

# Q6:函数里什么时候该用print，什么时候该用return？
# A:print只是屏幕输出而已，你可以让一个函数既print又return值。明白这一点后，你就知道这个问题其实没什么意义。
#   如果你想要打印到屏幕，那就使用print；如果是想返回值，那就是用return。

# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex1.py
# Topic:       第一个程序
# Author:      dk-joker
# Created:     10-14-2019
# -------------------------------------------------------------------------------

print "Hello World!"
print "Hello Again"
print "I like typing this."
print "This is fun."
print 'Yay! Printing.'
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'

# Q1:我可不可以使用IDLE？
# A:不行。你应该使用OSX的终端或者Windows的PowerShell，和我这里演示的一样。如果你不知道如何用它们，可以去阅读附录的“命令行快速入门”。

# Q2:怎样让编辑器显示不同颜色？
# A:编辑之前先将文件保存为.py格式，如ex1.py，后面编辑时你就可以看到各种颜色了。

# Q3:运行ex1.py时看到SyntaxError: invalid syntax。
# A:你也许已经运行了Python，然后又在Python环境下运行了一遍Python。关掉并重启终端，重来一遍，只键入python ex1.py就可以了。

# Q4:遇到错误信息can’t open file 'ex1.py': [Errno 2] No such file or directory。
# A:你需要在自己创建文件的目录下运行命令。确保你事先使用 cd 命令进入了这层目录下。假如你的文件存在 lpthw/ex1.py 下面，
#   那你需要先执行 cd lpthw/再运行 python[…]

# Q5:怎样在代码中输入我们国家的语言文字？
# A:确认在文件开头加入了这行：# -*- coding: utf-8 -*-。

# Q6:我的文件无法运行，它直接回到了提示符，没有任何输出。
# A:很有可能是你把代码做了字面理解，认为print "Hello World!"就是让你在文件中打印"Hello World!"，于是你没有输入 print。
#   你的代码应该和我的一模一样。我的每行里边都有print，你的也要确保都有，这样代码才能正常运行。

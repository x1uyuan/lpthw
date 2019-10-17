# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex36.py
# Topic:       设计和调试
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------

import numpy as np

print "How many times do you want to flip a coin?"
times = int(raw_input(">"))
count = 0

for i in range(0, times):
    a = np.random.randint(2)
    if a > 0:
        count += 1
print "You have got %d times of upper side" % count

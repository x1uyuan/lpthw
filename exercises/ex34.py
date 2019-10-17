# -*- coding: utf-8 -*-
# -------------------------------------------------------------------------------
# Name:        ex34.py
# Topic:       访问列表的元素
# Author:      dk-joker
# Created:     10-16-2019
# -------------------------------------------------------------------------------

animals = ['bear', 'python', 'peacock', 'kangaroo', 'whale', 'platypus']

animals_size = len(animals)
count = 0

while count < animals_size:
    print "There is a %s in position %d" % (animals[count], count)
    count = count + 1

for i in range(0, animals_size):
    print "There is a %s in position %d" % (animals[i], i)

# -*- coding: utf-8 -*-
# @Time    : 2022/11/3 10:04

items = [(1, 'B'), (1, 'A'), (2, 'A'), (0, 'B'), (0, 'a')]
a = sorted(items)
b = sorted(items,key=lambda x:(x[0], x[1]))
print(items)
print(a)
print(b)
# -*- coding: utf-8 -*-
# @Time    : 2022/10/11 11:41

from functools import reduce

l = [i for i in range(10)]
print(l)

l1 = list(filter(lambda x:x%5==0, l))
print('l1:',l1)

l2 = reduce(lambda a,b:a+b+1, l)
print('l2:',l2)

l3 = list(map(lambda x:x**2, l))
print('l3:',l3)

print(l3)



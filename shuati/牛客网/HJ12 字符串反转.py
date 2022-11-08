# -*- coding: utf-8 -*-
# @Time    : 2022/9/27 19:46
# @Author  : liujia
# @File    : HJ12 字符串反转.py

string = 'abcd'#input()
n = len(string)
for i in range(n):
    print(string[n-i-1], end='')

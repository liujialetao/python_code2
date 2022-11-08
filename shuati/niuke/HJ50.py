# -*- coding: utf-8 -*-
# @Time    : 2022/10/6 18:44
a = '20*[-4/(8-6)+7]'#input()
st = a.replace('[', '(').replace(']', ')').replace('{', '(').replace('}', ')')


def func(i):
    nums = []
    flag = None
    while i < len(st):
        num = 0
        if st[i] == '(':
            i, num = func(i + 1)
        if flag == ')':
            return i, sum(nums)

        while i < len(st) and st[i].isdigit():
            num = num * 10 + int(st[i])
            i += 1
        if not nums:
            nums.append(num)
        if flag == '+':
            nums.append(num)
        elif flag == '-':
            nums.append(-num)
        elif flag == '*':
            nums.append(nums.pop() * num)
        elif flag == '/':
            nums.append(nums.pop() // num)
        if i < len(st): flag = st[i]
        i += 1
    return i, sum(nums)


print(func(0)[1])
print(func(0)[1])
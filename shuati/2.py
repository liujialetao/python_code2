# -*- coding: utf-8 -*-
# @Time    : 2022/10/10 23:38
# coding=UTF-8
def isValid(s):
    temp_str = []  # 存放临时开括号
    openParentheses = ["(", "[", "{"]
    combineParentheses = ["()", "[]", "{}"]
    for cha in s:
        if cha in openParentheses:  # 如果是开括号就放入temp_str中
            temp_str.append(cha)
        else:
            if not temp_str:  # 如果temp_str为空，返回False
                return False
            else:
                temp_cha = temp_str.pop() + cha  # 弹出，组合
                if temp_cha not in combineParentheses:
                    return False
    if not temp_str:  # 判断是否存在多余开括号
        return True
    else:
        return False


def calculate_maxDepth(string, left, right):
    depth = 0
    maxdepth = 0
    for c in string:
        if c == left:
            depth += 1
            maxdepth = max(depth, maxdepth)
        elif c == right:
            depth -= 1
    return maxdepth


string = input("Please input: ")
if isValid(string) == True:
    print(
    max(calculate_maxDepth(string, '(', ')'), calculate_maxDepth(string, '[', ']'),
        calculate_maxDepth(string, '{', '}')))
else:
    print(0)

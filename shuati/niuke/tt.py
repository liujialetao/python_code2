# -*- coding: utf-8 -*-
# @Time    : 2022/10/5 17:23
input_content = '580 72461'#input()
a, b = [int(ele) for ele in input_content.split()]


def split(a, b):
    m = max(a, b)
    yueshu = []
    for i in range(2, m+1):
        if i > a and i > b:
            break
        while (a % i == 0 or b % i == 0):
            yueshu.append(i)
            # 更新a b
            if a % i == 0:
                a = a // i
            if b % i == 0:
                b = b // i

    return yueshu


result = 1
for ele in split(a, b):
    result = result * ele
print(result)

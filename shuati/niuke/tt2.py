# -*- coding: utf-8 -*-
# @Time    : 2022/10/5 18:51
# while True:
#     try:
#         string = str(input().strip())
#         print(string[::-1])
#     except:
#         break

a = '0.3'#input()
a = float(a)
def f(n):
    if n>0:
        fuhao = 1
    elif n==0:
        return 0
    else:
        fuhao = -1

    absn = abs(n)
    c = 1
    a = min(absn,c)
    c = max(absn,c)
    while True:
        if a**3==absn:
            result =  a*fuhao
            break
        elif c**3==absn:
            result = c*fuhao
            break
        else:
            if abs(round(a-c,1))<0.2:
                if abs(a**3-absn) <  abs(c**3-absn):
                    return a*fuhao
                else:
                    return c*fuhao


            if a**3<absn and c**3>absn:
                b = round((a+c)/2,1)
                if b**3>absn:
                    c = b
                elif b**3==absn:
                    result = b
                    break
                else:
                    a = b

        print(a,c, a**3,c**3)
        print()
    return result
print(f(a))
pass

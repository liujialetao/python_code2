# #utf-8
# # class Solution:
# #     def countAndSay(self, n: int) -> str:
# #         for i in range(n):
# #             string='1'
# #             new_string=''
# #             for i in string:
# #
# #
# #
# #
# #             string=new_string
# string ='1211'#     111221
# new_string = ''
# n=len(string)
# zifu=string[0]
# count=1
# pre=string[0]
# for i in range(n-2,0,-1):
#     if string[i]!=pre:
#         #将之前的记录保存到new_string中
#         new_string += zifu + str(count)
#         #zifu与前一个不同，先记录下，并初始化count
#         zifu=string[i]
#         count=1
#     else:
#         #字符与之前相同的的话，count加1
#         count+=1
#     pre = string[i]
# new_string+=zifu+str(count)
# new_string=new_string[::-1]
# print(new_string)
# print(new_string)
#
#
#
#
import tensorflow as tf
print(tf.__version__)